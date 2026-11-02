"""Copia os arquivos de comum/ para referencia/ de cada Skill, conforme comum/uso.json.

Uso:
    python scripts/sincronizar_comum.py              copia e informa o que mudou
    python scripts/sincronizar_comum.py --conferir   só confere; sai com código 1 se houver divergência
    python scripts/sincronizar_comum.py --remover-orfaos
                                                     também apaga cópias de comum/ que não estão no uso.json

Só usa a biblioteca padrão do Python.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
COMUM = RAIZ / "comum"
SKILLS = RAIZ / "skills"
USO = COMUM / "uso.json"

# Primeira linha de conteúdo de todo arquivo de comum/. Serve para reconhecer cópias órfãs.
CABECALHO_COMUM = "> Arquivo comum às Skills SST-PTBR."


def ler_texto(caminho):
    """Lê como UTF-8 e normaliza o fim de linha, para comparar sem depender do core.autocrlf."""
    return caminho.read_bytes().decode("utf-8").replace("\r\n", "\n")


def carregar_uso():
    dados = json.loads(USO.read_text(encoding="utf-8"))
    return {skill: arquivos for skill, arquivos in dados.items() if not skill.startswith("_")}


def problemas_do_uso(uso):
    """Erros no próprio uso.json: Skill ou arquivo de comum/ que não existe."""
    erros = []
    for skill, arquivos in uso.items():
        if not (SKILLS / skill / "SKILL.md").is_file():
            erros.append(f"uso.json: a Skill '{skill}' não existe em skills/")
        for nome in arquivos:
            if not (COMUM / nome).is_file():
                erros.append(f"uso.json: '{nome}' (pedido por {skill}) não existe em comum/")
    return erros


def copias_orfas(uso):
    """Arquivos em referencia/ com o cabeçalho de comum/ que o uso.json não prevê."""
    orfas = []
    for referencia in sorted(SKILLS.glob("*/referencia")):
        previstos = set(uso.get(referencia.parent.name, []))
        for arquivo in sorted(referencia.glob("*.md")):
            if arquivo.name in previstos:
                continue
            if CABECALHO_COMUM in ler_texto(arquivo):
                orfas.append(arquivo)
    return orfas


def divergencias(uso):
    """Lista (skill, arquivo, motivo) das cópias ausentes ou diferentes de comum/."""
    saida = []
    for skill, arquivos in sorted(uso.items()):
        for nome in arquivos:
            origem = COMUM / nome
            destino = SKILLS / skill / "referencia" / nome
            if not origem.is_file():
                continue
            if not destino.is_file():
                saida.append((skill, nome, "ausente"))
            elif ler_texto(destino) != ler_texto(origem):
                saida.append((skill, nome, "diferente de comum/"))
    return saida


def main():
    parser = argparse.ArgumentParser(description="Sincroniza comum/ com referencia/ das Skills.")
    parser.add_argument("--conferir", action="store_true", help="não copia; só confere")
    parser.add_argument("--remover-orfaos", action="store_true", help="apaga cópias que não estão no uso.json")
    args = parser.parse_args()

    uso = carregar_uso()
    erros = problemas_do_uso(uso)
    if erros:
        for erro in erros:
            print(f"ERRO  {erro}")
        return 1

    pendentes = divergencias(uso)
    orfas = copias_orfas(uso)

    if args.conferir:
        for skill, nome, motivo in pendentes:
            print(f"ERRO  {skill}/referencia/{nome}: {motivo}")
        for arquivo in orfas:
            print(f"ERRO  {arquivo.relative_to(RAIZ).as_posix()}: cópia de comum/ fora do uso.json")
        if pendentes or orfas:
            print("Rode: python scripts/sincronizar_comum.py")
            return 1
        print("OK    referencia/ das Skills igual a comum/")
        return 0

    for skill, nome, motivo in pendentes:
        destino = SKILLS / skill / "referencia" / nome
        destino.parent.mkdir(exist_ok=True)
        shutil.copyfile(COMUM / nome, destino)
        print(f"COPIADO  {skill}/referencia/{nome} ({motivo})")

    for arquivo in orfas:
        caminho = arquivo.relative_to(RAIZ).as_posix()
        if args.remover_orfaos:
            arquivo.unlink()
            print(f"REMOVIDO {caminho}")
        else:
            print(f"AVISO    {caminho}: cópia de comum/ fora do uso.json (use --remover-orfaos)")

    if not pendentes:
        print("Nada a copiar: referencia/ já está igual a comum/")
    return 1 if orfas and not args.remover_orfaos else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
