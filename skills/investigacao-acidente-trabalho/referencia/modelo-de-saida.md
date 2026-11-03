# Modelo de saída — relatório de investigação de acidente de trabalho

Arquivo próprio desta Skill (não vem de `comum/`). Estrutura fixa, sempre nesta ordem. Todo relatório gerado por esta Skill segue esta sequência de seções.

Onde faltar informação, escreva **Não informado** (o relato não traz) ou **A apurar — por [função]** (ainda não foi levantado). Não deixe seção vazia e não invente dado.

**Cabeçalho do rascunho** (antes da seção 1):

> **RASCUNHO para revisão técnica.** Elaborado com apoio de IA a partir do relato fornecido. Não substitui a investigação oficial da empresa nem o parecer do responsável técnico. As conclusões valem apenas para as evidências listadas na seção 8.

Título, empresa ou unidade (se o usuário quiser informar) e data de elaboração do rascunho.

## Seções

1. **Descrição da ocorrência** — resumo objetivo do que aconteceu, com a classificação do evento (por exemplo: acidente com afastamento, sem afastamento, quase acidente). Se usar "quase acidente" ou "incidente", explique o sentido no texto ("ocorrência sem lesão que poderia ter causado lesão").
2. **Local** — unidade, setor, ponto exato do acidente.
3. **Data**
4. **Horário**
5. **Atividade executada** — o que estava sendo feito no momento do acidente.
6. **Equipamentos envolvidos**
7. **Pessoas envolvidas** — vítima(s), testemunhas, quem prestou socorro, identificados por função, setor e vínculo (próprio ou terceiro), sem nome, CPF ou matrícula.
8. **Evidências analisadas** — o que foi recebido e examinado (relato, fotos, registros, documentos, medições, depoimentos), com o que **não** foi recebido. Cada item indica o que sustenta.
9. **Sequência cronológica dos fatos** — reconstrução em ordem temporal, com horários quando disponíveis. Se houver versões conflitantes, registre cada uma por função, sem escolher, marque como hipótese e indique a evidência que resolveria.
10. **Danos observados** — lesões (natureza e parte do corpo atingida, sem CID nem diagnóstico individual além do necessário à análise), danos materiais, ou ambos.
11. **Medidas imediatas** — o que foi feito ou precisa ser feito já (socorro, isolamento da área, preservação do local e das evidências, interdição, comunicação interna), com responsável por cargo. Diferente das recomendações da seção 19.
12. **Causas imediatas** — o que foi feito ou observado e que gerou o evento diretamente, descrito sem rótulo de culpa (ver glossário, seção 2), com o fator que permitiu. Cada causa leva o rótulo fato, evidência ou hipótese.
13. **Causas básicas** — falhas de método, processo, organização ou gestão por trás das causas imediatas. Só afirme falha de gestão ou de pessoa com evidência; sem evidência, é hipótese e vai rotulada.
14. **Fatores contribuintes**
15. **Análise dos 5 Porquês** — cada porquê com o rótulo fato, evidência ou hipótese. A causa raiz só é afirmada se o último porquê for fato ou evidência; senão, "causa raiz provável (hipótese)" com o que falta para confirmar.
16. **Análise 5M** (Método, Mão de obra, Máquina, Material, Meio Ambiente)
17. **Barreiras existentes** — o que deveria ter evitado ou minimizado o evento e existia.
18. **Barreiras ausentes** — o que deveria existir e não existia.
19. **Recomendações** — ações corretivas e preventivas específicas ao caso, ligadas às causas das seções 12 a 16.
20. **Plano de ação** — ação, responsável (por cargo ou função, nunca por nome) e prazo, quando a informação existir ou puder ser proposta de forma realista; do contrário, **A apurar**.
21. **Limitações da análise** — o que não foi possível apurar, evidências ausentes, versões não resolvidas, hipóteses que podem mudar a conclusão.
22. **Conclusão técnica** — o que está sustentado por fato ou evidência e o que permanece como hipótese.
23. **Responsável técnico** — bloco em branco para o responsável preencher:

   - Nome: ______
   - Profissão e registro profissional: ______
   - Data da revisão: ______
   - Assinatura: ______

   Não presuma profissão nem preencha nome: quem assina informa.

## Regras de conteúdo

- Cada seção tem conteúdo específico ao caso relatado, nunca frase genérica de preenchimento.
- Fato observado, evidência, inferência e hipótese são diferenciados ao longo de todo o texto, especialmente nas seções 12 a 16.
- Vocabulário sem culpa presumida: ver `glossario-sst.md`, seção 2.
- Citação de norma, quando houver: Regra A (`regras-de-fonte.md`), com a data do acidente como data de referência.
- Privacidade: `privacidade.md`.
