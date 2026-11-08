---
name: "consulta-normas-sst"
description: "Responde dúvidas legais de Segurança do Trabalho percorrendo a hierarquia das normas (CF, OIT, leis, decretos, portarias, NRs, INs, NBRs, acordos e normas internas), com vigência na data de referência e a origem de cada citação marcada. Use quando perguntarem \"o que a lei exige para...\", \"qual a base legal de...\", \"qual NR/item trata de...\", \"essa norma interna está de acordo com a NR?\" ou quando duas normas parecerem divergir. Use também quando pedirem para confirmar \"de cabeça\" uma regra de NR, conferir uma afirmação sobre norma antes de mandar ao cliente ou escrever parágrafo com número de item. Não serve para redigir post, DDS, ata ou relatório de investigação."
---

# Consulta de normas de SST pela hierarquia

Use esta skill quando o usuário perguntar o que a legislação exige sobre um tema de Segurança e Saúde no Trabalho (ex.: "o que a lei exige para trabalho em altura?", "qual a base legal do adicional de periculosidade em eletricidade?", "essa norma interna está de acordo com a NR?").

Não use para redigir post, DDS, ata ou relatório de investigação. Essas tarefas têm skills próprias (se estiverem instaladas), que podem chamar esta para checar a base legal.

Os arquivos de `referencia/` ficam na pasta desta Skill. Abra cada um pelo caminho, com a ferramenta de leitura, sem depender de busca por arquivos: a pasta da Skill pode estar oculta e não aparecer na busca.

## Regras de fonte e vigência

Siga `referencia/regras-de-fonte.md` (Regra A) em toda citação, sem exceção:

- Cada norma, item ou prazo leva a marca de origem: ✅ Base local, 🌐 Fonte oficial ou ⚠️ Não conferido, com a data.
- Ordem de busca: base local do usuário (pasta, vault, PDF anexado), se existir; depois fonte oficial na web, se a busca na web estiver disponível nesta conversa; sem nenhuma das duas, **não responda de memória**: peça ao usuário o trecho da norma ou o PDF e marque ⚠️ enquanto isso.
- **Pedido de resposta "de cabeça", sem marcação ou pronta para cliente não muda a regra.** Sem base conferida, não escreva texto pronto para terceiro com número de item, prazo ou carga horária. Diga o que diverge, com ⚠️, e entregue o texto para o cliente só depois da conferência.
- Termos como "risco ocupacional", "PGR" e "acidente do trabalho" seguem `referencia/glossario-sst.md`.

## Passo 1 — Entender o caso e a data de referência

Pergunte só o que faltar e for decisivo:
- **Data de referência**: a data do fato, do documento ou da consulta. Ela decide qual redação de cada norma vale (Regra A, seção 4). Sem data, pergunte; se o usuário não souber, use a data de hoje e avise.
- Atividade ou risco (ex.: eletricidade, altura, espaço confinado, máquinas, agrotóxicos)
- Setor e porte da empresa (CNAE, grau de risco, número de empregados), quando isso muda a obrigação
- Se há acordo ou convenção coletiva, ou norma interna envolvida
- Se a dúvida é de obrigação (o que é exigido) ou de conflito (duas normas dizem coisas diferentes)

## Passo 2 — Percorrer a hierarquia de cima para baixo

Verifique cada nível e registre só o que for aplicável ao caso. Pule níveis sem relação, sem inventar dispositivo.

