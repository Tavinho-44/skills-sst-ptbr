#!/usr/bin/env python3
"""
detectar.py - painel de cinco verificações que dá uma nota de "cara de IA"
para um texto em português.

Adaptado de detect.py (linkedin-agent-skill, Jake Schincariol, licença MIT).

O que é: cinco heurísticas locais inspiradas nos sinais que detectores
públicos medem (variação do tamanho das frases, concretude, vocabulário de
muleta, marcas tipográficas e voz). Roda só na máquina, nada é enviado.

O que NÃO é: GPTZero, Originality, Copyleaks ou qualquer detector comercial.
Não chama essas ferramentas e não garante o veredito delas.

Cada verificação vai de 0 a 100. Quanto maior, mais humano.

Termos da lista "excecoes" do léxico (uso técnico de SST, como "jornada de
trabalho", "desbloquear" um equipamento, "transformador" elétrico) e trechos
entre aspas (citações) não contam como muleta.

Uso (a partir da pasta da Skill; no Windows use "python", em Linux/macOS "python3")
  python scripts/detectar.py rascunho.txt
  python scripts/detectar.py antes.txt depois.txt     # compara duas versões
  python scripts/detectar.py rascunho.txt --json
  python scripts/detectar.py - < rascunho.txt

Códigos de saída: 0 = rodou (mesmo que o texto não seja aprovado: o veredito
aparece na tela e no JSON); 2 = erro de uso (arquivo inexistente, texto vazio,
arquivo que não é UTF-8, léxico inválido).
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(AQUI, "lexico-ptbr.json")

FRASE_RE = re.compile(r"[^.!?\n]+[.!?]*")
PALAVRA_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ']+")
COLOQUIAL = re.compile(r"\b(?:pra|pro|pras|pros|tá|tô|né|a gente|daí|aí)\b", re.IGNORECASE)
PESSOA = re.compile(r"\b(?:eu|me|meu|minha|meus|minhas|comigo|nós|nosso|nossa|nossos|nossas|"
                    r"a gente|você|vocês|seu|sua|seus|suas|te|teu|tua|"
                    # português omite o sujeito: verbos comuns em 1ª pessoa contam como voz pessoal
                    r"fiz|vi|ouvi|aprendi|trabalhei|comecei|percebi|errei|tive|fui|sou|estou|estava|"
                    r"achei|perguntei|respondi|liberei|interditei|parei|faço|falo|acho|vejo|aprendemos|"
                    r"fizemos|tivemos|paramos|começamos)\b", re.IGNORECASE)
NUMEROS = re.compile(r"\b\d[\d.,]*%?|\bR\$\s?\d|\bNR-?\s?\d{1,2}\b")
SIGLAS = re.compile(r"\b[A-Z]{2,6}\b")
PROPRIOS = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-Ý][a-zà-ÿ]{2,}\b", re.MULTILINE)

CITACAO_RE = re.compile(r"“[^”\n]*”|\"[^\"\n]*\"|«[^»\n]*»")

VERIFICACOES = ["VARIAÇÃO", "CONCRETUDE", "MULETAS", "TIPOGRAFIA", "VOZ"]


def erro(msg):
    """Mensagem de erro de uso: vai para stderr e sai com código 2."""
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(2)


def configurar_utf8():
    # Console do Windows usa cp1252: força UTF-8 para acentos e emoji.
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def carregar_lexico(caminho):
    try:
        with open(caminho, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        erro(f"léxico não encontrado: {caminho}")
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        erro(f"léxico inválido ({caminho}): {e}")
    except OSError as e:
        erro(f"não foi possível abrir o léxico {caminho}: {e}")


def ler_entrada(caminho):
    """Lê o texto como UTF-8 (com ou sem BOM). A entrada padrão é lida em bytes,
    para não depender da página de código do console."""
    try:
        if caminho == "-":
            if sys.stdin is None or sys.stdin.isatty():
                erro("nenhum texto recebido na entrada padrão. "
                     "Passe um arquivo (ex.: rascunho.txt) ou redirecione: < rascunho.txt")
            dados = sys.stdin.buffer.read()
        else:
            with open(caminho, "rb") as fh:
                dados = fh.read()
    except FileNotFoundError:
        erro(f"arquivo não encontrado: {caminho}")
    except IsADirectoryError:
        erro(f"{caminho} é uma pasta, não um arquivo de texto")
    except OSError as e:
        erro(f"não foi possível ler {caminho}: {e}")
    try:
        texto = dados.decode("utf-8-sig")
    except UnicodeDecodeError:
        erro("o texto não está em UTF-8. Salve o arquivo como UTF-8 e tente de novo "
             "(no Bloco de Notas: Salvar como > Codificação UTF-8).")
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    if not texto.strip():
        erro("o texto está vazio")
    return texto


def limitar(n):
    return max(0.0, min(100.0, n))


def escala(valor, humano, maquina):
    if humano == maquina:
        return 50.0
    return limitar((valor - maquina) / (humano - maquina) * 100)


def frases(t):
    return [f.strip() for f in FRASE_RE.findall(t) if len(f.split()) > 2]


def palavras(t):
    return PALAVRA_RE.findall(t)


def v_variacao(t):
    tam = [len(f.split()) for f in frases(t)]
    if len(tam) < 4:
        return 50.0, "curto demais para avaliar"
    media = statistics.mean(tam)
    cv = statistics.pstdev(tam) / media if media else 0
    return escala(cv, 0.70, 0.22), f"variação {cv:.2f} em {len(tam)} frases (ideal 0,55+)"


def v_concretude(t):
    p = palavras(t)
    if len(p) < 25:
        return 50.0, "curto demais para avaliar"
    marcas = (len(NUMEROS.findall(t)) + len(set(PROPRIOS.findall(t)))
              + len(set(SIGLAS.findall(t))))
    dens = marcas * 100 / len(p)
    return escala(dens, 6.0, 0.5), f"{marcas} marcas concretas (números, NRs, siglas, nomes), {dens:.1f} por 100 palavras (ideal 4+)"


def _padrao(termo):
    return re.compile(r"\b" + re.escape(termo).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)


def spans_excecao(t, lex):
    """Trechos em que um termo do léxico tem uso técnico de SST e não conta como muleta."""
    por_termo = {}
    for ex in lex.get("excecoes", []):
        try:
            padrao = re.compile(ex["contexto"], re.IGNORECASE)
        except re.error:
            continue
        spans = [m.span() for m in padrao.finditer(t)]
        for termo in ex["termos"]:
            por_termo.setdefault(termo.lower(), []).extend(spans)
    return por_termo


def v_muletas(t, lex):
    p = palavras(t)
    if not p:
        return 50.0, "vazio"
    # Citações entre aspas não são vocabulário do autor; ficam fora da contagem.
    t = CITACAO_RE.sub(lambda m: " " * len(m.group(0)), t)
    excecoes = spans_excecao(t, lex)
    total, achados = 0, []
    for e in lex["words"] + lex["phrases"]:
        spans = excecoes.get(e["find"].lower(), [])
        n = sum(1 for m in _padrao(e["find"]).finditer(t)
                if not any(a <= m.start() and m.end() <= b for a, b in spans))
        if n:
            total += n
            achados.append(e["find"])
    dens = total * 100 / len(p)
    det = f"{total} muletas, {dens:.1f} por 100 palavras"
    if achados:
        det += " (" + ", ".join(sorted(achados)[:4]) + (", ..." if len(achados) > 4 else "") + ")"
    return escala(dens, 0.0, 4.0), det


def v_tipografia(t, aceitar_curvas=False):
    invis = sum(1 for c in t if unicodedata.category(c) == "Cf")
    trav = t.count("—")
    curvas = 0 if aceitar_curvas else sum(t.count(c) for c in "‘’“”")
    retic = t.count("…")
    duro = sum(t.count(c) for c in "   ")
    total = invis * 4 + max(trav - 1, 0) * 2 + curvas + retic + duro  # um travessão é tolerado
    por_mil = total * 1000 / max(len(t), 1)
    det = f"{invis} invisíveis, {trav} travessões, {curvas} aspas curvas, {retic} reticências, {duro} espaços duros"
    return escala(por_mil, 0.0, 12.0), det


def v_voz(t, lex):
    p = palavras(t)
    if len(p) < 25:
        return 50.0, "curto demais para avaliar"
    por100 = 100 / len(p)
    coloq = len(COLOQUIAL.findall(t)) * por100
    pessoa = len(PESSOA.findall(t)) * por100
    marcas, nomes = 0, []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(t))
        except re.error:
            continue
        if n:
            marcas += n
            nomes.append(s["id"])
    itens = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•✅➡️]\s*(.+)$", t)]
    uniforme = len(itens) >= 3 and statistics.pstdev(itens) < 1.6
    nota = (escala(coloq, 1.5, 0.0) * 0.20
            + escala(pessoa, 7.0, 1.0) * 0.40
            + limitar(100 - marcas * 22) * 0.40)
    if uniforme:
        nota -= 12
        nomes.append("itens-uniformes")
    det = f"{pessoa:.1f} pronomes pessoais e {coloq:.1f} marcas coloquiais por 100 palavras, {marcas} estrutura(s) de IA"
    if nomes:
        det += " [" + ", ".join(nomes[:4]) + "]"
    return limitar(nota), det


def avaliar(t, lex, aceitar_curvas=False):
    r = {
        "VARIAÇÃO": v_variacao(t),
        "CONCRETUDE": v_concretude(t),
        "MULETAS": v_muletas(t, lex),
        "TIPOGRAFIA": v_tipografia(t, aceitar_curvas),
        "VOZ": v_voz(t, lex),
    }
    notas = [r[v][0] for v in VERIFICACOES]
    geral = statistics.mean(notas) * 0.6 + min(notas) * 0.4
    veredito = "APROVADO" if geral >= 70 and min(notas) >= 55 else ("REVISAR" if geral >= 50 else "SINALIZADO")
    return r, geral, veredito


def barra(n, largura=24):
    cheio = round(n / 100 * largura)
    return "#" * cheio + "." * (largura - cheio)


def mostrar(r, geral, veredito, rotulo=None, out=sys.stdout):
    titulo = "PAINEL DE DETECÇÃO" + (f"  -  {rotulo}" if rotulo else "")
    print("\n" + titulo, file=out)
    print("=" * max(len(titulo), 62), file=out)
    for v in VERIFICACOES:
        nota, det = r[v]
        print(f"  {v:<12} {barra(nota)} {nota:5.1f}", file=out)
        print(f"  {'':<12} {det}", file=out)
    print("-" * 62, file=out)
    print(f"  {'NOTA HUMANA':<12} {barra(geral)} {geral:5.1f}   {veredito}", file=out)
    if veredito != "APROVADO":
        pior = min(VERIFICACOES, key=lambda v: r[v][0])
        print(f"\n  Sinal mais fraco: {pior}. Corrija esse primeiro.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Dá uma nota de cara de IA para um texto em português. "
                                 "Código de saída 0 quando roda (aprovado ou não); 2 em erro de uso.")
    ap.add_argument("entrada", nargs="?", default="-", help="arquivo de texto em UTF-8, ou - para a entrada padrão")
    ap.add_argument("comparar", nargs="?", help="segundo arquivo, para antes/depois")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--aceitar-aspas-curvas", action="store_true",
                    help="não penaliza aspas curvas (texto formal, ABNT, documentos)")
    ap.add_argument("--lexico", default=LEX)
    a = ap.parse_args()

    configurar_utf8()
    lex = carregar_lexico(a.lexico)
    alvos = [(a.entrada, ler_entrada(a.entrada))]
    if a.comparar:
        if a.comparar == "-" or a.entrada == "-":
            erro("na comparação, passe os dois textos como arquivos (a entrada padrão serve para um só)")
        alvos.append((a.comparar, ler_entrada(a.comparar)))

    saida = []
    for nome, texto in alvos:
        r, geral, veredito = avaliar(texto, lex, a.aceitar_aspas_curvas)
        saida.append({"fonte": nome,
                      "verificacoes": {k: {"nota": round(v[0], 1), "detalhe": v[1]} for k, v in r.items()},
                      "nota_humana": round(geral, 1), "veredito": veredito})
        if not a.json:
            mostrar(r, geral, veredito, rotulo=os.path.basename(nome) if a.comparar else None)

    if a.json:
        print(json.dumps(saida if a.comparar else saida[0], indent=2, ensure_ascii=False))
    elif a.comparar:
        x, y = saida
        print(f"  {x['nota_humana']:.1f} {x['veredito']}  ->  {y['nota_humana']:.1f} {y['veredito']}   "
              f"({y['nota_humana'] - x['nota_humana']:+.1f})\n")
    # Texto não aprovado não é erro: o veredito está na saída. Código 0 sempre que rodou.


if __name__ == "__main__":
    main()
