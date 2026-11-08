---
name: "conferencia-documento-sst"
description: "Confere as citações de norma (NR, item, portaria, lei) de um documento de SST na data de referência e faz revisão adversarial como fiscal e perito. Use no fim de PGR, PCMSO, laudo, ordem de serviço, procedimento ou relatório de investigação, ou quando pedirem \"confere as citações\", \"revisa como um fiscal\" ou \"onde esse documento cai?\". Não serve para post, carrossel ou legenda de LinkedIn. Não substitui o responsável técnico."
---

# Conferência de documento de SST

Duas leituras de um documento pronto, sempre nesta ordem:

- **A. Conferente de citações:** cada NR, item, portaria, lei ou NBR citada existe, diz o que o documento afirma e está vigente na data de referência?
- **B. Revisor adversário:** onde um fiscal, um perito ou quem executa em campo derrubaria o documento?

Serve para PGR, PCMSO, laudos (LTCAT, insalubridade, periculosidade), ordens de serviço, procedimentos, relatórios de investigação de acidente e outros documentos de SST. Para post, carrossel ou legenda de LinkedIn, use a `revisao-tecnica-post-sst`, se estiver instalada; sem ela, esta conferência vale para as citações do texto, mas não para o tom e o formato de rede social.

Método adaptado dos agentes `conferente-de-citacoes` e `revisor-adversario` do repositório jcbarbalho/claude-skills-advocacia-br (Apache-2.0).

**Aviso que vai em toda resposta:** esta conferência apoia o responsável técnico e não o substitui. A decisão, a assinatura e a responsabilidade pelo documento continuam com o profissional legalmente habilitado que o assina.

Os arquivos de `referencia/` ficam na pasta desta Skill. Abra cada um pelo caminho, com a ferramenta de leitura, sem depender de busca por arquivos: a pasta da Skill pode estar oculta e não aparecer na busca.

## Regras que valem para as duas leituras

- **Fonte e vigência:** siga `referencia/regras-de-fonte.md` (Regra A) em toda conferência. Cada citação leva a origem ✅ Base local, 🌐 Fonte oficial ou ⚠️ Não conferido, com a data. A ordem de busca é base local do usuário, depois fonte oficial na web (se a busca na web estiver disponível nesta conversa); sem nenhuma das duas, **não complete de memória**: peça ao usuário o trecho da norma ou o PDF e deixe ⚠️.
- **Só leitura.** Não editar o documento nem a base de normas. Quem decide e reescreve é o usuário.
- **Privacidade:** siga `referencia/privacidade.md`. Se o documento trouxer nome, CPF, matrícula ou dado de saúde individual de trabalhador, isso é achado (🟠). Ao citar um trecho do documento na resposta, mascare esses dados (`[nome do trabalhador]`, `[matrícula]`) e identifique a pessoa por função e setor. Nunca repita o valor.
- **Não reproduzir NBR/ISO.** O texto é protegido e pago: cite só número, título e edição, e não copie trecho, tabela ou figura, nem do documento nem de memória.
- **Obrigação x boa prática x interpretação:** em cada achado, diga se o requisito é obrigação legal (está no texto de norma conferido), boa prática (manual, guia, norma técnica voluntária) ou sua interpretação. Nunca trate boa prática como exigência da NR (Regra A, seção 6). Os termos seguem `referencia/glossario-sst.md`.

## Entrada

- O documento (.docx, .pdf ou texto colado). Numere os parágrafos como `[i]` e use esse número em todos os achados.
- A **data de referência**: data do documento, do fato investigado ou da avaliação. É ela que decide qual redação vale. Se não estiver clara, pergunte ou use a data do documento e avise. Data do documento já passada em relação a hoje não é falha: confira na data de referência e, se quiser, avise numa linha, sem 🔴 e sem mudar o veredito.
- O tipo de documento e a empresa ou atividade, se não estiverem óbvios.
- **Documento grande:** trabalhe por blocos, mantendo a numeração, e diga no fim quais parágrafos foram lidos. **PDF escaneado ou sem texto legível:** não finja que leu; marque ⚠️, diga o que faltou e peça o texto (colado ou em PDF com texto).

Se a conversa permitir delegar, faça A e B em duas leituras separadas, e na B leia só o documento, sem o que foi conversado sobre ele, para a leitura ser a frio. Sem essa possibilidade, faça duas passadas e, na B, julgue só o que está escrito.

## A. Conferente de citações

1. **Levantar** todas as citações com o parágrafo `[i]`: NR com item (inclusive alínea e subitem), anexo de NR, portaria do MTE, lei, decreto, CLT, convenção da OIT, NBR/ISO, instrução normativa, norma interna. Remissão sem norma identificada ("conforme item 4.2"): a norma é a do contexto. Se for ambígua, aponte.
2. **Conferir no texto oficial** (Regra A), buscando o item exato (por exemplo, `35.4.1`) e lendo só o trecho em volta:
   - **Existe?** Inclusive o subitem e a alínea. Erro comum: subitem certo no item errado.
   - **Diz o que o documento afirma?** Compare o conteúdo, não só o número. Citação entre aspas: confira palavra por palavra.
   - **Vigência na data de referência:** veja as marcas de vigência do texto ("redação dada pela Portaria...") e a tabela de alterações da NR. Redação posterior à data de referência aplicada a fato anterior é versão errada. Item revogado é 🔴.
   - **Redação antiga:** se o texto disponível é o atual e a data de referência é anterior a uma alteração, procure a redação da época: a portaria que alterou a NR no site do MTE ou no Diário Oficial da União (in.gov.br), e a versão consolidada da data, se o MTE a publicar. Se não achar a redação antiga, não presuma que o item era igual: ⚠️ e peça ao usuário o texto da época.
   - **NR-10:** há duas redações; confira qual o documento cita e se serve à data de referência. A nova foi aprovada pela Portaria MTE 737/2026, com início de vigência futuro: confira a data na fonte.
   - Informe a data em que o texto usado foi baixado ou consultado.
