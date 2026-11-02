---
name: "conferencia-documento-sst"
description: "Confere as citações (NR, item, portaria, lei) de um documento de SST na base de normas e faz revisão adversarial como fiscal e perito. Use no fim de PGR, laudo, OS, investigação ou ao pedir \"confere as citações\"."
---

# Conferência de documento de SST

Duas leituras de um documento pronto, sempre nesta ordem:

- **A. Conferente de citações:** cada NR, item, portaria, lei ou NBR citada existe, diz o que o documento afirma e está vigente?
- **B. Revisor adversário:** onde um fiscal, um perito ou quem executa em campo derrubaria o documento?

Serve para PGR, PCMSO, laudos (LTCAT, insalubridade, periculosidade), ordens de serviço, procedimentos, relatórios de investigação de acidente e documentos dos kits de CIPA e brigada. Para post, carrossel ou legenda de LinkedIn, use a `revisao-tecnica-post-sst`.

Método adaptado dos agentes `conferente-de-citacoes` e `revisor-adversario` do repositório jcbarbalho/claude-skills-advocacia-br (Apache-2.0).

## Regras que valem para as duas leituras

- **Só leitura.** Não editar o documento nem a base de normas. Quem decide e reescreve é o usuário.
- **Nunca completar de memória.** Item, redação, número de portaria ou data que não foi conferido sai como `❓ não conferido` ou `[VERIFICAR]`, com o motivo.
- **Base local primeiro, web depois.** Se o usuário tiver uma base de normas própria (por exemplo, um vault do Obsidian com NRs, portarias e leis em Markdown), conferir nela, buscando o item exato sem ler a norma inteira. Sem base local, usar as fontes oficiais (gov.br/trabalho-e-emprego, planalto.gov.br, in.gov.br) e anotar a data da consulta.
- **Privacidade:** se o documento trouxer nome, CPF, matrícula ou dado de saúde individual de trabalhador, isso é achado (🟠). Não repetir esses dados na resposta.

## Entrada

- O documento (.docx, .pdf ou texto colado). Em .docx, numerar os parágrafos como `[i]` e usar esse número em todos os achados.
- A **data de referência**: data do documento, do fato investigado ou da avaliação. É ela que decide qual redação vale. Se não estiver clara, perguntar ou usar a data do documento e avisar.
- O tipo de documento e a empresa ou atividade, se não estiverem óbvios.

No Claude Code, rodar A e B como dois subagentes separados, que leem só o documento e não a conversa, para a leitura ser a frio de verdade. No app, fazer em duas passadas separadas e, na B, julgar só o que está escrito no documento, sem considerar o que foi conversado sobre ele.

## A. Conferente de citações

1. **Levantar** todas as citações com o parágrafo `[i]`: NR com item (inclusive alínea e subitem), anexo de NR, portaria do MTE, lei, decreto, CLT, convenção da OIT, NBR/ISO, instrução normativa, norma interna. Remissão sem norma identificada ("conforme item 4.2"): a norma é a do contexto. Se for ambígua, apontar.
2. **Conferir no texto oficial** (base local ou site oficial), buscando o item exato (`35.4.1`) e lendo só o trecho em volta:
   - **Existe?** Inclusive o subitem e a alínea. Erro comum: subitem certo no item errado.
   - **Diz o que o documento afirma?** Comparar o conteúdo, não só o número. Citação entre aspas: conferir palavra por palavra.
   - **Vigência na data de referência:** ver as marcas de vigência do texto ("redação dada pela Portaria...") e a lista de portarias que alteraram a NR. Redação posterior à data de referência aplicada a fato anterior é ⚠️. Item revogado é 🔴.
   - **NR-10:** a redação atual vale até 31/05/2027 e a nova a partir de 01/06/2027. Conferir se o documento cita a versão certa para a data de referência.
   - Informar a data em que o texto usado foi baixado ou consultado.
