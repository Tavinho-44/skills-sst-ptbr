---
name: "comentarios-linkedin-sst"
description: "Escreve comentários para posts de outras pessoas no LinkedIn (SST, RH, indústria) que soam como profissional com opinião, sem inventar experiência nem número e sem corrigir ninguém em público sem fonte conferida. Use ao colar um post pedindo comentário ou uma rodada de comentários. Não serve para responder comentários no post do próprio usuário."
---

# Comentários no LinkedIn

Adaptado de li-comment (linkedin-agent-skill, Jake Schincariol, MIT) para português e Segurança do Trabalho. O aviso de licença está em `LICENCA-linkedin-agent-skill.txt`, nesta pasta.

Comentar costuma render mais visibilidade do que se imagina e é fácil de fazer mal. Um comentário bom num post com muitas reações pode ser visto por muita gente (observação de uso, não dado publicado pelo LinkedIn). Um comentário genérico não é visto por ninguém e ainda tira credibilidade.

Não é para responder comentários no post do próprio usuário (para isso, use `respostas-comentarios-linkedin`, também deste repositório).

## Regras comuns

Leia os arquivos da pasta `referencia/` e siga:

- `referencia/linkedin-regras.md`: a Skill escreve e o usuário comenta; nada inventado; norma em conteúdo público.
- `referencia/regras-de-fonte.md` (Regra A): toda norma, item, lei ou prazo citado num comentário.
- `referencia/privacidade.md`: sem nome de trabalhador, empresa, cliente ou obra; sem dado de saúde.

## Entrada

O usuário cola o texto do post (e, se quiser, só a função de quem publicou, sem o nome). Print também serve; ao usar o print, não repita nomes de pessoas que aparecem nele. Se vier só um link que não abre, peça o texto: nunca adivinhe o que o post dizia e nunca use o navegador para varrer o feed.

Se o tipo de comentário pedir uma vivência ou um número do usuário (tipos 1 e 6) e ele não deu, pergunte ou escolha outro tipo.

## Os nove tipos de comentário

Escolha pelo que o post é. Nunca caia no tipo 9 por preguiça. Os trechos entre `{ }` são lacunas que só o usuário pode preencher; a Skill nunca preenche com vivência ou número inventado.

| # | Tipo | Quando | Forma |
|---|------|--------|-------|
| 1 | Acrescentar um dado | o post afirma algo que dá para reforçar com um dado que o usuário tem | "No que eu vi em {situação que o usuário informou}, {dado que o usuário informou}." Sem dado do usuário e sem fonte com data, não use este tipo. |
| 2 | O caso que faltou | o post está certo, mas incompleto | "Vale até {condição}. Depois disso..." |
| 3 | Discordar com respeito | o usuário acha que está errado | primeiro a concordância real, depois o ponto de divergência |
| 4 | Ampliar uma frase | uma frase do post é a melhor | cite a frase e construa em cima dela |
| 5 | A pergunta certa | o post pulou a parte difícil | uma pergunta específica, sem "fiquei curioso" |
| 6 | O relato | o usuário já fez o que o post descreve | o que aconteceu, em duas frases, só com o que ele contou |
| 7 | A correção | há um erro técnico (NR revogada, item errado, dado sem fonte) | certo, curto, gentil e com certeza, só com fonte conferida (ver abaixo) |
| 8 | Outra leitura | fatos certos, enquadramento errado | "Dá pra ler isso de outro jeito:" |
| 9 | Uma linha | o post não precisa de nada, só presença | até 12 palavras, verdadeira ou bem-humorada |

### Tipo 7: corrigir alguém em público

Corrigir alguém em público exige a Regra A (`referencia/regras-de-fonte.md`):

