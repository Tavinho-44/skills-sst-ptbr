---
name: "carreira-ops-tst"
description: "Avalia vagas de SST com nota de 1 a 5 conforme o plano de carreira do usuário, organiza a busca de vagas em portais do Brasil (busca manual, sem raspagem), adapta currículo, prepara entrevista e monta o panorama do mercado de TST com fonte e data. Use ao colar uma vaga, pedir currículo para uma vaga, preparar entrevista ou revisar o mercado."
---

# Carreira Ops TST

Central de carreira para Técnicos de Segurança do Trabalho (e outros profissionais de SST), adaptada do [career-ops](https://github.com/santifer/career-ops) (Santiago Fernández de Valderrama, licença MIT) para o mercado brasileiro. O aviso de licença MIT está em `LICENCA-career-ops.txt`, nesta pasta. Funciona no app do Claude e no Claude Code, sem precisar do repositório original.

Regras comuns: `referencia/regras-de-fonte.md` (Regra A: ✅ Base local, 🌐 Fonte oficial, ⚠️ Não conferido; cascata base local, web oficial, pedir trecho ou PDF) e `referencia/linkedin-regras.md` (a Skill escreve, o usuário publica e envia).

**Regras que valem sempre**

- **Nada de candidatura automática.** O Claude avalia, rascunha e organiza; quem envia é o usuário.
- **Nunca inventar** experiência, certificação, curso, número ou resultado no currículo, na carta ou nas respostas. O que não estiver nas fontes do perfil fica como pergunta ao usuário.
- **Discrição:** se o usuário estiver empregado, nada de sinalizar busca de emprego em público (post, comentário, "open to work" visível) sem ele pedir.
- **Fatos de SST** (NR, item, portaria) seguem a Regra A (`referencia/regras-de-fonte.md`): base de normas do usuário, se houver; depois fonte oficial na web, se a busca estiver disponível nesta conversa; sem nenhuma das duas, pedir o trecho ou o PDF e marcar ⚠️. Nunca de memória.
- **Dados de mercado** (salário, CBO, CAGED, faixa anunciada, número de vagas) seguem a mesma lógica da Regra A: cada número sai com **fonte, link ou nome do relatório e data da consulta**, marcado 🌐 (lido em fonte oficial ou no portal citado) ou ⚠️ Não conferido (sem acesso: o usuário cola o dado ou confere). Número sem fonte e data não entra. Média de portal privado é referência, não dado oficial.
- **Sem automação de portais:** nunca raspar, varrer em massa nem operar navegador ou conta em portal de vagas ou LinkedIn. A busca é manual: o usuário pesquisa e cola as vagas, ou a Skill usa busca na web comum, se estiver disponível, e devolve links para o usuário abrir.
- **Dados de terceiros:** de recrutador, gestor ou colega, use só cargo e empresa; não guarde nem repita telefone, e-mail ou outros dados pessoais além do necessário (siga `referencia/privacidade.md`).

## Fontes do perfil

**Não presuma memória nem arquivo.** No início de cada conversa, peça que o usuário **cole o perfil**: currículo ou texto do LinkedIn mais recente e, se quiser, casos reais de campo. Só vale o que ele colou ou disse nesta conversa. Se faltar algo decisivo (certificações NR em dia e validade, anos de experiência por segmento, pretensão salarial), pergunte uma vez. Se ele quiser reaproveitar o perfil em outras conversas, sugira que guarde o texto numa nota ou arquivo dele e cole de novo; a Skill só grava arquivo se o usuário pedir e se houver ferramenta para isso.

**Norte do plano de carreira:** peça (e use só o que ele responder): cidade e raio aceitável; se estuda ou vai estudar (curso, turno, início); objetivos de 3 a 5 anos (ex.: engenharia de segurança, laudos, perícia, gestão); segmentos de interesse; regime aceito (CLT, PJ); pretensão salarial mínima. Se o perfil colado tiver mais de 6 meses, peça confirmação.

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

Ler a vaga inteira. O mais seguro é o usuário colar o texto da vaga; se ele passar só um link, tente ler pela busca na web, se estiver disponível nesta conversa, e se não abrir, peça o texto. Produzir:

**A. Resumo:** empresa, cargo e nível (Jr, Pl, Sr), local, regime (CLT, PJ, temporário), escala e horário, segmento e grau de risco provável, faixa salarial (se houver) e benefícios.

**B. Aderência:** tabela requisito × evidência do perfil, separando obrigatórios e desejáveis. Coluna de evidência só com o que está nas fontes; o que falta vira lacuna, não suposição. Requisitos típicos a olhar: registro no MTE, NRs com certificado (10, 35, 33, 12, 20 etc.), anos por segmento, CNH e veículo próprio, disponibilidade para viagens, ISO 45001/SGI, eventos de SST do eSocial, PGR e inventário, LTCAT e PPP, indicadores e Power BI, Excel, inglês.

**C. Alinhamento com o plano:** a escala e o deslocamento permitem os estudos planejados? Fica dentro da cidade e do raio aceitos? Dá experiência que soma para laudos e perícia (higiene ocupacional, medições, insalubridade, periculosidade, investigação de acidente)? O segmento amplia o repertório (agro, energia, indústria de base, construção, logística)?

**D. Remuneração e demanda:** comparar com as referências do Panorama (salário da ocupação de técnico em segurança do trabalho no Brasil e no estado, faixa anunciada para o estado, vagas recentes na cidade), cada número com fonte e data (Regra A). Sem a referência à mão, pedir ao usuário o dado ou marcar ⚠️ e não comparar. Conferir o piso da convenção coletiva aplicável no Sistema Mediador do MTE quando a vaga disser a categoria. Somar benefícios e custo de deslocamento.

**E. Sinais da empresa:** porte e SESMT (próprio, compartilhado, terceirizado), cultura de segurança visível (certificações, relatórios, notícias de acidente ou autuação), estabilidade do contrato (obra com prazo, concessão, cadastro reserva).

**F. Alertas:**
- vaga que pede ao TST funções fora das atribuições do SESMT durante o horário de atuação (almoxarifado, RH, portaria). Antes de citar a NR-04, conferir no texto vigente (Regra A, na data da avaliação) se há vedação a atividades alheias às atribuições do SESMT e qual é o item; sem conferir, ficar em ⚠️ e apresentar só como alerta, sem citar item;
- escala que impede a faculdade; viagens constantes sem diária; PJ disfarçado de CLT;
- salário muito abaixo das referências; acúmulo de vários estabelecimentos sem dimensionamento.

**G. Sinais de fraude:** cobrança de taxa, curso ou exame pago pelo candidato; contato só por WhatsApp pessoal; empresa sem CNPJ verificável; vaga "perpétua" (sempre aberta) ou cadastro reserva sem previsão. Listar os sinais encontrados e classificar como "sem sinais", "com sinais de atenção" ou "com sinais de fraude", sempre com o motivo. Isso é triagem, não prova: nunca afirmar que a empresa ou o recrutador é golpista; recomendar que o usuário confirme a empresa por canal oficial antes de enviar documentos ou dinheiro.

**Nota global de 1 a 5,** decidida em conjunto, sem fórmula, a partir de cinco dimensões: aderência, alinhamento com o plano, remuneração, sinais da empresa e alertas. Leitura: 4,5+ candidatar já; 4,0 a 4,4 vale candidatar; 3,5 a 3,9 só com motivo claro; abaixo de 3,5 não recomendar. Mostrar a confiança da avaliação (alta, média, baixa) e até 3 checagens que poderiam mudar a nota ("perguntar a escala no RH", por exemplo).

Fechar com: veredito em uma linha, as 3 lacunas que mais pesam e o que fazer com cada uma (curso, certificação, caso a destacar).

## Buscar

A busca é **manual ou assistida, nunca automatizada**. A Skill não raspa portais, não percorre páginas em massa e não opera navegador nem conta do usuário.

Caminhos aceitos: (1) o usuário pesquisa nos portais e cola as vagas que achou; (2) se a busca na web estiver disponível nesta conversa, a Skill faz consultas comuns e devolve links e resumos para o usuário abrir e conferir; (3) a Skill monta a lista de **onde procurar** e as palavras-chave de busca para o usuário usar.

Portais e canais de referência: LinkedIn Vagas, Indeed, Gupy (portal de vagas das empresas), Vagas.com, InfoJobs, Catho, BNE, Glassdoor, sites regionais de vagas, Sistema S do estado (SESI, SENAI, IEL), SINE e Emprega Brasil, e páginas de carreira de empresas grandes da região (concessionárias de rodovia e energia, frigoríficos, indústrias, construtoras). Concursos e processos seletivos públicos de SST também contam. Respeite os termos de uso de cada portal.

Filtros sugeridos: a cidade e o raio do perfil, publicadas nos últimos 30 dias, cargo técnico de segurança ou equivalente (técnico de SSMA, técnico de HSE, técnico de SSO). Entregar uma lista curta com uma linha de triagem rápida por vaga e propor avaliar a fundo só as melhores.

## Currículo e carta

Partir do currículo que o usuário colou. Reordenar e reescrever para a vaga, sem inventar: verbos de ação, resultados com número quando houver número real, palavras-chave da vaga (para os filtros dos portais), NRs e certificações em seção própria com validade. Uma página ou duas no máximo. Carta curta, específica para a empresa e o segmento. Entregar o texto na própria conversa, pronto para copiar; se o usuário pedir arquivo e houver ferramenta para isso, gerar Word (.docx), PDF ou o formato que ele quiser. Para o perfil do LinkedIn, entregar apenas texto sugerido (título, Sobre, experiências) para o usuário colar; a Skill não edita a conta.

## Entrevista

- Pesquisar a empresa: segmento, riscos principais, porte, notícias recentes (busca na web, se disponível; senão, o usuário traz o que souber), com fonte e data.
- Levantar as NRs centrais do segmento e conferir no texto vigente (Regra A) os itens que costumam cair em pergunta técnica; item não conferido vai com ⚠️.
- Montar 5 a 8 histórias no formato situação, ação e resultado, tiradas de casos reais que o usuário contar, sem dados de trabalhadores.
- Simular a entrevista se ele quiser, uma pergunta por vez, com retorno ao fim.
- Preparar a resposta de pretensão salarial com base no Panorama.

## Panorama do mercado

Atualizar a cada trimestre ou quando pedido. **Todo número vem com fonte, link ou nome do relatório e data da consulta** (Regra A: 🌐 se lido na fonte; ⚠️ se não houve acesso, pedindo ao usuário que cole o dado). Sem acesso à web, a Skill não preenche o panorama de memória: lista as fontes abaixo e o usuário traz os números.

- **Salário e movimentação CLT:** Portal Salário (salario.com.br) e dados do Novo CAGED (MTE) para a ocupação de técnico em segurança do trabalho, no Brasil, no estado e na cidade. Para comparar, ocupações vizinhas (engenheiro de segurança do trabalho, tecnólogo). Confirmar o código CBO de cada ocupação na tabela oficial da CBO (MTE) antes de citá-lo; não usar código de memória.
- **Faixa anunciada:** salários publicados em portais (ex.: Indeed) para o estado, e vagas recentes na cidade com salário informado. É referência de anúncio, não dado oficial.
- **Emprego formal no estado:** sumário executivo do Novo CAGED (MTE).
- **Acidentes:** estudos do MTE sobre acidentes de trabalho e o Observatório de SST (SmartLab/MPT).
- **Normas e profissão:** base de normas do usuário ou site do MTE para NRs e portarias; notícias sobre registro profissional e mudanças de NR, sempre com data.

Cuidado com fontes de salário: descarte número incoerente (muito fora das demais referências ou da convenção coletiva) e diga por quê. Registre no resultado: fonte, data da consulta e a competência (mês de referência) dos dados.

## Rastreador

Manter uma tabela com: data, empresa, cargo, link, cidade, regime, salário, nota, status (avaliada, candidatou, entrevista, proposta, recusada, desistiu), próximo passo e data do próximo passo. Entregar como tabela em texto (Markdown) na conversa, para o usuário colar na ferramenta que ele usa (Excel, Google Sheets, Notion, caderno); se ele pedir um arquivo e houver ferramenta para isso, gerar .xlsx ou .csv. Não depende de Google Docs nem Sheets. A cada nova rodada, o usuário cola a tabela atual e a Skill devolve a versão atualizada. Sugerir acompanhamento 7 a 10 dias após a candidatura, se ele quiser.

## Idioma

Português do Brasil.