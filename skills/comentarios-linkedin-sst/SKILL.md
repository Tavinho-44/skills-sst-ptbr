---
name: "comentarios-linkedin-sst"
description: "Escreve comentários para posts de outras pessoas no LinkedIn (SST, RH, indústria) que soam como profissional com opinião. Use ao colar um post pedindo comentário ou uma rodada de comentários."
---

# Comentários no LinkedIn

Adaptado de li-comment (linkedin-agent-skill, Jake Schincariol, MIT) para português e Segurança do Trabalho.

Comentar é a ação de maior retorno no LinkedIn e a mais fácil de fazer mal. Um comentário bom num post com 400 reações é visto por mais gente que muitos posts do próprio autor. Um comentário genérico não é visto por ninguém e ainda tira credibilidade.

Não é para responder comentários no post do próprio usuário (para isso, use respostas-comentarios-linkedin).

## Entrada

O usuário cola o texto do post (e, se tiver, nome e cargo de quem publicou). Print também serve. Se vier só um link que não abre, peça o texto: nunca adivinhe o que o post dizia e nunca use o navegador para varrer o feed.

## Os nove tipos de comentário

Escolha pelo que o post é. Nunca caia no tipo 9 por preguiça.

| # | Tipo | Quando | Forma |
|---|------|--------|-------|
| 1 | Acrescentar um dado | o post afirma algo que dá para reforçar com número | "Vi o mesmo em obra: dos 12 desvios do mês, 9 foram..." |
| 2 | O caso que faltou | o post está certo, mas incompleto | "Vale até {condição}. Depois disso..." |
| 3 | Discordar com respeito | o usuário acha que está errado | primeiro a concordância real, depois o ponto de divergência |
| 4 | Ampliar uma frase | uma frase do post é a melhor | cite a frase e construa em cima dela |
| 5 | A pergunta certa | o post pulou a parte difícil | uma pergunta específica, sem "fiquei curioso" |
| 6 | O relato | o usuário já fez o que o post descreve | o que aconteceu, em duas frases |
| 7 | A correção | há um erro técnico (NR revogada, item errado, dado sem fonte) | certo, curto, gentil e com certeza; cite o item da norma |
| 8 | Outra leitura | fatos certos, enquadramento errado | "Dá pra ler isso de outro jeito:" |
| 9 | Uma linha | o post não precisa de nada, só presença | até 12 palavras, verdadeira ou bem-humorada |

Para correções técnicas (tipo 7), confira a vigência da norma antes; se houver dúvida, use a skill consulta-normas-sst.

## Regras

- **2 a 4 frases.** Mais que isso parece sequestro do post; menos parece enchimento.
- **Nunca abra com** "Ótimo post", "Excelente reflexão", "Parabéns pelo conteúdo", "Muito top", "Concordo plenamente" ou o nome do autor seguido de exclamação.
- **Sem emoji na abertura.** Nada de 👏 ou 🔥 como primeiro caractere.
- **Não repita o post.** O autor sabe o que escreveu.
- **Uma ideia só.**
- **Diga a coisa específica.** Se o comentário caberia em qualquer post do tema, é ruído.
- **Discordar funciona**, desde que a concordância venha antes e seja real.
- **Nunca invente experiência.** Se o tipo 1 ou 6 pede um caso e o usuário não deu, pergunte ou escolha outro tipo.
- **Cuidado com exposição.** Não cite empresa, cliente ou colega identificável em caso de acidente ou desvio.

## Saída

Duas opções de tipos diferentes, com rótulo, e uma linha dizendo qual você postaria e por quê. Passe as duas pela skill humanizer-ptbr antes de mostrar: em comentário curto, um travessão denuncia IA mais do que em post.

```
COMENTÁRIOS  (post de @autor sobre DDS)

[6 · Relato]
Testei DDS de 5 minutos com uma pergunta só, em vez de leitura de folha. Na
segunda semana a equipe começou a trazer os próprios casos. Na primeira
ninguém falou nada.

[3 · Discordar com respeito]
Concordo que DDS lido não funciona. Mas o problema que vejo não é o formato,
é quem conduz: quando o encarregado puxa a conversa, a adesão muda.

Postaria o primeiro: é experiência própria e admite que a primeira semana não deu certo.
```

## Rodada de comentários

Se o usuário quiser comentar em vários posts, peça os 5 a 10 textos numa mensagem só e devolva um comentário para cada, num bloco. Avise se ele estiver comentando sempre nas mesmas pessoas: isso fica visível.

## Nunca

A skill escreve, o usuário publica. Não publique comentários pelo navegador em nome dele: automatizar comentários viola os termos do LinkedIn e coloca a conta em risco.