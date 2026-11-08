"""Valida o repositório público skills-sst-ptbr.

Uso:
    python scripts/validar.py                 mostra erros e avisos; sai com código 1 se houver erro
    python scripts/validar.py --estrito       também sai com código 1 se houver aviso
    python scripts/validar.py --sem-pacotes   não confere os ZIPs de pacotes/

ERRO  quebra a instalação, vaza conteúdo pago ou expõe dado pessoal. Precisa ser corrigido antes do PR.
AVISO pendência de conteúdo conhecida (dependência inexistente, nome de ferramenta, data fixa,
      Regra A ainda não aplicada). Lista o que falta corrigir nas Skills.

Só usa a biblioteca padrão do Python.
"""

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import empacotar
import sincronizar_comum

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / "skills"
COMUM = RAIZ / "comum"
PACOTES = RAIZ / "pacotes"

MARCADOR_PREMIUM = empacotar.MARCADOR_PREMIUM
PASTAS_PREMIUM = empacotar.PASTAS_PREMIUM

EXTENSOES_TEXTO = empacotar.EXTENSOES_TEXTO
IGNORAR_NA_VARREDURA = {".git", "__pycache__"}

# Dados que não podem aparecer em skills/, comum/ nem nos textos da raiz.
DADOS_PROIBIDOS = [
    (re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"), "número no formato de CPF"),
    (re.compile(r"[A-Za-z]:\\Users\\", re.IGNORECASE), "caminho local do Windows (C:\\Users\\...)"),
    (re.compile(r"(?<![\w.])/(?:Users|home)/[A-Za-z0-9_.-]+/"), "caminho local de usuário (/Users/ ou /home/)"),
    (re.compile(r"\bCCR\b"), "nome de empresa do autor (CCR)"),
    (re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"), "número no formato de CNPJ"),
    (re.compile(r"\(?\b[1-9]{2}\)?[ .-]?9[ .]?\d{4}[ .-]?\d{4}\b"), "número no formato de celular"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@(?!example\.|exemplo\.|users\.noreply\.)[A-Za-z0-9-]+\.[A-Za-z.]{2,}\b"),
     "endereço de e-mail"),
]

# Pendências de conteúdo apontadas na auditoria da Fase 2.
PADROES_AVISO = [
    (re.compile(r"\bWeb(?:Search|Fetch)\b"), "nome de ferramenta do Claude Code; no app a busca tem outro nome ou está desligada"),
    (re.compile(r"\bsua skill de\b", re.IGNORECASE), "depende de skill do usuário que não está no repositório"),
    (re.compile(r"\bskill de perfil\b", re.IGNORECASE), "depende de skill que não está no repositório"),
    (re.compile(r"br-eli-mcp"), "depende de servidor MCP externo; tratar como opcional"),
    (re.compile(r"\bkits? de CIPA\b", re.IGNORECASE), "convenção pessoal do autor (kits de CIPA)"),
    (re.compile(r"\bcampos em amarelo\b", re.IGNORECASE), "convenção pessoal do autor (campos em amarelo)"),
    (re.compile(r"\bcabeçalho padrão\b", re.IGNORECASE), "convenção pessoal do autor (cabeçalho padrão)"),
    (re.compile(r"\batos? (?:e condições )?insegur[oa]s?\b|\bcondi(?:ção|ções) insegura", re.IGNORECASE),
     "vocabulário de culpa; ver comum/glossario-sst.md"),
]
DATA_FIXA = re.compile(
    r"\b\d{2}/\d{2}/\d{4}\b"
    r"|\b(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro) de \d{4}\b",
    re.IGNORECASE,
)
CITA_NORMA = re.compile(r"\bNR-?\s?\d{1,2}\b|\bLei\s+(?:n[º°.]?\s*)?\d|\bPortaria\b|\bDecreto\b")
NOME_VALIDO = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_MD = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CAMINHO_EM_CRASE = re.compile(r"`((?:referencia|scripts|exemplos)/[^`\s]+)`")
SKILL_EM_CRASE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")


class Relatorio:
    def __init__(self):
        self.erros = []
        self.avisos = []

    def erro(self, onde, msg):
        self.erros.append(f"{onde}: {msg}")

    def aviso(self, onde, msg):
        self.avisos.append(f"{onde}: {msg}")


def rel(caminho):
    return caminho.relative_to(RAIZ).as_posix()


def ler(caminho):
    return caminho.read_bytes().decode("utf-8").replace("\r\n", "\n")


def eh_copia_comum(texto):
    return sincronizar_comum.CABECALHO_COMUM in texto


def ler_frontmatter(texto):
    """Lê o frontmatter simples (chave: valor) entre as duas primeiras linhas '---'."""
    linhas = texto.split("\n")
    if not linhas or linhas[0].strip() != "---":
        return None
    campos = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            return campos
        if ":" not in linha or linha.startswith((" ", "\t")):
            continue
        chave, valor = linha.split(":", 1)
        valor = valor.strip()
        if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
            valor = valor[1:-1].replace('\\"', '"')
        campos[chave.strip()] = valor
    return None


def validar_frontmatter(pasta, texto, r):
    onde = rel(pasta / "SKILL.md")
    campos = ler_frontmatter(texto)
    if campos is None:
        r.erro(onde, "frontmatter ausente ou sem a linha '---' de fechamento")
        return
    nome = campos.get("name", "")
    descricao = campos.get("description", "")
    if not nome:
        r.erro(onde, "campo 'name' ausente")
    elif nome != pasta.name:
        r.erro(onde, f"'name' ({nome}) diferente do nome da pasta ({pasta.name})")
    elif not NOME_VALIDO.match(nome) or len(nome) > 64:
        r.erro(onde, "'name' deve ter até 64 caracteres: minúsculas, números e hífens")
    elif "anthropic" in nome or "claude" in nome:
        r.erro(onde, "'name' não pode conter 'anthropic' nem 'claude'")
    if not descricao:
        r.erro(onde, "campo 'description' ausente ou vazio")
    elif len(descricao) > 1024:
        r.erro(onde, f"'description' com {len(descricao)} caracteres (máximo 1024)")
    elif re.search(r"<[A-Za-z/][^>]*>", descricao):
        r.erro(onde, "'description' não pode ter tags XML/HTML")


def validar_links(pasta, arquivo, texto, r):
    onde = rel(arquivo)
    alvos = [(m, "link") for m in LINK_MD.findall(texto)]
    if arquivo.name == "SKILL.md":
        alvos += [(m, "caminho") for m in CAMINHO_EM_CRASE.findall(texto)]
    for alvo, tipo in alvos:
        if re.match(r"^[a-z]+:", alvo) or alvo.startswith("#"):
            continue
        alvo_limpo = alvo.split("#", 1)[0]
        base = pasta if tipo == "caminho" else arquivo.parent
        destino = (base / alvo_limpo).resolve()
        if not destino.is_relative_to(pasta.resolve()):
            r.erro(onde, f"'{alvo}' aponta para fora da pasta da Skill; a Skill instalada não enxerga esse arquivo")
        elif not destino.exists():
            r.erro(onde, f"'{alvo}' não existe")


def validar_conteudo(pasta, nomes_skills, uso, r):
    skill_md = pasta / "SKILL.md"
    texto_skill = ler(skill_md)
    validar_frontmatter(pasta, texto_skill, r)

    if texto_skill.count("\n") > 500:
        r.aviso(rel(skill_md), "mais de 500 linhas; mover detalhes para referencia/")

    for arquivo in sorted(pasta.rglob("*.md")):
        texto = ler(arquivo)
        validar_links(pasta, arquivo, texto, r)
        if eh_copia_comum(texto):
            continue
        onde = rel(arquivo)
        for numero, linha in enumerate(texto.split("\n"), start=1):
            for padrao, msg in PADROES_AVISO:
                if padrao.search(linha):
                    r.aviso(f"{onde}:{numero}", msg)
            for data in DATA_FIXA.findall(linha):
                r.aviso(f"{onde}:{numero}", f"data fixa {data}; orientar a conferir a vigência ou tirar do texto")
            if "skill" in linha.lower():
                for nome in SKILL_EM_CRASE.findall(linha):
                    if nome not in nomes_skills and re.search(r"(?<![\w-])skills?(?![\w-])", linha, re.IGNORECASE):
                        r.aviso(f"{onde}:{numero}", f"menciona `{nome}`, que não é Skill deste repositório")

    if CITA_NORMA.search(texto_skill) and "regras-de-fonte.md" not in texto_skill:
        r.aviso(rel(skill_md), "cita norma, mas não aplica a Regra A (referencia/regras-de-fonte.md)")
    for nome in uso.get(pasta.name, []):
        if nome not in texto_skill:
            r.aviso(rel(skill_md), f"recebe referencia/{nome}, mas o SKILL.md ainda não manda ler")


def validar_dados_proibidos(r):
    alvos = [RAIZ / "README.md", RAIZ / "CREDITOS.md", RAIZ / "CHANGELOG.md"]
    for pasta in (SKILLS, COMUM):
        alvos += [p for p in sorted(pasta.rglob("*")) if p.is_file() and p.suffix.lower() in EXTENSOES_TEXTO]
    for arquivo in alvos:
        if not arquivo.is_file() or "__pycache__" in arquivo.parts:
            continue
        for numero, linha in enumerate(ler(arquivo).split("\n"), start=1):
            for padrao, msg in DADOS_PROIBIDOS:
                if padrao.search(linha):
                    r.erro(f"{rel(arquivo)}:{numero}", msg)


def validar_barreira_premium(r):
    """Nada da edição Premium pode entrar no repositório público."""
    for caminho in sorted(RAIZ.rglob("*")):
        partes = caminho.relative_to(RAIZ).parts
        if any(p in IGNORAR_NA_VARREDURA for p in partes):
            continue
        if caminho.is_dir():
            if caminho.name in PASTAS_PREMIUM:
                r.erro(rel(caminho), "pasta típica da edição Premium no repositório público")
            continue
        sufixo = caminho.suffix.lower()
        if sufixo in EXTENSOES_TEXTO:
            if MARCADOR_PREMIUM in ler(caminho):
                r.erro(rel(caminho), "arquivo com o marcador da edição Premium")
        elif sufixo == ".zip":
            with zipfile.ZipFile(caminho) as zf:
                for nome in zf.namelist():
                    if set(Path(nome).parts) & PASTAS_PREMIUM:
                        r.erro(f"{rel(caminho)}!{nome}", "pasta típica da edição Premium dentro do ZIP")
                    elif Path(nome).suffix.lower() in EXTENSOES_TEXTO:
                        if MARCADOR_PREMIUM.encode("utf-8") in zf.read(nome):
                            r.erro(f"{rel(caminho)}!{nome}", "arquivo com o marcador da edição Premium")


def validar_readme(nomes_skills, r):
    readme = RAIZ / "README.md"
    texto = ler(readme)
    for alvo in LINK_MD.findall(texto):
        if re.match(r"^[a-z]+:", alvo) or alvo.startswith("#"):
            continue
        if not (RAIZ / alvo.split("#", 1)[0]).exists():
            r.erro("README.md", f"link '{alvo}' não existe")
    for nome in sorted(nomes_skills):
        if f"skills/{nome}/SKILL.md" not in texto:
            r.aviso("README.md", f"Skill '{nome}' não aparece na lista do README")


def validar_pacotes(nomes_skills, r):
    for nome in sorted(nomes_skills):
        zip_atual = PACOTES / f"{nome}.zip"
        if not zip_atual.is_file():
            r.erro(rel(zip_atual), "ZIP ausente (rode python scripts/empacotar.py)")
            continue
        esperado = empacotar.gerar_zip(SKILLS / nome)
        if not empacotar.mesmo_conteudo(zip_atual.read_bytes(), esperado):
            r.erro(rel(zip_atual), "ZIP diferente da pasta da Skill (rode python scripts/empacotar.py)")
        for problema in empacotar.problemas_do_zip(zip_atual.read_bytes(), nome):
            r.erro(rel(zip_atual), problema)
    for zip_extra in sorted(PACOTES.glob("*.zip")):
        if zip_extra.stem not in nomes_skills:
            r.erro(rel(zip_extra), "ZIP sem Skill correspondente em skills/")


def main():
    parser = argparse.ArgumentParser(description="Valida o repositório público skills-sst-ptbr.")
    parser.add_argument("--estrito", action="store_true", help="avisos também reprovam")
    parser.add_argument("--sem-pacotes", action="store_true", help="não confere os ZIPs de pacotes/")
    args = parser.parse_args()

    r = Relatorio()
    pastas = [p for p in sorted(SKILLS.iterdir()) if p.is_dir()]
    for pasta in pastas:
        if not (pasta / "SKILL.md").is_file():
            r.erro(rel(pasta), "pasta de Skill sem SKILL.md")
    pastas = [p for p in pastas if (p / "SKILL.md").is_file()]
    nomes_skills = {p.name for p in pastas}

    uso = sincronizar_comum.carregar_uso()
    for erro in sincronizar_comum.problemas_do_uso(uso):
        r.erro("comum/uso.json", erro.split(": ", 1)[1])
    for skill, nome, motivo in sincronizar_comum.divergencias(uso):
        r.erro(f"skills/{skill}/referencia/{nome}", f"{motivo} (rode python scripts/sincronizar_comum.py)")
    for orfa in sincronizar_comum.copias_orfas(uso):
        r.erro(rel(orfa), "cópia de comum/ fora do uso.json")
    usados = {n for arquivos in uso.values() for n in arquivos}
    for arquivo in sorted(COMUM.glob("*.md")):
        if arquivo.name not in usados:
            r.aviso(rel(arquivo), "nenhuma Skill recebe este arquivo (ver comum/uso.json)")

    for pasta in pastas:
        validar_conteudo(pasta, nomes_skills, uso, r)
    validar_dados_proibidos(r)
    validar_barreira_premium(r)
    validar_readme(nomes_skills, r)
    if not args.sem_pacotes:
        validar_pacotes(nomes_skills, r)

    for linha in r.erros:
        print(f"ERRO  {linha}")
    for linha in r.avisos:
        print(f"AVISO {linha}")
    print(f"\n{len(pastas)} Skill(s) · {len(r.erros)} erro(s) · {len(r.avisos)} aviso(s)")
    if r.erros or (args.estrito and r.avisos):
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
