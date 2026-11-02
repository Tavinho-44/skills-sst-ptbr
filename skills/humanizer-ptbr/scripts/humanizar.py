#!/usr/bin/env python3
"""
humanizar.py - tira as marcas mecânicas de um texto em português.

Adaptado de humanize.py (linkedin-agent-skill, Jake Schincariol, licença MIT).

Três passadas, nesta ordem:

  1. INVISÍVEIS   apaga caracteres que um teclado não produz: espaços de
                  largura zero, word joiners, hífens suaves, BOM, caracteres
                  de tag Unicode, espaços não separáveis.
  2. TIPOGRAFIA   travessão -> vírgula, meia-risca -> hífen, aspas curvas ->
                  retas, reticências de um caractere -> três pontos.
  3. LÉXICO       troca ou apaga as muletas do lexico-ptbr.json. Entradas com
                  replace null são só SINALIZADAS (concordância e contexto
                  pedem reescrita manual).

URLs, e-mails e hashtags nunca são alterados. Siglas e NRs não estão no léxico.
Estruturas ("não é sobre X, é sobre Y", trincas, perguntas empilhadas) são
apontadas, nunca reescritas automaticamente.

Uso
  python3 humanizar.py rascunho.txt --relatorio
  python3 humanizar.py rascunho.txt -o limpo.txt --relatorio
  python3 humanizar.py rascunho.txt --json
"""

import argparse
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(AQUI, "lexico-ptbr.json")

PROTEGER_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+|#[\wÀ-ÿ]+")
FRASE_RE = re.compile(r"[^.!?\n]+[.!?]*")
MARCA = "\x01"  # posição onde uma muleta foi apagada


def carregar_lexico(caminho=LEX):
    with open(caminho, encoding="utf-8") as fh:
        return json.load(fh)


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
    return texto, achados


def passada_tipografia(texto, lex):
    achados = []
    for e in lex["typographic"]:
        ch = e["from"]
        n = texto.count(ch)
        if not n:
            continue
        achados.append({"nome": f"{ch} {e['name']}", "qtd": n, "para": e["to"].strip() or "(espaço)"})
        if ch == "—":
            texto = re.sub(r"\s*—\s*", ", ", texto)
        elif ch == "–":
            texto = re.sub(r"\s*–\s*(?=\d)", "-", texto)
            texto = re.sub(r"\s+–\s+", ", ", texto)
            texto = texto.replace("–", "-")
        else:
            texto = texto.replace(ch, e["to"])
    texto = re.sub(r",\s*([,.;:!?])", r"\1", texto)
    texto = re.sub(r",[ \t]*\n", "\n", texto)
    texto = re.sub(r"(?m)^[ \t]*,[ \t]*", "", texto)
    return texto, achados


def _mesma_caixa(origem, troca):
    if not troca:
        return troca
    if origem.isupper() and len(origem) > 1:
        return troca.upper()
    if origem[0].isupper():
        return troca[0].upper() + troca[1:]
    return troca


def _padrao(termo):
    return re.compile(r"\b" + re.escape(termo).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)


def passada_lexico(texto, lex):
    trocas, sinais = [], []
    entradas = sorted(lex["phrases"] + lex["words"], key=lambda e: len(e["find"]), reverse=True)
    for e in entradas:
        padrao = _padrao(e["find"])
        achou = padrao.findall(texto)
        if not achou:
            continue
        if e["replace"] is None:
            sinais.append({"termo": e["find"], "qtd": len(achou), "familia": e["family"]})
            continue
        trocas.append({"termo": e["find"], "por": e["replace"] or "(apagado)",
                       "qtd": len(achou), "familia": e["family"]})
        if e["replace"] == "":
            texto = padrao.sub(MARCA, texto)
        else:
            texto = padrao.sub(lambda m: _mesma_caixa(m.group(0), e["replace"]), texto)

    # Arrumação depois das remoções.
    texto = re.sub(MARCA + r"[ \t]*,?[ \t]*", MARCA, texto)
    # Início de frase onde a muleta foi apagada: capitaliza a palavra seguinte.
    texto = re.sub(r"(^|[.!?][ \t]+|\n[ \t]*)" + MARCA + r"+([a-zà-ÿ])",
                   lambda m: m.group(1) + m.group(2).upper(), texto)
    texto = texto.replace(MARCA, "")
    texto = re.sub(r"[ \t]{2,}", " ", texto)
    texto = re.sub(r"(?m)^[ \t]*([,.;:])[ \t]*", "", texto)
    texto = re.sub(r"[ \t]+([,.;:!?])", r"\1", texto)
    texto = re.sub(r"([.!?])[ \t]*,[ \t]*", r"\1 ", texto)
    texto = re.sub(r"(?m)^[ \t]+", "", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
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


def humanizar(texto, lex):
    texto, guardados = proteger(texto)
    texto, inv = passada_invisiveis(texto, lex)
    texto, tipo = passada_tipografia(texto, lex)
    texto, trocas, sinais_lex = passada_lexico(texto, lex)
    texto = restaurar(texto, guardados)
    return texto.strip() + "\n", {
        "invisiveis": inv,
        "tipografia": tipo,
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
    if r["tipografia"]:
        titulo("2. TIPOGRAFIA")
        for h in r["tipografia"]:
            print(f"  {h['qtd']:>3}x  {h['nome']}  -> {h['para']}", file=out)
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
    ap = argparse.ArgumentParser(description="Tira as marcas mecânicas de um texto em português.")
    ap.add_argument("entrada", nargs="?", default="-", help="arquivo, ou - para stdin")
    ap.add_argument("-o", "--saida", help="grava o texto limpo neste arquivo")
    ap.add_argument("--relatorio", action="store_true", help="mostra o que mudou (stderr)")
    ap.add_argument("--json", action="store_true", help="emite {texto, relatorio} em JSON")
    ap.add_argument("--lexico", default=LEX)
    a = ap.parse_args()

    bruto = sys.stdin.read() if a.entrada == "-" else open(a.entrada, encoding="utf-8").read()
    limpo, r = humanizar(bruto, carregar_lexico(a.lexico))

    if a.json:
        print(json.dumps({"texto": limpo, "relatorio": r}, indent=2, ensure_ascii=False))
        return
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as fh:
            fh.write(limpo)
        print(f"gravado em {a.saida}", file=sys.stderr)
    else:
        sys.stdout.write(limpo)
    if a.relatorio:
        relatorio(r)


if __name__ == "__main__":
    main()
