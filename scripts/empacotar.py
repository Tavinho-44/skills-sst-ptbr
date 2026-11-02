"""Gera e confere os ZIPs das Skills em pacotes/ (um ZIP por Skill, estrutura <skill>/...).

Uso:
    python scripts/empacotar.py                       gera todos os ZIPs em pacotes/
    python scripts/empacotar.py humanizer-ptbr        gera só os ZIPs pedidos
    python scripts/empacotar.py --saida C:\\temp\\zips  grava em outra pasta
    python scripts/empacotar.py --conferir            não grava; sai com código 1 se algum ZIP
                                                      de pacotes/ estiver diferente do que seria gerado

Regras do pacote:
- arquivos de texto com fim de linha LF, mesmo que o Git tenha feito checkout em CRLF;
- nada de __pycache__, .pyc, .DS_Store, Thumbs.db ou arquivos .git*;
- data fixa nas entradas, para o mesmo conteúdo gerar sempre o mesmo ZIP.

Antes de gerar, confere se referencia/ está igual a comum/ (scripts/sincronizar_comum.py).
Só usa a biblioteca padrão do Python.
"""

import argparse
import io
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sincronizar_comum

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / "skills"
PACOTES = RAIZ / "pacotes"

EXTENSOES_TEXTO = {".md", ".txt", ".py", ".json", ".csv", ".yml", ".yaml", ".html", ".css", ".js"}
NOMES_EXCLUIDOS = {"__pycache__", ".DS_Store", "Thumbs.db", "desktop.ini"}
SUFIXOS_EXCLUIDOS = {".pyc", ".pyo"}
DATA_FIXA = (2026, 1, 1, 0, 0, 0)

# Barreira contra vazamento da edição Premium. O marcador é montado em partes
# para este arquivo não acusar a si mesmo.
MARCADOR_PREMIUM = "<!-- " + "sst-ptbr-premium" + " -->"
PASTAS_PREMIUM = {"checklists", "templates", "base-nrs"}


def excluido(caminho_relativo):
    for parte in caminho_relativo.parts:
        if parte in NOMES_EXCLUIDOS or parte.startswith(".git"):
            return True
    return caminho_relativo.suffix.lower() in SUFIXOS_EXCLUIDOS


def conteudo_para_zip(arquivo):
    dados = arquivo.read_bytes()
    if arquivo.suffix.lower() in EXTENSOES_TEXTO:
        dados = dados.replace(b"\r\n", b"\n")
    return dados


def entradas_da_skill(pasta_skill):
    """Lista ordenada de (nome no ZIP, bytes ou None para pasta)."""
    nome = pasta_skill.name
    entradas = [(f"{nome}/", None)]
    for caminho in sorted(pasta_skill.rglob("*"), key=lambda c: c.relative_to(pasta_skill).as_posix()):
        relativo = caminho.relative_to(pasta_skill)
        if excluido(relativo):
            continue
        destino = f"{nome}/{relativo.as_posix()}"
        if caminho.is_dir():
            entradas.append((destino + "/", None))
        else:
            entradas.append((destino, conteudo_para_zip(caminho)))
    return entradas


def gerar_zip(pasta_skill):
    """Devolve os bytes do ZIP da Skill."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for nome, dados in entradas_da_skill(pasta_skill):
            info = zipfile.ZipInfo(nome, date_time=DATA_FIXA)
            info.create_system = 3  # Unix, para as permissões abaixo valerem
            if dados is None:
                info.external_attr = (0o40755 << 16) | 0x10
                zf.writestr(info, b"")
            else:
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(info, dados)
    return buffer.getvalue()


def problemas_do_zip(dados_zip, nome_skill):
    """Confere um ZIP já gerado: estrutura, fim de linha e arquivos proibidos."""
    problemas = []
    with zipfile.ZipFile(io.BytesIO(dados_zip)) as zf:
        nomes = zf.namelist()
        if f"{nome_skill}/SKILL.md" not in nomes:
            problemas.append(f"falta {nome_skill}/SKILL.md")
        for nome in nomes:
            if not nome.startswith(f"{nome_skill}/"):
                problemas.append(f"'{nome}' fora da pasta {nome_skill}/")
            if "\\" in nome:
                problemas.append(f"'{nome}' usa barra invertida")
            if excluido(Path(nome)):
                problemas.append(f"'{nome}' não deveria estar no pacote")
            if set(Path(nome).parts) & PASTAS_PREMIUM:
                problemas.append(f"'{nome}' está numa pasta típica da edição Premium")
            if not nome.endswith("/") and Path(nome).suffix.lower() in EXTENSOES_TEXTO:
                conteudo = zf.read(nome)
                if b"\r\n" in conteudo:
                    problemas.append(f"'{nome}' tem fim de linha CRLF")
                if MARCADOR_PREMIUM.encode("utf-8") in conteudo:
                    problemas.append(f"'{nome}' tem o marcador da edição Premium")
    return problemas


def pastas_das_skills(nomes):
    todas = {p.name: p for p in sorted(SKILLS.iterdir()) if (p / "SKILL.md").is_file()}
    if not nomes:
        return list(todas.values()), []
    desconhecidas = [n for n in nomes if n not in todas]
    return [todas[n] for n in nomes if n in todas], desconhecidas


def main():
    parser = argparse.ArgumentParser(description="Gera e confere os ZIPs das Skills.")
    parser.add_argument("skills", nargs="*", help="nomes das Skills (padrão: todas)")
    parser.add_argument("--saida", type=Path, default=PACOTES, help="pasta dos ZIPs (padrão: pacotes/)")
    parser.add_argument("--conferir", action="store_true", help="não grava; compara com os ZIPs existentes")
    args = parser.parse_args()

    pastas, desconhecidas = pastas_das_skills(args.skills)
    for nome in desconhecidas:
        print(f"ERRO  Skill '{nome}' não encontrada em skills/")
    if desconhecidas:
        return 1

    uso = sincronizar_comum.carregar_uso()
    pendentes = sincronizar_comum.divergencias(uso)
    if pendentes:
        for skill, nome, motivo in pendentes:
            print(f"ERRO  {skill}/referencia/{nome}: {motivo}")
        print("Rode antes: python scripts/sincronizar_comum.py")
        return 1

    falhas = 0
    for pasta in pastas:
        dados = gerar_zip(pasta)
        problemas = problemas_do_zip(dados, pasta.name)
        if problemas:
            falhas += 1
            for problema in problemas:
                print(f"ERRO  {pasta.name}.zip: {problema}")
            continue
        destino = args.saida / f"{pasta.name}.zip"
        if args.conferir:
            if not destino.is_file():
                falhas += 1
                print(f"ERRO  {destino.name}: não existe em {args.saida}")
            elif destino.read_bytes() != dados:
                falhas += 1
                print(f"ERRO  {destino.name}: desatualizado (rode python scripts/empacotar.py)")
            else:
                print(f"OK    {destino.name}")
            continue
        args.saida.mkdir(parents=True, exist_ok=True)
        anterior = destino.read_bytes() if destino.is_file() else None
        if anterior == dados:
            print(f"IGUAL {destino.name}")
        else:
            destino.write_bytes(dados)
            with zipfile.ZipFile(io.BytesIO(dados)) as zf:
                arquivos = [n for n in zf.namelist() if not n.endswith("/")]
            print(f"GERADO {destino.name}: {len(arquivos)} arquivo(s), {len(dados)} bytes")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
