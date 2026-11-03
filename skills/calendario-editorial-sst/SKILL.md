---
name: "calendario-editorial-sst"
description: "Monta calendário editorial de posts de Segurança do Trabalho no LinkedIn por mês ou trimestre, em tabela, com pilares de conteúdo, formatos e datas do setor. Toda data ou campanha sai com origem e data da conferência, ou marcada como não conferida. Use quando o usuário pedir calendário de posts, planejamento de conteúdo, pauta do mês ou o que postar nas próximas semanas."
---

# Calendário editorial de SST para LinkedIn

Planeja o que publicar, quando e em que formato, para o usuário postar com regularidade sem depender de inspiração no dia. Quem publica é o usuário; a Skill só entrega o plano. Nunca publica, agenda nem opera o navegador no LinkedIn (`referencia/linkedin-regras.md`).

O usuário trabalha com SST, na função que ele informar (não presuma). Pergunte os segmentos em que ele atua, se não souber. Não restrinja o conteúdo ao segmento atual: o segmento sai do tema, então varie ao longo do mês. O público é formado por profissionais de SST, supervisores, gestores de operação e trabalhadores de vários setores.

## Regras que valem sempre

- **Nenhuma data, campanha ou prazo vai para o calendário sem origem.** Cada data leva a origem (nome da fonte e link) e a data em que foi conferida. Sem origem, a data entra marcada com ⚠️ e o texto "conferir antes de usar". Nunca escreva uma data de memória como se fosse certa.
- **Nunca inventar caso, número ou experiência do usuário.** O pilar "caso de campo" só recebe um espaço reservado ("relato do usuário a definir"); o caso vem dele. O mesmo vale para estatísticas: sem fonte e data, não entram.
- **Percentuais de distribuição, dias e horários de postagem são sugestões**, não regras do LinkedIn. Diga isso na entrega.
- Norma citada segue `referencia/regras-de-fonte.md` (Regra A): ✅ Base local, 🌐 Fonte oficial ou ⚠️ Não conferido, com data. Uma NR ou mudança de NR com vigência no período só entra com origem; sem ela, ⚠️.

## Entrada

Pergunte só o que faltar:

- Período (próximo mês, trimestre) e o ano.
- Frequência desejada (sugestão de partida: 3 posts por semana).
- Segmentos em que atua e temas que quer priorizar ou evitar.
- Se já tem métricas de posts anteriores. Se tiver, elas valem mais que as sugestões abaixo.

## Pilares de conteúdo (sugestão de distribuição)

Distribua os posts entre estes pilares, mais ou menos nesta proporção. É uma sugestão de equilíbrio; ajuste ao que o usuário pedir:

1. **Norma na prática (cerca de 25%):** uma NR ou item explicado com aplicação real (NR-10, NR-12, NR-18, NR-31, NR-33, NR-35, NR-01/GRO etc.). O item só entra no tema se tiver origem pela Regra A; senão, o tema fica pela NR e o item é conferido na hora de escrever.
2. **Caso de campo (cerca de 25%):** experiência vivida pelo usuário, anonimizada. A Skill `caso-de-campo-para-post` deste repositório ajuda, e é opcional.
3. **Notícia e dado (cerca de 20%):** atualidade do setor ou estatística com leitura crítica. Dado sem fonte e data não entra.
4. **Gestão e cultura (cerca de 15%):** liderança, indicadores, DDS eficaz, cultura de segurança.
5. **Carreira em SST (cerca de 15%):** rotina do técnico, formação, mercado, erros de iniciante.

## Datas do setor

As datas e campanhas mudam de ano para ano e algumas são de empresa ou de região. Por isso o texto desta Skill não traz datas fixas. Procure, para o período pedido, as que fazem sentido:

- Campanhas nacionais de prevenção e conscientização em SST (candidatas a conferir: CANPAT, Abril Verde).
- Dias comemorativos da área (dia do técnico de segurança do trabalho, dia nacional de prevenção de acidentes do trabalho, dia em memória das vítimas de acidentes e doenças do trabalho).
- Campanhas de saúde e a SIPAT da empresa (saúde mental e riscos psicossociais, prevenção de câncer, entre outras). A data da SIPAT é da empresa: pergunte ao usuário.
- Datas ligadas a segmentos do usuário (período de chuvas e descargas atmosféricas, calor, safra, paradas programadas).
- Mudanças de NR com vigência no período.

Como obter e registrar cada data:

1. **Com busca na web, se estiver disponível nesta conversa:** consulte fonte oficial (gov.br/trabalho-e-emprego, planalto.gov.br para leis, in.gov.br para o Diário Oficial; para campanhas, a página do órgão ou entidade que a promove). Registre o link e a data da consulta.
2. **Sem busca na web:** peça ao usuário as datas que ele já tem (calendário da empresa, da CIPA, do sindicato, do SESMT) ou os links das fontes. Se ele não tiver, monte o calendário só com os temas, sem data de campanha, e marque cada data sugerida como ⚠️ "conferir antes de usar".
3. Data de feriado ou comemoração que o modelo apenas "lembra": ⚠️, sempre.

Campanha ou data do tipo "habitualmente em tal mês" não é conferência. Se for o que há, escreva "⚠️ mês habitual, conferir o ano".

## Montagem

Para cada post, defina:

- **Data e dia da semana**, a partir do calendário do ano pedido. Priorize terça a quinta, de manhã, só como ponto de partida (sugestão); se o usuário tiver métricas dizendo outra coisa, siga as métricas.
- **Pilar.**
- **Tema e ângulo** (não o óbvio: o ponto de vista do usuário).
- **Formato:** texto, carrossel, enquete ou vídeo curto. Sugira ao menos 1 carrossel por semana, se o usuário tiver como produzir.
- **Origem da data** (quando o post depende de uma data ou campanha) e **data da conferência**, ou ⚠️.
- **Apoio, se quiser (opcional):** `caso-de-campo-para-post`, `revisao-tecnica-post-sst` e `humanizer-ptbr`, Skills deste repositório. Sem elas, o usuário escreve e revisa à mão.
- **Espaço "notícia do dia"**: reserve 1 post por semana sem tema fixo, para reagir a uma notícia.

Evite repetir o mesmo pilar ou a mesma NR em posts seguidos.

## Entrega

- **Tabela em Markdown** por padrão, com colunas: data, dia da semana, pilar, tema e ângulo, formato, origem da data e conferência, apoio, status. Se o usuário pedir, entregue também em CSV (separador vírgula, cabeçalho na primeira linha, UTF-8), para abrir no Excel ou em outra planilha.
- Um parágrafo curto com a lógica do período.
- Uma linha lembrando: percentuais, dias e horários são sugestões, e toda linha com ⚠️ precisa de conferência do usuário antes de virar post.
- Oferta: rascunhar os posts da primeira semana. Posts que citem norma só ficam prontos para publicar se todas as citações estiverem ✅ ou 🌐.

## Exemplo ilustrativo do formato (valores fictícios)

| Data | Dia | Pilar | Tema e ângulo | Formato | Origem da data / conferência | Apoio | Status |
|---|---|---|---|---|---|---|---|
| (a definir) | ter | Norma na prática | NR-35: o que muda quando o ponto de ancoragem é improvisado | Carrossel | Sem data de campanha | `revisao-tecnica-post-sst` (opcional) | Ideia |
| (a definir) | qui | Caso de campo | Relato do usuário sobre uma barreira que falhou (caso a informar) | Texto | Sem data de campanha | `caso-de-campo-para-post` (opcional) | Aguardando relato |
| (a definir) | qua | Gestão e cultura | DDS: quando a pergunta vale mais que a leitura | Texto | ⚠️ Campanha de saúde do mês: conferir o ano | n/a | Ideia |
