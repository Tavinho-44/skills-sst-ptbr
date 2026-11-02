---
name: "carreira-ops-tst"
description: "Avalia vagas de SST com nota de 1 a 5 conforme o seu plano de carreira, busca vagas em portais do Brasil, adapta currículo, prepara entrevista e atualiza o panorama do mercado de TST."
---

# Carreira Ops TST

Central de carreira para Técnicos de Segurança do Trabalho (e outros profissionais de SST), adaptada do [career-ops](https://github.com/santifer/career-ops) (Santiago Fernández de Valderrama, licença MIT) para o mercado brasileiro. Funciona no app do Claude e no Claude Code, sem precisar do repositório original.

**Regras que valem sempre**

- **Nada de candidatura automática.** O Claude avalia, rascunha e organiza; quem envia é o usuário.
- **Nunca inventar** experiência, certificação, curso, número ou resultado no currículo, na carta ou nas respostas. O que não estiver nas fontes do perfil fica como pergunta ao usuário.
- **Discrição:** se o usuário estiver empregado, nada de sinalizar busca de emprego em público (post, comentário, "open to work" visível) sem ele pedir.
- **Fatos de SST** (NR, item, portaria) saem da base de normas do usuário, se houver, ou das fontes oficiais; nunca de memória.
- **Dados de mercado** sempre com fonte e data; número sem fonte não entra.

## Fontes do perfil

Antes de qualquer modo, montar o perfil a partir de: o que o Claude já sabe do usuário (memória ou projeto), o currículo ou LinkedIn mais recente que ele passar e casos reais que ele contar. Se faltar algo decisivo (certificações NR em dia, anos de experiência por segmento, pretensão salarial), perguntar uma vez.

**Norte do plano de carreira:** na primeira vez, perguntar e guardar (na memória ou num arquivo `perfil-carreira.md`): cidade e raio aceitável; se estuda ou vai estudar (curso, turno, início); objetivos de 3 a 5 anos (ex.: engenharia de segurança, laudos, perícia, gestão); segmentos de interesse; regime aceito (CLT, PJ); pretensão salarial mínima. Conferir de novo se a informação tiver mais de 6 meses.

## Modos

| Pedido | Modo |
|---|---|
| Colou uma vaga (link ou texto) | **Avaliar vaga** |
| "Compara essas vagas" | **Comparar** (avaliar cada uma, depois tabela) |
| "Procura vagas" | **Buscar** |
| "Ajusta meu currículo para essa vaga" / carta | **Currículo e carta** |
| "Tenho entrevista" | **Entrevista** |
| "Como está o mercado" / revisão trimestral | **Panorama** |
| "Atualiza o acompanhamento" | **Rastreador** |

## Avaliar vaga

Ler a vaga inteira. Se for link, abrir; se não abrir, pedir o texto. Produzir:

**A. Resumo:** empresa, cargo e nível (Jr, Pl, Sr), local, regime (CLT, PJ, temporário), escala e horário, segmento e grau de risco provável, faixa salarial (se houver) e benefícios.

**B. Aderência:** tabela requisito × evidência do perfil, separando obrigatórios e desejáveis. Coluna de evidência só com o que está nas fontes; o que falta vira lacuna, não suposição. Requisitos típicos a olhar: registro no MTE, NRs com certificado (10, 35, 33, 12, 20 etc.), anos por segmento, CNH e veículo próprio, disponibilidade para viagens, ISO 45001/SGI, eSocial SST (S-2210, S-2220, S-2240), PGR e inventário, LTCAT e PPP, indicadores e Power BI, Excel, inglês.

**C. Alinhamento com o plano:** a escala e o deslocamento permitem os estudos planejados? Fica dentro da cidade e do raio aceitos? Dá experiência que soma para laudos e perícia (higiene ocupacional, medições, insalubridade, periculosidade, investigação de acidente)? O segmento amplia o repertório (agro, energia, indústria de base, construção, logística)?

**D. Remuneração e demanda:** comparar com as referências do Panorama (salário médio do CBO 3516-05 no Brasil e no estado, faixa anunciada no Indeed para o estado, vagas recentes na cidade). Conferir o piso da convenção coletiva aplicável no Sistema Mediador do MTE quando a vaga disser a categoria. Somar benefícios e custo de deslocamento.

**E. Sinais da empresa:** porte e SESMT (próprio, compartilhado, terceirizado), cultura de segurança visível (certificações, relatórios, notícias de acidente ou autuação), estabilidade do contrato (obra com prazo, concessão, cadastro reserva).

**F. Alertas:**
- vaga que pede ao TST funções fora das atribuições do SESMT durante o horário de atuação (almoxarifado, RH, portaria). Conferir no texto vigente da NR-04 a vedação de atividades alheias às atribuições do SESMT (item 4.3.8 na redação consultada em outubro de 2026) antes de citar;
- escala que impede a faculdade; viagens constantes sem diária; PJ disfarçado de CLT;
- salário muito abaixo das referências; acúmulo de vários estabelecimentos sem dimensionamento.

**G. Legitimidade da vaga:** cobrança de taxa, curso ou exame pago pelo candidato; contato só por WhatsApp pessoal; empresa sem CNPJ verificável; vaga "perpétua" (sempre aberta) ou cadastro reserva sem previsão. Marcar como confiável, suspeita ou golpe provável, com o motivo.

**Nota global de 1 a 5,** decidida em conjunto, sem fórmula, a partir de cinco dimensões: aderência, alinhamento com o plano, remuneração, sinais da empresa e alertas. Leitura: 4,5+ candidatar já; 4,0 a 4,4 vale candidatar; 3,5 a 3,9 só com motivo claro; abaixo de 3,5 não recomendar. Mostrar a confiança da avaliação (alta, média, baixa) e até 3 checagens que poderiam mudar a nota ("perguntar a escala no RH", por exemplo).

Fechar com: veredito em uma linha, as 3 lacunas que mais pesam e o que fazer com cada uma (curso, certificação, caso a destacar).

## Buscar

Portais: LinkedIn Vagas, Indeed, Gupy (portal de vagas das empresas), Vagas.com, InfoJobs, Catho, BNE, Glassdoor, sites regionais de vagas, Sistema S do estado (SESI, SENAI, IEL), SINE e Emprega Brasil, e páginas de carreira de empresas grandes da região (concessionárias de rodovia e energia, frigoríficos, indústrias, construtoras). Concursos e processos seletivos públicos de SST também contam.

Usar o navegador só para ler. Filtrar por: a cidade e o raio do perfil, publicadas nos últimos 30 dias, cargo técnico de segurança ou equivalente (técnico de SSMA, técnico de HSE, técnico de SSO). Entregar uma lista curta com uma linha de triagem rápida por vaga e propor avaliar a fundo só as melhores.

## Currículo e carta

Partir do currículo atual do usuário. Reordenar e reescrever para a vaga, sem inventar: verbos de ação, resultados com número quando houver número real, palavras-chave da vaga (para os filtros dos portais), NRs e certificações em seção própria com validade. Uma página ou duas no máximo. Carta curta, específica para a empresa e o segmento. Entregar como documento (tipo Docs) ou Word se ele pedir. Para o perfil do LinkedIn, usar uma skill própria de perfil, se houver.

## Entrevista

- Pesquisar a empresa: segmento, riscos principais, porte, notícias recentes.
- Levantar as NRs centrais do segmento e conferir no texto vigente os itens que costumam cair em pergunta técnica.
- Montar 5 a 8 histórias no formato situação, ação e resultado, tiradas de casos reais que o usuário contar, sem dados de trabalhadores.
- Simular a entrevista se ele quiser, uma pergunta por vez, com retorno ao fim.
- Preparar a resposta de pretensão salarial com base no Panorama.

## Panorama do mercado

Atualizar a cada trimestre ou quando pedido, sempre com data e fonte:

- **Salário e movimentação CLT:** Portal Salário (salario.com.br), CBO 3516-05, Brasil, estado e cidade (dados do Novo CAGED); comparar com Engenheiro de Segurança (CBO 2149-15) e Tecnólogo (2149-35).
- **Faixa anunciada:** Indeed salários para o estado; vagas recentes na cidade com salário informado.
- **Emprego formal no estado:** sumário executivo do Novo CAGED (MTE).
- **Acidentes:** estudo do MTE de acidentes de trabalho (CANPAT) e Observatório de SST (SmartLab/MPT).
- **Normas e profissão:** base de normas do usuário ou site do MTE para NRs e portarias; notícias sobre registro profissional e mudanças de NR.

Cuidado com fontes de salário: o Glassdoor já mostrou valores claramente errados para alguns estados; descartar número incoerente e dizer por quê.

## Rastreador

Manter uma planilha (tipo Sheets) com: data, empresa, cargo, link, cidade, regime, salário, nota, status (avaliada, candidatou, entrevista, proposta, recusada, desistiu), próximo passo e data do próximo passo. Lembrar acompanhamento 7 a 10 dias após a candidatura, se ele quiser.

## Idioma

Português do Brasil.