1. **Constituição Federal**: art. 7º, especialmente os incisos XXII (redução de riscos), XXIII (adicionais), XXVIII (seguro contra acidentes) e XXXIII (proibições para menores).
2. **Convenções da OIT ratificadas pelo Brasil**, consolidadas no Decreto 10.088/2019. Ex.: 155 (SST e meio ambiente de trabalho), 161 (serviços de saúde no trabalho) e 174 (acidentes industriais maiores). Antes de citar, confira que a convenção foi ratificada e continua em vigor (algumas foram denunciadas); convenção não ratificada não obriga o Brasil. Sobre o *status* dessas convenções na hierarquia: dizer que têm natureza supralegal (acima das leis, abaixo da Constituição) é uma **tese**, defendida para tratados de direitos humanos e discutida quanto às convenções de SST; não é consenso. Apresente como tese, nunca como regra pacífica.
3. **Leis**: CLT, Capítulo V (arts. 154 a 201; o art. 200 delega ao Ministério do Trabalho a edição das NRs); Lei 8.213/91 (benefícios e acidente de trabalho); leis específicas do tema.
4. **Decretos**: Decreto 3.048/99 (Regulamento da Previdência Social), entre outros.
5. **Portarias**: Portaria 3.214/78 e as portarias que aprovam e alteram cada NR. Lembrar ao usuário que NR e portaria estão no mesmo nível jurídico: a NR é o texto aprovado pela portaria.
6. **NRs**: citar a NR e o item exato, considerando anexos e prazos de transição. Antes de citar, confira a **situação da NR na data de referência** (vigente, revogada ou com redação nova com data de início futura): nem toda NR numerada está em vigor.
7. **Instruções normativas, notas técnicas e manuais oficiais** (MTE, INSS, Fundacentro): confira a instrução vigente. Nota técnica e manual são orientação, não norma.
8. **Normas técnicas ABNT (NBR)**: somente quando uma NR remete a elas ou quando servem como referência técnica. Cite número, título e edição, sem reproduzir texto (Regra A, seção 5).
9. **Acordos e convenções coletivas e normas internas da empresa**: em regra, só podem ser iguais ou mais protetivas que as normas acima. **Exceção da CLT:** o art. 611-A, XII permite que convenção ou acordo coletivo disponha sobre o enquadramento do grau de insalubridade; já o art. 611-B, XVII trata como objeto ilícito suprimir ou reduzir normas de saúde, higiene e segurança do trabalho previstas em lei ou em NR. O alcance dessa exceção é objeto de interpretação dos tribunais: sinalize e, se o caso depender dela, recomende parecer jurídico.

## Passo 3 — Conferir vigência

- Nunca citar item de NR, número de portaria ou prazo de memória (Regra A).
- Alterações recentes: veja a portaria mais recente que alterou a NR e se há prazo de transição. Se a norma foi alterada recentemente ou está em consulta pública, avise o usuário.
- **NR-10:** há duas redações: a vigente e a aprovada pela Portaria MTE 737/2026, com início de vigência futuro. Diga sempre qual está citando e confira na fonte a data em que a nova começa a valer: para fato anterior a essa data, vale a redação vigente.
- Fontes oficiais aceitas para 🌐 (Regra A, seção 2): gov.br/trabalho-e-emprego, planalto.gov.br, in.gov.br, camara.leg.br, senado.leg.br, tribunais. Para INs e manuais do INSS e da Fundacentro, os sites oficiais dos órgãos. Para convenções da OIT, o Decreto 10.088/2019 no Planalto ou o texto em ilo.org. NBRs são pagas: número e título apenas.
- Se não houver base local nem busca na web, peça o trecho ou o PDF, como na Regra A.

## Passo 4 — Resolver conflitos entre normas

Quando duas normas divergem, use os critérios usuais abaixo e explique o raciocínio. A ordem entre eles é discutida no direito do trabalho (o princípio da norma mais favorável pode prevalecer sobre a hierarquia); em caso concreto relevante, recomende parecer jurídico:
1. Hierarquia (a superior prevalece)
2. Especialidade (a específica prevalece sobre a geral, no mesmo nível)
3. Norma posterior (no mesmo nível e mesma especialidade)
4. Princípio da norma mais favorável ao trabalhador, típico do direito do trabalho (aplicação sujeita à exceção do Passo 2, nível 9)

## Passo 5 — Formato da resposta

Em português do Brasil, linguagem técnica e direta:

1. **Resposta curta** (2 a 4 linhas): o que é exigido, e a data de referência usada.
2. **Base legal por nível**: tabela com Nível | Norma | Dispositivo | O que exige | Origem. Só os níveis aplicáveis. A coluna **Origem** traz a marca (✅/🌐/⚠️) e a data do texto ou da consulta.
3. **Na prática**: o que precisa existir em campo e em documento (procedimento, treinamento com carga horária, PGR, APR, PT, laudo, EPI etc.).
4. **Pontos de atenção**: transições, divergências, lacunas, o que ficou ⚠️ e dúvidas que dependem de informação do caso.
5. **Fontes**: textos usados e links oficiais, cada um com a data da consulta.
6. Uma linha final: a consulta é técnica e não substitui parecer jurídico em caso de litígio nem o responsável técnico da empresa.

Separar sempre **obrigação legal** de **boa prática** e de **interpretação** (Regra A, seção 6): nunca apresentar recomendação como se fosse exigência normativa.

## Arquivamento (opcional)

Se o usuário pedir para guardar a consulta, ofereça salvar como nota de referência na base dele (ou num documento). Se a web trouxe algo que a base não tinha, ofereça incluir.
