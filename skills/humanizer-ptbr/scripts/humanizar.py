#!/usr/bin/env python3
"""
humanizar.py - tira as marcas mecânicas de um texto em português.

Adaptado de humanize.py (linkedin-agent-skill, Jake Schincariol, licença MIT).

Três passadas, nesta ordem:

  1. INVISÍVEIS   apaga caracteres que um teclado não produz: espaços de
                  largura zero, word joiners, hífens suaves, BOM, caracteres
                  de tag Unicode, espaços não separáveis.
  2. TIPOGRAFIA   travessão -> vírgula (só quando há 2 ou mais no texto; um só
                  é mantido), meia-risca -> hífen, aspas curvas -> retas
                  (desligável com --manter-aspas-curvas), reticências de um
                  caractere -> três pontos.
  3. LÉXICO       troca ou apaga as muletas do lexico-ptbr.json. Entradas com
                  replace null são só SINALIZADAS (concordância e contexto
                  pedem reescrita manual).

Nunca são alterados: URLs, e-mails, hashtags, trechos entre aspas (retas,
curvas ou «»), linhas de citação iniciadas por ">" e blocos de código.
Siglas e NRs não estão no léxico. Termos da lista "excecoes" do léxico (uso
técnico de SST, como "jornada de trabalho") não são sinalizados.
Estruturas ("não é sobre X, é sobre Y", trincas, perguntas empilhadas) são
apontadas, nunca reescritas automaticamente.

Uso (a partir da pasta da Skill; no Windows use "python", em Linux/macOS "python3")
  python scripts/humanizar.py rascunho.txt --relatorio
  python scripts/humanizar.py rascunho.txt -o limpo.txt --relatorio
  python scripts/humanizar.py rascunho.txt --json
  python scripts/humanizar.py - < rascunho.txt

Códigos de saída: 0 = rodou; 2 = erro de uso (arquivo inexistente, texto vazio,
arquivo que não é UTF-8, léxico inválido).
"""

import argparse
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(AQUI, "lexico-ptbr.json")

PROTEGER_RE = re.compile(
    r"```[\s\S]*?```"                       # blocos de código
    r"|(?m:^[ \t]*>.*$)"                    # linhas de citação (markdown)
    r"|https?://\S+|www\.\S+|\S+@\S+\.\S+|#[\wÀ-ÿ]+"
    r"|“(?:[^”\n]|\n(?![ \t]*\n))*”"       # aspas: podem quebrar linha,
    r"|\"(?:[^\"\n]|\n(?![ \t]*\n))*\""     # mas não atravessam linha em branco
    r"|«(?:[^»\n]|\n(?![ \t]*\n))*»"
)
FRASE_RE = re.compile(r"[^.!?\n]+[.!?]*")
MARCA = "\x01"  # posição onde uma muleta foi apagada
PONTUACAO = ",.;:!?"
_EMOJI = "\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F"
ZWJ_EMOJI_RE = re.compile("(?<=[" + _EMOJI + "])\u200d(?=[" + _EMOJI + "])")
ZWJ_GUARDA = "\x02"  # ZWJ de emoji composto, guardado durante a limpeza


def erro(msg):
    """Mensagem de erro de uso: vai para stderr e sai com código 2."""
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(2)


def configurar_utf8():
    # Console do Windows usa cp1252: força UTF-8 para acentos e emoji.
    for fluxo in (sys.stdout, sys.stderr):
        try:
            # newline="": o texto sai com as quebras de linha que o programa produz.
            fluxo.reconfigure(encoding="utf-8", newline="")
        except (AttributeError, ValueError):
            pass


def carregar_lexico(caminho=LEX):
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
    crlf = "\r\n" in texto
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    if not texto.strip():
        erro("o texto está vazio")
    return texto, crlf


def _cp(spec):
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def proteger(texto):
    guardados = []

    def guarda(m):
        guardados.append(m.group(0))
        return f"\x00P{len(guardados) - 1}\x00"

    return PROTEGER_RE.sub(guarda, texto), guardados


def restaurar(texto, guardados):
    for i, trecho in enumerate(guardados):
        texto = texto.replace(f"\x00P{i}\x00", trecho)
    return texto


