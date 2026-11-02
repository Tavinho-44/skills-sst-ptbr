# Skills de SST para o Claude (pt-BR)

Skills em português do Brasil para profissionais de **Segurança e Saúde no Trabalho**: consulta de normas pela hierarquia legal, conferência de documentos como um auditor faria, investigação de acidentes, conteúdo técnico para o LinkedIn e uma central de carreira para TST.

Funcionam no **app do Claude** (web, desktop e celular) e no **Claude Code**. Todas seguem o padrão aberto de Agent Skills (uma pasta com um `SKILL.md`).

> Autor: Luiz Gustavo Gomes da Costa, Técnico de Segurança do Trabalho. As skills apoiam o trabalho técnico, não o substituem: toda citação de norma deve ser conferida no texto vigente, e a responsabilidade por documentos e laudos é de quem assina.

## As skills

### Normas e documentos

| Skill | O que faz |
|---|---|
| [consulta-normas-sst](skills/consulta-normas-sst/SKILL.md) | Responde dúvidas legais de SST percorrendo a hierarquia: CF, convenções da OIT, leis, decretos, portarias, NRs, INs, NBRs e normas internas. Separa obrigação legal de boa prática e informa as fontes. |
| [conferencia-documento-sst](skills/conferencia-documento-sst/SKILL.md) | Duas leituras de um documento pronto (PGR, laudo, OS, procedimento, investigação): confere cada citação (existe, diz isso, está vigente na data?) e faz revisão adversária com quatro olhares: fiscal do trabalho, perito, quem executa em campo e acabamento. |
| [investigacao-acidente-trabalho](skills/investigacao-acidente-trabalho/SKILL.md) | Transforma um relato bruto de acidente em relatório técnico de investigação em Word, com 5 Porquês e 5M, separando fato, evidência e hipótese. |

### Conteúdo para o LinkedIn

| Skill | O que faz |
|---|---|
| [revisao-tecnica-post-sst](skills/revisao-tecnica-post-sst/SKILL.md) | Revisa post, carrossel ou legenda antes de publicar: NRs vigentes, termos técnicos, dados com fonte, tom e risco de expor pessoas ou empresas. |
| [caso-de-campo-para-post](skills/caso-de-campo-para-post/SKILL.md) | Transforma um caso de campo, DDS ou investigação em post anonimizado, com a lição técnica em primeiro plano. |
| [humanizer-ptbr](skills/humanizer-ptbr/SKILL.md) | Tira as marcas de texto de IA de textos em português, preservando NRs, números e termos técnicos. Tem scripts Python sem dependências. |
| [calendario-editorial-sst](skills/calendario-editorial-sst/SKILL.md) | Monta calendário editorial mensal ou trimestral com pilares de conteúdo e datas do setor (Abril Verde, 28 de abril, campanhas usadas em SIPAT etc.). |
| [comentarios-linkedin-sst](skills/comentarios-linkedin-sst/SKILL.md) | Escreve comentários em posts de outras pessoas que soam como profissional com opinião, não como robô. |
| [respostas-comentarios-linkedin](skills/respostas-comentarios-linkedin/SKILL.md) | Organiza e responde os comentários nos seus próprios posts, separando oportunidade, conteúdo, colega, apoio e ruído. |
| [convite-conexao-linkedin](skills/convite-conexao-linkedin/SKILL.md) | Nota do convite de conexão (até 200 caracteres), primeira mensagem e acompanhamentos, para SST, RH e recrutadores. |

### Carreira

| Skill | O que faz |
|---|---|
| [carreira-ops-tst](skills/carreira-ops-tst/SKILL.md) | Avalia vagas de SST com nota de 1 a 5 conforme o seu plano de carreira, busca vagas em portais brasileiros (só lendo, nunca se candidata sozinha), adapta currículo sem inventar nada, prepara entrevista e mantém um panorama do mercado de TST com fontes (CAGED, MTE, Observatório de SST). |

## Como instalar

### No app do Claude (web, desktop ou celular)

1. Baixe o `.zip` da skill na pasta [`pacotes/`](pacotes/).
2. No Claude, abra as configurações de Skills e envie o arquivo.
3. Ative a skill. Ela entra sozinha quando o pedido combina com a descrição.

### No Claude Code

Todas de uma vez, como plugin:

```
/plugin marketplace add Tavinho-44/skills-sst-ptbr
/plugin install skills-sst@skills-sst-ptbr
```

Ou só uma, copiando a pasta para a sua pasta de skills:

```bash
git clone https://github.com/Tavinho-44/skills-sst-ptbr.git
cp -r skills-sst-ptbr/skills/consulta-normas-sst ~/.claude/skills/
```

## Base de normas local (opcional)

As skills de normas funcionam direto com as fontes oficiais (gov.br/trabalho-e-emprego, planalto.gov.br, in.gov.br). Se você mantiver as NRs, portarias e leis em Markdown (por exemplo, num vault do Obsidian), elas buscam ali primeiro: fica mais rápido, gasta menos e permite conferir o item exato com a data em que o texto foi baixado.

## Avisos

- NRs, portarias e prazos mudam. As skills mandam conferir a vigência, mas a conferência final é sua.
- Nada de dados pessoais de trabalhadores em posts ou exemplos: as skills anonimizam por função e setor.
- As skills de LinkedIn escrevem; quem publica é você. Automatizar comentários ou convites viola os termos do LinkedIn.

## Créditos

Veja [CREDITOS.md](CREDITOS.md). Partes de algumas skills foram adaptadas de projetos abertos de outros autores, com as licenças respeitadas.

## Licença

[MIT](LICENSE). Use, adapte e compartilhe; mantenha o aviso de licença e os créditos.
