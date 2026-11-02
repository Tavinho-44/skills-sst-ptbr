# Mudanças

## Não lançado

### Adicionado
- `comum/`: regras compartilhadas pelas Skills (`regras-de-fonte.md` com a Regra A, `privacidade.md`, `glossario-sst.md`, `linkedin-regras.md`) e `uso.json`, que diz quais arquivos cada Skill recebe.
- `skills/<skill>/referencia/`: cópias de `comum/`, geradas por script. As Skills ainda não mandam ler esses arquivos; isso entra na próxima versão.
- `scripts/sincronizar_comum.py`: copia `comum/` para `referencia/` de cada Skill e confere se as cópias estão iguais.
- `scripts/validar.py`: confere frontmatter, links internos, cópias de `comum/`, ZIPs, dados proibidos (CPF, caminhos locais) e conteúdo da edição Premium; lista como aviso as pendências de conteúdo conhecidas.
- `scripts/empacotar.py`: gera os ZIPs de `pacotes/` (estrutura `<skill>/...`, fim de linha LF, sem `__pycache__`, mesmo conteúdo gera o mesmo ZIP).

### Alterado
- ZIPs de `pacotes/` regerados pelo script. O conteúdo dos arquivos existentes não mudou; entraram as cópias de `referencia/`.

## 1.0.0

- Primeira versão: 11 Skills de SST em português.
- Correções urgentes (PR #1): licenças MIT de terceiros, privacidade na investigação de acidente, bugs do humanizer, convite que não envia nada.