def passada_invisiveis(texto, lex):
    achados = []
    texto = ZWJ_EMOJI_RE.sub(ZWJ_GUARDA, texto)
    for e in lex["invisible"]:
        cp = _cp(e["cp"])
        if isinstance(cp, tuple):
            padrao = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            padrao = re.escape(chr(cp))
        n = len(re.findall(padrao, texto))
        if n:
            achados.append({"nome": e["cp"] + " " + e["name"], "qtd": n,
                            "acao": "apagar" if e["action"] == "delete" else "espaço"})
            texto = re.sub(padrao, "" if e["action"] == "delete" else " ", texto)
    resto = [c for c in texto if unicodedata.category(c) == "Cf" and c != "\x00"]
    if resto:
        achados.append({"nome": "outros caracteres invisíveis", "qtd": len(resto), "acao": "apagar"})
        texto = "".join(c for c in texto if unicodedata.category(c) != "Cf" or c == "\x00")
    return texto.replace(ZWJ_GUARDA, "\u200d"), achados


def _troca_travessao(m):
    """Troca um travessão no meio da linha, olhando a pontuação vizinha."""
    s = m.string
    antes = s[m.start() - 1] if m.start() > 0 else "\n"
    depois = s[m.end()] if m.end() < len(s) else "\n"
    if antes.isdigit() and depois.isdigit():
        return "-"
    if depois == "\n":
        return ""
    if antes in PONTUACAO:
        return " "
    if depois in PONTUACAO:
        return ""
    return ", "


def passada_tipografia(texto, lex, manter_aspas=False):
    achados, mantidos = [], []

    # Travessão ou meia-risca no início da linha (diálogo ou marcador de lista): vira hífen.
    texto, n = re.subn(r"(?m)^([ \t]*)[—–](?!\d)[ \t]*(?=\S)", r"\1- ", texto)
    if n:
        achados.append({"nome": "— travessão no início de linha", "qtd": n, "para": "- (hífen)"})

    # Intervalo numérico com meia-risca: 10–20 -> 10-20.
    texto, n = re.subn(r"(?<=\d)[ \t]*–[ \t]*(?=\d)", "-", texto)
    if n:
        achados.append({"nome": "– meia-risca em intervalo", "qtd": n, "para": "-"})

    # Travessão no meio do texto: um só é tolerado (alinhado com SKILL.md e detectar.py);
    # com dois ou mais, todos viram vírgula (ou somem junto de pontuação).
    pad = re.compile(r"[ \t]*—[ \t]*|[ \t]+–[ \t]+")
    total = len(pad.findall(texto))
    if total == 1:
        mantidos.append({"nome": "travessão (um por texto é tolerado)", "qtd": 1})
    elif total >= 2:
        texto = pad.sub(_troca_travessao, texto)
        achados.append({"nome": "— travessão no meio da frase", "qtd": total, "para": ","})

    # Meia-risca restante (sem espaços) vira hífen.
    texto, n = re.subn("–", "-", texto)
    if n:
        achados.append({"nome": "– meia-risca", "qtd": n, "para": "-"})

    for e in lex["typographic"]:
        ch = e["from"]
        if ch in "—–":
            continue
        if manter_aspas and ch in "‘’“”":
            continue
        if ch == "′":
            texto, n = re.subn(r"(?<!\d)′", e["to"], texto)
        else:
            n = texto.count(ch)
            texto = texto.replace(ch, e["to"])
        if n:
            achados.append({"nome": f"{ch} {e['name']}", "qtd": n, "para": e["to"].strip() or "(espaço)"})
    return texto, achados, mantidos


def _mesma_caixa(origem, troca):
    if not troca:
        return troca
    if origem.isupper() and len(origem) > 1:
        return troca.upper()
    if origem[0].isupper():
        return troca[0].upper() + troca[1:]
    return troca


def _padrao(termo, sem_negacao=False):
    corpo = r"\b" + re.escape(termo).replace(r"\ ", r"\s+") + r"\b"
    if sem_negacao:
        corpo = r"(?<!não )" + corpo
    return re.compile(corpo, re.IGNORECASE)


def spans_excecao(texto, lex):
    """Trechos em que um termo do léxico tem uso técnico e não deve ser sinalizado."""
    por_termo = {}
    for ex in lex.get("excecoes", []):
        try:
            padrao = re.compile(ex["contexto"], re.IGNORECASE)
        except re.error:
            continue
        spans = [m.span() for m in padrao.finditer(texto)]
        for termo in ex["termos"]:
            por_termo.setdefault(termo.lower(), []).extend(spans)
    return por_termo


