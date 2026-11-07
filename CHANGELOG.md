# Mudanças

## Não lançado

### Adicionado
- `.github/workflows/validar.yml`: o GitHub roda a validação e o gitleaks (segredos no histórico) a cada envio e pull request; selo no README.
- `scripts/validar.py`: dados proibidos agora incluem CNPJ, celular e e-mail.
- README: aviso para instalar só do repositório oficial e seção de manutenção.
- `comum/`: regras compartilhadas pelas Skills (`regras-de-fonte.md` com a Regra A, `privacidade.md`, `glossario-sst.md`, `linkedin-regras.md`) e `uso.json`, que diz quais arquivos cada Skill recebe.
- `skills/<skill>/referencia/`: cópias de `comum/`, geradas por script. As Skills ainda não mandam ler esses arquivos; isso entra na próxima versão.
- `scripts/sincronizar_comum.py`: copia `comum/` para `referencia/` de cada Skill e confere se as cópias estão iguais.
- `scripts/validar.py`: confere frontmatter, links internos, cópias de `comum/`, ZIPs, dados proibidos (CPF, caminhos locais) e conteúdo da edição Premium; lista como aviso as pendências de conteúdo conhecidas.
- `scripts/empacotar.py`: gera os ZIPs de `pacotes/` (estrutura `<skill>/...`, fim de linha LF, sem `__pycache__`, mesmo conteúdo gera o mesmo ZIP).

### Alterado
- `scripts/empacotar.py` e `scripts/validar.py`: a conferência dos ZIPs compara o conteúdo (nomes, permissões e arquivos), não os bytes comprimidos. Antes, Python de versões ou sistemas diferentes acusava os 11 ZIPs como desatualizados mesmo com o conteúdo igual, e a checagem no GitHub reprovaria sempre.
- ZIPs de `pacotes/` regerados pelo script.
- As 11 Skills (Fase 5, correções da auditoria):
  - **Regras comuns:** seguem a Regra A, com a marca de origem ✅/🌐/⚠️ e a data, e mandam ler as cópias de `referencia/`.
  - **Dependências:** saíram as de Skills e ferramentas que não estão no repositório, e os nomes de ferramenta do Claude Code.
  - **Datas:** saíram as datas fixas que envelhecem.
  - **Exemplos:** marcados como ilustrativos, sem números ou vivências inventados.
- `investigacao-acidente-trabalho`:
  - pendências entram como "não informado" ou "a apurar";
  - rótulo fato, evidência ou hipótese em cada porquê;
  - sem vocabulário de culpa;
  - bloco de responsável técnico e aviso de rascunho;
  - seções de evidências, medidas imediatas e limitações.
- `conferencia-documento-sst`: ⚠️ volta a significar "não conferido", e o resultado da conferência vai numa coluna própria.
- `humanizer-ptbr`:
  - **Preservação do texto:** não mexe em vírgula após "etc.", em indentação, em sigla ou unidade (kV, dB(A), pH), em emoji composto nem em citação entre aspas, mesmo quando ela quebra a linha.
  - **Trocas só sinalizadas:** "utilizado" e "no cenário atual".
  - **Travessão:** um por texto é mantido, e entre números vira hífen.
  - **Windows:** lê e grava em UTF-8.
  - **Códigos de saída:** 0 quando roda e 2 em erro de uso.
- `carreira-ops-tst`: recebe `privacidade.md`.
- `investigacao-acidente-trabalho`: etapa de hipóteses concorrentes antes de fechar as causas (2 a 4 hipóteses, ao menos uma de método ou gestão, cada uma sustentada, descartada ou em aberto); resumo em Causas básicas e as em aberto em Limitações.
- `conferencia-documento-sst`: a resposta abre com veredito (APTO, APTO COM RESSALVAS, NÃO APTO ou SEM VEREDITO) e uma linha por etapa.
- CREDITOS: ideias adaptadas do affaan-m/ECC (MIT).

## 1.0.0

- Primeira versão: 11 Skills de SST em português.
- Correções urgentes (PR #1): licenças MIT de terceiros, privacidade na investigação de acidente, bugs do humanizer, convite que não envia nada.
