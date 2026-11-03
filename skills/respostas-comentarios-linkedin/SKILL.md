---
name: "respostas-comentarios-linkedin"
description: "Organiza e escreve as respostas aos comentários nos posts do próprio usuário no LinkedIn, separando oportunidade, conteúdo, colega, apoio e ruído. Use ao colar comentários de um post dele."
---

# Respostas aos comentários

Adaptado de li-reply (linkedin-agent-skill, Jake Schincariol, MIT) para português e Segurança do Trabalho. O aviso de licença MIT está em `LICENCA-linkedin-agent-skill.txt`, nesta pasta.

Regras comuns: siga `referencia/linkedin-regras.md` (a Skill escreve, o usuário publica; nada inventado), `referencia/privacidade.md` (pessoas e empresas) e `referencia/regras-de-fonte.md` (citação de norma, Regra A).

Use quando o usuário colar os comentários de um post dele e pedir "responde esses comentários", "o que eu falo pra essa pessoa", "alguém discordou do meu post" ou estiver lidando com crítica ou com um possível contato de trabalho nos comentários.

A conversa embaixo do post é onde o alcance se decide: cada resposta é uma nova interação, e responder cedo costuma ajudar (prática observada, não regra publicada pelo LinkedIn). Mas nem todo comentário vale o mesmo, então a skill separa antes de escrever.

## Entrada

O usuário cola os comentários, de preferência com a função da pessoa (nome só se ele quiser usar na resposta). Print serve. Não use o navegador para ler a conversa nem para responder: quem lê, copia e publica é o usuário.

Peça também, numa linha, o assunto do post original e o que o usuário **de fato** viveu ou tem pronto (caso, modelo, checklist, número). Só isso pode aparecer nas respostas como experiência dele.

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
- **Para correção técnica (Regra A):** antes de corrigir alguém em público, confira a norma segundo `referencia/regras-de-fonte.md` (base local, depois fonte oficial na web, se a busca estiver disponível; se não, peça ao usuário o trecho ou o PDF). Se a pessoa estiver certa, admita e agradeça. Se estiver errada e a citação for ✅ ou 🌐, cite o item com calma, com a data de referência. Com ⚠️ (não conferido), não corrija: escreva uma pergunta ("você viu em qual item?") ou deixe sem resposta. A Skill `consulta-normas-sst` ajuda na conferência, mas é opcional; sem ela, o caminho acima basta.
- **Nunca afirme o que o usuário não informou.** Não escreva "aqui na minha obra", "já fiz isso", "uso um checklist", "te mando o modelo" nem número de experiência se ele não disse que é verdade e que tem o material. Falta informação: use `[confirmar: ...]` ou pergunte.
- **Para oportunidade (vaga, recrutador, empresa):** responda bem em público e feche com uma frase de abertura ("se quiser, conversamos por mensagem"; oferecer material, como "te mando o modelo", só se o usuário confirmar que tem: `[confirmar: ...]`), nunca com um discurso de venda ou um currículo colado.
- **Para propaganda:** ignore. Responder dá alcance a ela.
- **Nunca exponha** empresa, cliente ou colega identificável ao comentar caso de acidente (`referencia/privacidade.md`).

### Ofensa, assédio e provocação

- **Não responda no calor.** Comentário agressivo, ameaça, discriminação ou assédio não recebe resposta imediata; o usuário espera, respira e decide depois.
- A Skill pode sugerir, como opção, uma resposta curta e fria ("Prefiro manter a conversa no assunto do post.") ou nenhuma resposta.
- Para ocultar, excluir o comentário, bloquear ou denunciar, indique que o usuário use as opções da própria plataforma (menu do comentário ou do perfil). Quem age é o usuário; a Skill não executa nada na conta.
- Ameaça ou ofensa grave: oriente o usuário a guardar prints (data, hora, link) e, se for o caso, procurar o canal de denúncia do LinkedIn ou orientação jurídica.
- Não rebata com ironia nem exponha o agressor.

## Saída

Um bloco por grupo, cada resposta pronta para colar. Se a Skill `humanizer-ptbr` do repositório estiver instalada, passe os textos por ela (é opcional). Sem ela, revise você mesmo: tire travessões em excesso, aberturas de manual ("Ótima pergunta!"), listas de três itens por reflexo e fecho de efeito; mantenha termos técnicos, NR e itens como estão.

O exemplo abaixo é **ilustrativo e fictício**: nomes, números e situações não são do usuário e não devem ser reaproveitados como vivência dele. As partes entre colchetes só entram se o usuário confirmou.

```
RESPOSTAS  ·  4 comentários  ·  1 OPORTUNIDADE, 1 CONTEÚDO, 1 APOIO, 1 RUÍDO   [exemplo ilustrativo]

OPORTUNIDADE
@Pessoa A (RH, indústria) - "como funciona a integração de terceiros?"
> Pessoa A, a ideia central é [descrição que o usuário confirmou]. Se quiser,
> [oferta que o usuário confirmou ter, ex.: te mando o modelo por mensagem].

CONTEÚDO
@Pessoa B - discorda da frequência do DDS
> Faz sentido no seu cenário. [Ponto do post que o usuário sustenta]. Em
> equipe maior, o desenho pode mudar.

APOIO  (curtir; responder só os primeiros)
@Pessoa C "Excelente!" -> Valeu, Pessoa C.

RUÍDO  (1)
Ignorado: anúncio de curso. Responder dá alcance.
```

Nada é publicado pela Skill. O usuário revisa, cola e publica as respostas na própria conta.