3. **Fora das NRs:** lei, decreto ou CLT na base local, se houver; senão na página oficial (planalto.gov.br, camara.leg.br), se a busca na web estiver disponível. Se você tiver um servidor ou conector de legislação instalado (por exemplo, o `br-eli-mcp`), pode usá-lo como atalho, mas ele é **opcional** e não substitui a fonte oficial. Sem conseguir, ⚠️ e peça o trecho.
4. **NBR e ISO:** confirme que a norma existe e qual é a edição vigente. O conteúdo de um item só é conferido se o usuário fornecer o texto; caso contrário, ⚠️ "conteúdo não conferido".
5. Manual, guia ou nota técnica citado como se fosse obrigação legal é 🟠, porque é interpretação, não norma.

Devolver uma tabela na ordem do documento, com duas colunas distintas, a origem (Regra A) e o resultado:

| [§] | Citação | Origem | Resultado | Nota (correção concreta) |
|---|---|---|---|---|

- **Origem:** ✅ Base local, 🌐 Fonte oficial ou ⚠️ Não conferido, com a data. O ⚠️ só aparece aqui e só significa "não conferido".
- **Resultado:** `Confere` · `Versão errada para a data` · `Não diz isso / interpretação citada como norma` (🟠) · `Inexistente, revogado ou contrário` (🔴) · `Sem conferência` (quando a origem é ⚠️).

Antes da tabela, em até 5 linhas: o total de citações, quantas de cada resultado e os 🔴 e 🟠 primeiro, cada um com a correção (item certo, redação vigente, norma que de fato diz aquilo, se achou).

## B. Revisor adversário

Leia o documento como quem quer achar o furo. Se estiver sólido, diga em uma linha e pare: não invente defeito para parecer útil, e não elogie por elogiar.

Quatro lentes:

1. **Auditor-Fiscal do Trabalho.** O documento tem os elementos mínimos que a NR aplicável exige para esse tipo de documento? Leia esses requisitos no texto da NR (Regra A); não presuma de memória. Responsável técnico, assinatura, datas, periodicidade e revisão estão presentes? Há medida de controle sem prazo ou sem responsável? A hierarquia de controle foi respeitada (EPI apresentado como primeira medida é achado)?
2. **Perito ou advogado do trabalhador** (ação trabalhista, acidente, insalubridade ou periculosidade). Onde o documento se contradiz (datas, funções, setores, agentes, valores medidos e limites)? Que evidência falta para sustentar o que afirma (lista de presença, ficha de EPI com CA válido, medição com equipamento calibrado, ordem de serviço assinada)? A conclusão decorre do que foi levantado? Na investigação de acidente: a causa raiz culpa só o trabalhador, sem analisar organização e gestão? Ou culpa a gestão sem evidência? Nenhuma causa se atribui sem evidência (ver `referencia/glossario-sst.md`).
3. **Quem executa em campo** (encarregado, eletricista, operador). As medidas são concretas e aplicáveis na atividade real? Há instrução vaga ("tomar cuidado", "usar EPI adequado") onde precisaria dizer qual EPI, qual bloqueio, qual sequência?
4. **Acabamento e padrão.** Campos ainda não preenchidos, numeração e versões, dado pessoal de trabalhador. Se o usuário tiver um padrão próprio de documento (cabeçalho, modelo, campos destacados para preencher), confira também esse padrão; se não houver, não presuma nenhum. É 🟡, salvo quando muda o sentido ou a validade do documento.

No máximo 12 achados, em ordem de gravidade:

- 🔴 **Derruba:** autuação provável, documento inválido, conclusão sem base, requisito obrigatório ausente.
- 🟠 **Enfraquece:** contradição, evidência que falta, medida inaplicável, citação frágil.
- 🟡 **Acabamento:** só o que um fiscal ou perito notaria.

Cada achado: `[parágrafo]` · o problema em uma frase · por quê (item conferido no texto da norma, com a origem da Regra A, ou trecho do documento, mascarado se tiver dado pessoal) · a correção em uma linha · se o requisito é **obrigação** (norma conferida) ou **boa prática** (recomendação). Separe **fato** (está no documento ou na norma) de **inferência** sua. Não reescreva parágrafos inteiros.

## Fechamento

- Uma linha com o que **não** foi conferido: NBR sem texto disponível, lei sem acesso ao texto, anexo que não veio, trecho escaneado ilegível, parágrafos não lidos, redação antiga não encontrada, data de referência presumida. Peça o trecho ou o PDF do que ficou ⚠️.
- Repita o aviso: apoio ao responsável técnico, não substituto.
- Ofereça, em uma linha, aplicar as correções no documento. Só com aprovação, e pela skill que gerou o documento, se houver (ex.: `investigacao-acidente-trabalho`).
- Se a conferência mostrar erro que veio de uma skill ou de um modelo do usuário (modelo com item errado, por exemplo), aponte para corrigir a origem.

## Idioma

Português do Brasil.