1. Confira a norma antes: base local do usuário, se houver; senão, fonte oficial pela busca na web, se estiver disponível nesta conversa; senão, peça ao usuário o trecho da norma ou o PDF. Confira também a vigência na data do post ou do fato em discussão (a data de referência).
2. **✅ ou 🌐:** escreva a correção com o item e, na nota ao usuário (fora do texto do comentário), a marca de origem e a data da conferência.
3. **⚠️ (não conferido):** não escreva correção. Escreva uma pergunta que convide a pessoa a verificar ("Você consegue indicar o item da norma que sustenta isso? Quero conferir a redação vigente."). Comentário ⚠️ não é marcado como pronto para publicar.
4. Se o próprio erro for da Skill ou do usuário, é melhor não comentar do que comentar errado.
5. Corrija a afirmação, não a pessoa. Sem ironia, sem expor o autor do post.

Norma em transição: a redação aplicável é a vigente na data de referência, não a de hoje.

## Regras

- **Tamanho:** o padrão é **2 a 4 frases**. Mais que isso parece sequestro do post; menos parece enchimento. A única exceção é o tipo 9 (uma linha, até 12 palavras), que existe justamente para quando o post não pede mais que presença.
- **Nunca abra com** "Ótimo post", "Excelente reflexão", "Parabéns pelo conteúdo", "Muito top", "Concordo plenamente", "Concordo que" ou o nome do autor seguido de exclamação.
- **Sem emoji na abertura.** Nada de 👏 ou 🔥 como primeiro caractere.
- **Não repita o post.** O autor sabe o que escreveu.
- **Uma ideia só.**
- **Diga a coisa específica.** Se o comentário caberia em qualquer post do tema, é ruído.
- **Discordar funciona**, desde que a concordância venha antes e seja real.
- **Nunca invente experiência, caso, número, percentual ou estatística.** Número só se o usuário informou ou se tem fonte e data (e então a fonte vai na nota ao usuário). Sem isso, escreva sem número.
- **Cuidado com exposição.** Não cite empresa, cliente ou colega identificável em caso de acidente ou desvio.
- **Culpa:** não atribua causa a pessoa, equipe ou gestão sem evidência (ver `referencia/privacidade.md` e o vocabulário de `referencia/linkedin-regras.md`).

## Saída

Duas opções de tipos diferentes, com rótulo, e uma linha dizendo qual você postaria e por quê. Marque cada opção com a situação das citações (sem norma, ✅, 🌐 ou ⚠️). Depois de escritas, sugira passar as duas pela Skill `humanizer-ptbr` (opcional, também deste repositório): em comentário curto, um travessão denuncia IA mais do que em post. Sem ela, revise você mesmo: tire travessão, "além disso" e frases genéricas.

O exemplo abaixo é **ilustrativo**: o post, as lacunas e as respostas são fictícios, e o usuário só usa o relato (tipo 6) se for verdade para ele.

```
COMENTÁRIOS  (exemplo ilustrativo: post sobre DDS lido em voz alta)

[6 · Relato]  (precisa que você me conte o que viveu)
{Uma ou duas frases sobre o que você fez no DDS e o que aconteceu. Se você
não testou, vamos para outro tipo.}

[5 · A pergunta certa]
Quem conduz o DDS faz diferença para a equipe falar? Em que ponto o
formato deixa de ser o problema?

Postaria o 5: não depende de experiência que eu não tenho como confirmar.
Citações de norma: nenhuma.
```

O comentário final é do usuário. A Skill não escreve "como já disse" nem finge continuidade com comentários anteriores.

## Rodada de comentários

Se o usuário quiser comentar em vários posts, peça os 5 a 10 textos numa mensagem só e devolva um comentário para cada, num bloco. A Skill não guarda histórico entre conversas: se o usuário colar a lista dos últimos comentários, avise quando ele estiver comentando sempre nas mesmas pessoas, porque isso fica visível.

## Nunca

A Skill escreve, o usuário publica. Não publique comentários pelo navegador em nome dele: automatizar comentários viola os termos do LinkedIn e coloca a conta em risco.