def _ocorrencias(padrao, texto, spans):
    """Ocorrências de um termo que não estão cobertas por uma exceção técnica."""
    return [m for m in padrao.finditer(texto)
            if not any(a <= m.start() and m.end() <= b for a, b in spans)]


def _tira_marca(m):
    s = m.string
    antes, depois = m.group(1), m.group(2)
    prox = s[m.end()] if m.end() < len(s) else "\n"
    ant = s[m.start() - 1] if m.start() > 0 else "\n"
    if prox in PONTUACAO + "\n":
        return ""
    if ant == "\n":
        return antes  # preserva a indentação
    return " " if (antes or depois) else ""


def passada_lexico(texto, lex):
    trocas, sinais = [], []
    excecoes = spans_excecao(texto, lex)
    entradas = sorted(lex["phrases"] + lex["words"], key=lambda e: len(e["find"]), reverse=True)
    for e in entradas:
        spans = excecoes.get(e["find"].lower(), [])
        if e["replace"] is None:
            achou = _ocorrencias(_padrao(e["find"]), texto, spans)
            if achou:
                sinais.append({"termo": e["find"], "qtd": len(achou), "familia": e["family"]})
            continue
        if e["replace"] == "":
            # Não apaga "é importante ressaltar que" depois de "não": mudaria o sentido.
            todos = len(_padrao(e["find"]).findall(texto))
            padrao = _padrao(e["find"], sem_negacao=True)
            achou = len(padrao.findall(texto))
            if todos > achou:
                sinais.append({"termo": e["find"] + " (depois de \"não\", conferir à mão)",
                               "qtd": todos - achou, "familia": e["family"]})
            if achou:
                trocas.append({"termo": e["find"], "por": "(apagado)", "qtd": achou, "familia": e["family"]})
                texto = padrao.sub(MARCA, texto)
        else:
            padrao = _padrao(e["find"])
            achou = len(padrao.findall(texto))
            if achou:
                trocas.append({"termo": e["find"], "por": e["replace"], "qtd": achou, "familia": e["family"]})
                texto = padrao.sub(lambda m: _mesma_caixa(m.group(0), e["replace"]), texto)

    # Arrumação feita só em volta das muletas apagadas; o resto do texto fica como está.
    texto = re.sub(MARCA + r"[ \t]*,?[ \t]*", MARCA, texto)
    # Início de frase onde a muleta foi apagada: capitaliza a palavra seguinte.
    texto = re.sub(r"(^|[.!?][ \t]+|\n[ \t]*)" + MARCA + r"+([a-zà-ÿ])(?=[a-zà-ÿ]*(?![A-Za-zÀ-ÿ0-9(]))",
                   lambda m: m.group(1) + m.group(2).upper(), texto)
    # Vírgula que sobraria antes do fim da frase: "foi bom, em suma." -> "foi bom."
    texto = re.sub(r",[ \t]*" + MARCA + r"+(?=[ \t]*[.!?])", MARCA, texto)
    texto = re.sub(r"([ \t]*)" + MARCA + r"+([ \t]*)", _tira_marca, texto)
    return texto, trocas, sinais


def varrer_estruturas(texto, lex):
    sinais = []
    for s in lex["structures"]:
        try:
            padrao = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        achou = padrao.findall(texto)
        if achou:
            sinais.append({"nome": s["name"], "qtd": len(achou), "como": s["fix"]})
    tam = [len(f.split()) for f in FRASE_RE.findall(texto) if len(f.split()) > 2]
    if len(tam) >= 4:
        media = sum(tam) / len(tam)
        var = sum((n - media) ** 2 for n in tam) / len(tam)
        cv = (var ** 0.5) / media if media else 0
        if cv < 0.35:
            sinais.append({"nome": f"Frases do mesmo tamanho (variação {cv:.2f})", "qtd": len(tam),
                           "como": "Quebre uma frase ao meio. Deixe outra mais longa."})
    return sinais