3. **Fora das NRs:** lei, decreto ou CLT na base local, se houver. Senão: usar o servidor `br-eli-mcp` (se estiver instalado no Claude Code) ou a página oficial do Planalto pela web. Sem conseguir, `❓`.
4. **NBR e ISO:** o texto é pago e a base local em geral só tem resumos. Confirmar que a norma existe e qual é a edição vigente; o conteúdo de um item só é ✅ se o texto estiver disponível. Caso contrário, `❓ conteúdo não conferido`.
5. Manual, guia ou nota técnica citado como se fosse obrigação legal é 🟠, porque é interpretação, não norma.

Devolver uma tabela na ordem do documento:

| [§] | Citação | Status | Nota (correção concreta) |
|---|---|---|---|

Status: ✅ confere · ⚠️ redação mudou ou versão errada para a data · 🟠 não diz exatamente isso, ou interpretação citada como norma · 🔴 inexistente, revogado ou contrário · ❓ não conferido.

Antes da tabela, em até 5 linhas: o total de citações, quantas de cada status e os 🔴 e 🟠 primeiro, cada um com a correção (item certo, redação vigente, norma que de fato diz aquilo, se achou).

## B. Revisor adversário

Ler o documento como quem quer achar o furo. Se estiver sólido, dizer em uma linha e parar: não inventar defeito para parecer útil, e não elogiar por elogiar.

Quatro lentes:

1. **Auditor-Fiscal do Trabalho.** O documento tem os elementos mínimos que a NR aplicável exige para esse tipo de documento? Ler esses requisitos no texto da NR; não presumir de memória. Responsável técnico, assinatura, datas, periodicidade e revisão estão presentes? Há medida de controle sem prazo ou sem responsável? A hierarquia de controle foi respeitada (EPI apresentado como primeira medida é achado)?
2. **Perito ou advogado do trabalhador** (ação trabalhista, acidente, insalubridade ou periculosidade). Onde o documento se contradiz (datas, funções, setores, agentes, valores medidos e limites)? Que evidência falta para sustentar o que afirma (lista de presença, ficha de EPI com CA válido, medição com equipamento calibrado, ordem de serviço assinada)? A conclusão decorre do que foi levantado? Na investigação de acidente: a causa raiz culpa só o trabalhador sem analisar organização e gestão?
3. **Quem executa em campo** (encarregado, eletricista, operador). As medidas são concretas e aplicáveis na atividade real? Há instrução vaga ("tomar cuidado", "usar EPI adequado") onde precisaria dizer qual EPI, qual bloqueio, qual sequência?
4. **Acabamento e padrão.** Campos em amarelo ainda não preenchidos, cabeçalho padrão da empresa, numeração e versões, ABNT em documento formal, dado pessoal de trabalhador. É 🟡, salvo quando muda o sentido ou a validade do documento.

No máximo 12 achados, em ordem de gravidade:

- 🔴 **Derruba:** autuação provável, documento inválido, conclusão sem base, requisito obrigatório ausente.
- 🟠 **Enfraquece:** contradição, evidência que falta, medida inaplicável, citação frágil.
- 🟡 **Acabamento:** só o que um fiscal ou perito notaria.

Cada achado: `[parágrafo]` · o problema em uma frase · por quê (item conferido no texto da norma ou trecho do documento) · a correção em uma linha. Separar **fato** (está no documento ou na norma) de **inferência** sua. Não reescrever parágrafos inteiros.

## Fechamento

- Uma linha com o que **não** foi conferido: NBR sem texto disponível, lei sem acesso ao texto, anexo que não veio, data de referência presumida.
- Oferecer, em uma linha, aplicar as correções no documento. Só com aprovação, e pela skill que gerou o documento, se houver (ex.: `investigacao-acidente-trabalho`).
- Se a conferência mostrar erro que veio de uma skill ou de um modelo do usuário (modelo com item errado, por exemplo), apontar para corrigir a origem.

## Idioma

Português do Brasil.