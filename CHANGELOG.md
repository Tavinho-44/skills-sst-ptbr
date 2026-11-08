# Mudanças

## Não lançado

### Adicionado
- `comum/`: regras compartilhadas pelas Skills (`regras-de-fonte.md` com a Regra A, `privacidade.md`, `glossario-sst.md`, `linkedin-regras.md`) e `uso.json`, que diz quais arquivos cada Skill recebe.
- `skills/<skill>/referencia/`: cópias de `comum/`, geradas por script. As Skills ainda não mandam ler esses arquivos; isso entra na próxima versão.
- `scripts/sincronizar_comum.py`: copia `comum/` para `referencia/` de cada Skill e confere se as cópias estão iguais.
- `scripts/validar.py`: confere frontmatter, links internos, cópias de `comum/`, ZIPs, dados proibidos (CPF, caminhos locais) e conteúdo da edição Premium; lista como aviso as pendências de conteúdo conhecidas.
- `scripts/empacotar.py`: gera os ZIPs de `pacotes/` (estrutura `<skill>/...`, fim de linha LF, sem `__pycache__`, mesmo conteúdo gera o mesmo ZIP).

### Alterado
- Fase 6, correções a partir dos testes (07 e 08/11/2026):
  - **Todas as Skills com `referencia/`:** mandam abrir os arquivos pelo caminho, sem depender de busca por arquivos (a pasta da Skill pode estar oculta).
  - **`comum/regras-de-fonte.md`:** a marca de origem é da conferência feita na conversa; marca copiada de arquivo da Skill ou do documento analisado, ou arquivo achado por busca e não indicado pelo usuário, não vale.
  - **`revisao-tecnica-post-sst`:** a hierarquia de controles segue a ordem de prioridade da NR-01, item 1.4.1, alínea g; a escala de cinco degraus é boa prática.
  - **`consulta-normas-sst`:** pedido de resposta "de cabeça" ou pronta para cliente não autoriza texto com item, prazo ou carga horária sem conferência.
  - **`conferencia-documento-sst`:** data do documento já passada não é falha.
  - **`humanizer-ptbr`:** verbo e termo técnico ficam como estão; nada de fato novo; a lista de mudanças só descreve o que mudou.
  - **`convite-conexao-linkedin`:** usa as palavras do usuário sobre a experiência; não diz que ele acompanha a pessoa sem ele ter dito.
  - **`comentarios-linkedin-sst`:** comentário ⚠️ não é "o que eu postaria"; não atribui ao usuário conhecimento da norma.
  - **`respostas-comentarios-linkedin`:** não promete ação pelo usuário; não confirma causa de acidente em público.
  - **`carreira-ops-tst`:** no máximo 3 perguntas, sem procurar arquivo no computador; status "avaliada" só após avaliar.
  - **`calendario-editorial-sst`:** data informada pelo usuário sem fonte fica ⚠️ até ele passar a lei ou o link.
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

## 1.0.0

- Primeira versão: 11 Skills de SST em português.
- Correções urgentes (PR #1): licenças MIT de terceiros, privacidade na investigação de acidente, bugs do humanizer, convite que não envia nada.
