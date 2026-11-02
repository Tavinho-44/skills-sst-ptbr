---
name: "respostas-comentarios-linkedin"
description: "Organiza e escreve as respostas aos comentários nos posts do próprio usuário no LinkedIn, separando oportunidade, conteúdo, colega, apoio e ruído. Use ao colar comentários de um post dele."
---

# Respostas aos comentários

Adaptado de li-reply (linkedin-agent-skill, Jake Schincariol, MIT) para português e Segurança do Trabalho.

Use quando o usuário colar os comentários de um post dele e pedir "responde esses comentários", "o que eu falo pra essa pessoa", "alguém discordou do meu post" ou estiver lidando com crítica ou com um possível contato de trabalho nos comentários.

A conversa embaixo do post é onde o alcance se decide: cada resposta é uma nova interação, e a primeira hora pesa mais. Mas nem todo comentário vale o mesmo, então a skill separa antes de escrever.

## Entrada

O usuário cola os comentários, de preferência com nome e cargo. Print serve. Não use o navegador para ler a conversa.

## Triagem primeiro

Classifique cada comentário e diga a contagem:

| Grupo | O que é | O que recebe |
|-------|---------|--------------|
| **OPORTUNIDADE** | recrutador, gestor, empresa ou alguém com um problema que o usuário resolve | resposta completa + uma porta aberta |
| **CONTEÚDO** | traz dado, discorda, complementa, corrige | a resposta mais elaborada da conversa |
| **COLEGA** | profissional de SST/RH cuja presença vale a pena | uma resposta que acrescenta algo para ele |
| **APOIO** | "ótimo post", 👏, marcação de alguém | curtida e, no máximo, 3 a 8 palavras |
| **RUÍDO** | propaganda, spam, má-fé | nada, ou uma linha e acabou |

Escreva nessa ordem e pare quando o valor acabar.

## Como responder

- **Responda a pergunta de fato.** Se perguntaram como, explique como, ali mesmo. Não mande para o privado o que dava para responder em público.
- **Use o nome uma vez**, no começo, sem exclamação.
- **Acompanhe o tamanho.** Comentário de duas linhas não ganha resposta de seis.
- **Para crítica:** reconheça primeiro a parte verdadeira, com as palavras da pessoa, depois sustente o que você defende. Não apague, não fique na defensiva, não responda duas vezes na mesma conversa.
- **Para correção técnica:** se a pessoa estiver certa sobre uma NR ou item, admita e agradeça; se estiver errada, cite o item vigente com calma. Na dúvida, confira com a skill consulta-normas-sst antes de responder.
- **Para oportunidade (vaga, recrutador, empresa):** responda bem em público e feche com uma frase de abertura ("se quiser, te mando o modelo por mensagem"), nunca com um discurso de venda ou um currículo colado.
- **Para propaganda:** ignore. Responder dá alcance a ela.
- **Nunca exponha** empresa, cliente ou colega identificável ao comentar caso de acidente.

## Saída

Um bloco por grupo, cada resposta pronta para colar e já passada pela skill humanizer-ptbr:

```
RESPOSTAS  ·  14 comentários  ·  1 OPORTUNIDADE, 2 CONTEÚDO, 3 COLEGA, 7 APOIO, 1 RUÍDO

OPORTUNIDADE
@Fulana (RH, indústria) - "como vocês fazem a integração de terceiros?"
> Fulana, o que mudou pra nós foi exigir a APR da contratada antes do primeiro
> dia, não no primeiro dia. Se quiser, te mando o checklist que uso.

CONTEÚDO
@Beltrano - discorda da frequência do DDS
> Faz sentido no seu cenário. Aqui funcionou porque a equipe é pequena; com
> 80 pessoas por turno eu faria diferente.

APOIO  (curtir; responder só os três primeiros)
@... "Excelente!" -> Valeu, Ciclano.

RUÍDO  (1)
Ignorado: anúncio de curso. Responder dá alcance.
```

Nada é publicado sem o "sim" do usuário. Ele cola as respostas.