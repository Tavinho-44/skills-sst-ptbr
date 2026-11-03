---
name: "consulta-normas-sst"
description: "Responde dúvidas legais de Segurança do Trabalho percorrendo a hierarquia das normas (CF, OIT, leis, decretos, portarias, NRs, INs, NBRs, normas internas) com vigência conferida e fontes."
---

# Consulta de normas de SST pela hierarquia

Use esta skill quando o usuário perguntar o que a legislação exige sobre um tema de Segurança e Saúde no Trabalho (ex.: "o que a lei exige para trabalho em altura?", "qual a base legal do adicional de periculosidade em eletricidade?", "essa norma interna está de acordo com a NR?").

Não use para redigir post, DDS, ata ou relatório de investigação. Essas tarefas têm skills próprias, mas podem chamar esta para checar a base legal.

**Fonte primária: a base local de normas, se você tiver uma** (por exemplo, um vault do Obsidian com as NRs, portarias e leis em Markdown, com a data em que cada texto foi baixado). Busque nela o item exato e leia só o trecho em volta, sem abrir a norma inteira. Sem base local, vá direto às fontes oficiais do Passo 3.

## Passo 1 — Entender o caso antes de consultar

Identifique, perguntando só o que faltar e for decisivo:
- Atividade ou risco (ex.: eletricidade, altura, espaço confinado, máquinas, agrotóxicos)
- Setor e porte da empresa (CNAE, grau de risco, número de empregados), quando isso muda a obrigação
- Se há acordo ou convenção coletiva, ou norma interna envolvida
- Se a dúvida é de obrigação (o que é exigido) ou de conflito (duas normas dizem coisas diferentes)

## Passo 2 — Percorrer a hierarquia de cima para baixo

Verifique cada nível e registre só o que for aplicável ao caso. Pule níveis sem relação, sem inventar dispositivo.

1. **Constituição Federal**: art. 7º, especialmente XXII (redução de riscos), XXIII (adicionais), XXVIII (seguro contra acidentes) e XXXIII (proibições para menores).
2. **Convenções da OIT ratificadas** (status supralegal): consolidadas no Decreto 10.088/2019. Ex.: 155 (SST e meio ambiente de trabalho), 161 (serviços de saúde no trabalho) e 174 (acidentes industriais maiores). A 184 (agricultura) não foi ratificada pelo Brasil.
3. **Leis**: CLT arts. 154 a 201 (Capítulo V, redação da Lei 6.514/77; art. 200 delega ao Ministério do Trabalho a edição das NRs); Lei 8.213/91 (benefícios e acidente de trabalho); leis específicas do tema.
4. **Decretos**: Decreto 3.048/99 (Regulamento da Previdência Social), entre outros.
5. **Portarias**: Portaria 3.214/78 e as portarias que aprovam e alteram cada NR. Lembrar ao usuário que NR e portaria estão no mesmo nível jurídico: a NR é o texto aprovado pela portaria.
6. **NRs vigentes**: citar a NR e o item exato. Considerar anexos e prazos de transição.
7. **Instruções normativas, notas técnicas e manuais oficiais**: MTE, INSS (ex.: IN PRES/INSS 128/2022), Fundacentro.
8. **Normas técnicas ABNT (NBR)**: somente quando uma NR remete a elas ou quando servem como referência técnica. Ex.: NR-10 remete à NBR 5410 e à NBR 14039.
9. **Acordos e convenções coletivas e normas internas da empresa**: só podem ser iguais ou mais protetivas que as normas acima.

## Passo 3 — Buscar e conferir vigência

- Nunca citar item de NR, número de portaria ou prazo de memória sem conferir. NRs são revisadas com frequência.
- **Primeiro a base local, se houver:** ache o item (ex.: `35.4.1`) e leia só o trecho. Informe a data em que aquele texto foi baixado.
- Alterações recentes: confira a portaria mais recente que alterou a NR e se há prazo de transição. NR-10: a redação atual vale até 31/05/2027 e a nova a partir de 01/06/2027; diga qual está citando.
- **Web só para conferir vigência ou cobrir lacuna** (avisando que a base local não tinha), nas fontes oficiais, anotando a data da consulta:
  - planalto.gov.br (CF, leis, decretos)
  - gov.br/trabalho-e-emprego (NRs atualizadas e portarias)
  - in.gov.br (Diário Oficial da União)
  - gov.br/inss e Fundacentro (INs, notas e manuais)
  - ilo.org (texto das convenções)
  - ABNT (NBRs são pagas: indicar número e título, sem reproduzir texto)
- Se a norma foi alterada recentemente ou está em consulta pública, avisar o usuário.
- NR-02 e NR-27 estão revogadas: não citar como vigentes.

## Passo 4 — Resolver conflitos entre normas

Quando duas normas divergem, aplicar nesta ordem e explicar o raciocínio:
1. Hierarquia (a superior prevalece)
2. Especialidade (a específica prevalece sobre a geral, no mesmo nível)
3. Norma posterior (no mesmo nível e mesma especialidade)
4. Princípio da norma mais favorável ao trabalhador, típico do direito do trabalho

## Passo 5 — Formato da resposta

Em português do Brasil, linguagem técnica e direta:

1. **Resposta curta** (2 a 4 linhas): o que é exigido.
2. **Base legal por nível**: tabela com Nível | Norma | Dispositivo | O que exige. Só os níveis aplicáveis.
3. **Na prática**: o que precisa existir em campo e em documento (procedimento, treinamento com carga horária, PGR, APR, PT, laudo, EPI etc.).
4. **Pontos de atenção**: transições, divergências, lacunas, dúvidas que dependem de informação do caso.
5. **Fontes**: textos usados (com a data em que foram baixados) e links oficiais com data da consulta.
6. Uma linha final: a consulta é técnica e não substitui parecer jurídico em caso de litígio.

Separar sempre **obrigação legal** de **boa prática**: nunca apresentar recomendação como se fosse exigência normativa.

## Arquivamento (opcional)

Se o usuário pedir para guardar a consulta, oferecer salvar como nota de referência na base local (ou num documento). Se a web trouxe algo que a base não tinha, oferecer incluir.