def humanizar(texto, lex, manter_aspas=False):
    texto, guardados = proteger(texto)
    texto, inv = passada_invisiveis(texto, lex)
    texto, tipo, mantidos = passada_tipografia(texto, lex, manter_aspas)
    texto, trocas, sinais_lex = passada_lexico(texto, lex)
    texto = restaurar(texto, guardados)
    # Remove só linhas em branco no começo e espaços no fim; a indentação da 1ª linha fica.
    texto = re.sub(r"\A(?:[ \t]*\n)+", "", texto).rstrip() + "\n"
    return texto, {
        "invisiveis": inv,
        "tipografia": tipo,
        "mantidos": mantidos,
        "lexico": trocas,
        "palavras_sinalizadas": sinais_lex,
        "estruturas": varrer_estruturas(texto, lex),
    }


def relatorio(r, out=sys.stderr):
    def titulo(t):
        print(f"\n{t}\n" + "-" * len(t), file=out)

    total = sum(h["qtd"] for k in ("invisiveis", "tipografia", "lexico") for h in r[k])
    titulo("RELATÓRIO DO HUMANIZADOR")
    print(f"{total} marcas removidas; {len(r['palavras_sinalizadas'])} termos e "
          f"{len(r['estruturas'])} estruturas para reescrever à mão", file=out)
    if r["invisiveis"]:
        titulo("1. CARACTERES INVISÍVEIS")
        for h in r["invisiveis"]:
            print(f"  {h['qtd']:>3}x  {h['nome']}  -> {h['acao']}", file=out)
    if r["tipografia"] or r["mantidos"]:
        titulo("2. TIPOGRAFIA")
        for h in r["tipografia"]:
            print(f"  {h['qtd']:>3}x  {h['nome']}  -> {h['para']}", file=out)
        for h in r["mantidos"]:
            print(f"  {h['qtd']:>3}x  {h['nome']}  -> mantido", file=out)
    if r["lexico"]:
        titulo("3. MULETAS TROCADAS")
        for h in r["lexico"]:
            print(f"  {h['qtd']:>3}x  {h['termo']}  -> {h['por']}   [{h['familia']}]", file=out)
    if r["palavras_sinalizadas"]:
        titulo("4. TERMOS PARA REESCREVER  (não trocados automaticamente)")
        for h in r["palavras_sinalizadas"]:
            print(f"  {h['qtd']:>3}x  {h['termo']}   [{h['familia']}]", file=out)
    if r["estruturas"]:
        titulo("5. ESTRUTURAS PARA REESCREVER")
        for h in r["estruturas"]:
            print(f"  {h['qtd']:>3}x  {h['nome']}\n        {h['como']}", file=out)
    if not any(r.values()):
        titulo("LIMPO")
        print("  Nada a remover.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(
        description="Tira as marcas mecânicas de um texto em português. "
                    "Código de saída 0 quando roda; 2 em erro de uso.")
    ap.add_argument("entrada", nargs="?", default="-", help="arquivo de texto em UTF-8, ou - para a entrada padrão")
    ap.add_argument("-o", "--saida", help="grava o texto limpo neste arquivo")
    ap.add_argument("--relatorio", action="store_true", help="mostra o que mudou (stderr)")
    ap.add_argument("--json", action="store_true", help="emite {texto, relatorio} em JSON")
    ap.add_argument("--manter-aspas-curvas", action="store_true",
                    help="não troca aspas curvas por retas (use em texto formal, ABNT, documentos)")
    ap.add_argument("--lexico", default=LEX)
    a = ap.parse_args()

    configurar_utf8()
    bruto, crlf = ler_entrada(a.entrada)
    limpo, r = humanizar(bruto, carregar_lexico(a.lexico), a.manter_aspas_curvas)
    # Mantém o estilo de quebra de linha do original (CRLF no Windows, LF nos demais).
    saida_texto = limpo.replace("\n", "\r\n") if crlf else limpo

    if a.saida:
        try:
            with open(a.saida, "w", encoding="utf-8", newline="") as fh:
                fh.write(saida_texto)
        except OSError as e:
            erro(f"não foi possível gravar {a.saida}: {e}")
        print(f"gravado em {a.saida}", file=sys.stderr)
    if a.json:
        print(json.dumps({"texto": limpo, "relatorio": r}, indent=2, ensure_ascii=False))
        return
    if not a.saida:
        sys.stdout.write(saida_texto)
    if a.relatorio:
        relatorio(r)


if __name__ == "__main__":
    main()
