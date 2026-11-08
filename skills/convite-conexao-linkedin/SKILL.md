---
name: "convite-conexao-linkedin"
description: "Escreve a nota do convite de conexão no LinkedIn (curta, dentro do limite de caracteres que o usuário informar; 200 é o valor de referência a conferir), a primeira mensagem após o aceite e até dois acompanhamentos, para SST, RH e recrutadores. O usuário envia. Use para convites e follow-ups."
---

# Convite e mensagens no LinkedIn

Adaptado de li-dm (linkedin-agent-skill, Jake Schincariol, MIT) para português e para quem trabalha com Segurança do Trabalho. O aviso de licença MIT está em `LICENCA-linkedin-agent-skill.txt`, nesta pasta.

Regras comuns: siga `referencia/linkedin-regras.md` (a Skill escreve, o usuário envia; nada inventado) e `referencia/privacidade.md` (dados de terceiros).

Use quando o usuário pedir "escreve um convite de conexão", "manda mensagem pra essa pessoa", "como eu abordo esse recrutador", "como faço o follow-up" ou estiver montando a lista de convites da semana.

A nota do convite é curta. Neste material usa-se 200 caracteres como referência, mas ⚠️ a conferir no LinkedIn: o limite pode variar conforme o tipo de conta e mudar com o tempo. Pergunte ao usuário qual limite aparece na tela dele e use esse. A primeira mensagem decide se haverá uma segunda. Nenhuma das duas é pedido de emprego nem venda.

Os arquivos de `referencia/` ficam na pasta desta Skill. Abra cada um pelo caminho, com a ferramenta de leitura, sem depender de busca por arquivos: a pasta da Skill pode estar oculta e não aparecer na busca.

## Antes de escrever, pegue o específico

Pergunte, numa mensagem só:

1. **Quem**: cargo e empresa, e o nome só se o usuário quiser usar na saudação. Peça apenas o que a nota vai usar (minimização de dados de terceiros, `referencia/privacidade.md`); não peça telefone, e-mail pessoal nem detalhes da vida da pessoa.
2. **O motivo de agora**: um post que a pessoa escreveu, algo que a empresa fez, um contato em comum, uma palestra, uma vaga publicada. "É da área" não é motivo. **Se o motivo for um post, peça que o usuário cole o texto do post** (ou o trecho). Sem o texto, não cite o que o post diz: a Skill não abre o link nem o LinkedIn, e escrever "li seu post sobre X" sem ver o post é inventar.
3. **O que o usuário quer**: trocar experiência, uma indicação, uma vaga, um contato comercial. Seja honesto internamente, mesmo que a mensagem não comece por isso.
4. **Quem o usuário é, nas palavras dele**: cargo e área que ele quer mostrar. Não presuma cidade, empresa, setor, tempo de experiência nem certificação. Use as palavras dele: "1 ano de experiência" não vira "1 ano de obra".

Se não houver motivo específico para falar com essa pessoa hoje, diga. Mensagem sem motivo é o que todo mundo manda, e é por isso que quase ninguém responde.

### Lista da semana (vários convites)

Quando o usuário trouxer uma lista de pessoas, faça uma nota diferente para cada uma, baseada no motivo de cada uma. Se para alguém não houver motivo, marque "sem gancho: pular ou mandar sem nota" em vez de inventar. Entregue a lista para o usuário revisar e enviar ele mesmo, um convite de cada vez. Guarde só o necessário de cada pessoa (cargo, empresa, motivo) e não repita dados pessoais além disso.

## A nota do convite (até o limite informado; referência: 200 caracteres)

```
{uma referência específica à pessoa} + {uma linha de quem é o usuário} + {sem pedido}
```

A nota não pede nada; ela só torna o aceite óbvio. Conte os caracteres (com espaços) e mostre a contagem. **Recontagem com margem:** contagem feita de cabeça erra. Se houver ferramenta de código nesta conversa, conte com `len()` do texto final; se não houver, conte com cuidado e deixe uma margem de pelo menos 10 caracteres abaixo do limite, para absorver erro de contagem e ajuste do usuário. Peça que o usuário confira o contador do LinkedIn ao colar. Qualquer edição na nota exige nova contagem.

Exemplo **ilustrativo e fictício** (o tema do post e o cargo são marcadores; troque pelos dados reais do usuário e do post que ele colou):

```
Li seu post sobre revisar a tarefa com a equipe antes de liberar o trabalho
e achei útil a parte do passo a passo. Sou técnico de segurança e quero
acompanhar seu conteúdo.                                          [172 caracteres; referência 200]
```

A contagem do exemplo (172) foi conferida com `len()` do texto em uma linha só, com espaços.

## A primeira mensagem, depois do aceite

Espere um dia. Então:

- **Duas a quatro frases.** Um bloco de texto vai para a lixeira.
- **Retome o que estava na nota**: a continuidade é o motivo de a nota ter sido específica.
- **Dê algo antes de pedir**: um dado, um modelo, um contato, uma resposta.
- **Um pedido, pequeno.** "Topa 15 minutos de conversa?" funciona melhor que "segue meu currículo em anexo".
- **Para recrutador ou vaga:** cite a vaga ou a área, diga em uma frase por que o usuário encaixa e pergunte qual o melhor caminho. Só use como "algo concreto" o que o usuário informou ter: NR com certificado, setor, tempo de experiência. Não invente certificação, curso, registro ou experiência para agradar o recrutador; se faltar, pergunte ou deixe `[confirmar: ...]`. Currículo só se pedirem.

## Acompanhamentos

No máximo dois. Os intervalos abaixo são **sugestão de prática**, não regra do LinkedIn nem dado de pesquisa; o usuário pode ajustá-los ao contexto.

- **Cerca de 4 dias depois**: traga algo novo. Nunca "só passando para lembrar". Sem nada novo, não há acompanhamento.
- **Cerca de 10 dias depois**: a mensagem de encerramento. Diga que não vai mais insistir, e não insista. Costuma tirar a pressão, mas sem garantia de resposta.

Depois disso, pare.

## Nunca

- Nunca invente contato em comum, escola em comum ou ter lido algo que o usuário não leu. Também não escreva que ele acompanha os posts ou conhece o trabalho da pessoa sem ele ter dito.
- Nunca abra com "Espero que esta mensagem o encontre bem" ou "Prezado(a)".
- Nunca envie convite ou mensagem, nem opere o navegador ou a conta do usuário para isso, mesmo que ele peça. Esta skill só escreve; quem envia é o usuário, pessoa por pessoa. Envio automatizado ou em massa conflita com os termos do LinkedIn (`referencia/linkedin-regras.md`, seção 1) e pode restringir a conta.
- Nunca guarde nem repita dado pessoal de terceiros além do necessário para a nota (cargo, empresa, motivo).

## Saída

A nota com a contagem de caracteres (recontada), a primeira mensagem e os dois acompanhamentos com o dia sugerido de cada um. Se a Skill `humanizer-ptbr` do repositório estiver instalada, passe os textos por ela (é opcional); sem ela, revise você mesmo: sem "Prezado(a)", sem frase de manual, sem exagero. Quem copia e envia é o usuário.