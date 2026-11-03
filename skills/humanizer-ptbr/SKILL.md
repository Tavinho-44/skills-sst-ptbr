---
name: "humanizer-ptbr"
description: "Tira as marcas de texto de IA de posts e textos em português do Brasil (LinkedIn e SST), mantendo termos técnicos, NRs, citações e dados intactos. Use ao pedir para humanizar, naturalizar, deixar menos robótico ou tirar cara de IA de um texto, ou depois de redigir um post. Traz dois scripts Python opcionais (limpar e dar nota) e funciona sem eles."
---

# Humanizer PT-BR

Revisa um texto em português para que soe escrito por uma pessoa: um técnico de segurança experiente falando com colegas de profissão, não um assistente de IA nem um folheto institucional. Use esta skill no lugar do humanizer original (baseado em inglês) para textos em português.

## Ferramentas (rode, não avalie no olho)

A pasta `scripts/` tem dois programas Python que usam só a biblioteca padrão, rodam na sua máquina e não enviam o texto para lugar nenhum. Quando houver shell e Python disponíveis, use-os; sem eles, aplique as mesmas regras à mão.

Comandos, a partir da pasta desta Skill. No Windows use `python`; em Linux e macOS, `python3`:

```bash
python scripts/humanizar.py rascunho.txt -o limpo.txt --relatorio   # limpa e mostra o que mudou
python scripts/detectar.py rascunho.txt limpo.txt                   # nota antes e depois
```

**Como passar o texto:** grave-o num arquivo `.txt` em UTF-8 e passe o caminho (é o jeito mais seguro, principalmente no Windows). Outra opção é a entrada padrão com `-`: `python scripts/humanizar.py - < rascunho.txt` (no PowerShell, `Get-Content rascunho.txt -Encoding utf8 | python scripts/humanizar.py -`). Se a Skill estiver instalada em outra pasta, use o caminho completo de `scripts/humanizar.py`.

**Códigos de saída:** `0` quando o programa rodou, inclusive se o texto não foi aprovado (o veredito aparece na tela). `2` só para erro de uso: arquivo inexistente, texto vazio, arquivo que não é UTF-8 ou léxico inválido. A mensagem de erro diz o que corrigir.

- **humanizar.py** apaga caracteres invisíveis, apaga muletas seguras ("é importante ressaltar que", "vale lembrar que", "em suma") e troca formalidades ("utilizar" → "usar", "a fim de" → "para"). Quanto à tipografia: troca aspas curvas por retas, e o travessão só quando houver **dois ou mais** no texto (um só é mantido, conforme a regra abaixo). Travessão no começo da linha vira hífen. Palavras como "fundamental", "crucial", "jornada" e os clichês de SST são só **sinalizados**, porque trocar automaticamente quebraria a concordância ou o sentido. "Utilizado(a)" também é só sinalizado: "EPI usado" pode ser lido como EPI de segunda mão.
- **Nunca é alterado:** URLs, e-mails, hashtags, trechos entre aspas duplas (retas, curvas ou « », mesmo quebrando linha, desde que sem linha em branco no meio; aspas simples não protegem), linhas iniciadas por `>` e blocos de código. Citação de norma e fala vão entre aspas para ficarem protegidas. Palavras que mudam o sentido quando trocadas ("alavanca", "alavancar", "visando", "concluindo") são só sinalizadas. Uma muleta depois de "não" ("não é importante ressaltar que") também só é sinalizada.
- **Aspas curvas em texto formal:** em laudo, ofício, documento com ABNT ou qualquer texto que precise manter aspas curvas, use `--manter-aspas-curvas` no humanizar.py e `--aceitar-aspas-curvas` no detectar.py. Sem isso, as aspas curvas **fora** de citações viram retas.
- **detectar.py** dá uma nota de 0 a 100 em cinco critérios: VARIAÇÃO (tamanho das frases), CONCRETUDE (números, NRs, siglas, nomes), MULETAS, TIPOGRAFIA (invisíveis, travessões, aspas curvas) e VOZ (primeira pessoa e estruturas de IA). Aprovado = nota 70+ e nenhum critério abaixo de 55. Citações entre aspas não contam como muleta.
- **Usos técnicos de SST não são falsos positivos.** O léxico tem uma lista de exceções (`excecoes` em `scripts/lexico-ptbr.json`) para casos como "jornada de trabalho", "desbloquear" um equipamento ou energia, "mergulhar" em trabalho de mergulho, "serviços essenciais", "ecossistema" em sentido ambiental, "ensino fundamental" e "transformador" elétrico. Esses usos não são sinalizados nem contados. Se faltar um caso, acrescente uma exceção ao JSON.
- O léxico fica em `scripts/lexico-ptbr.json` e pode ser editado. Nunca coloque siglas, NRs ou termos técnicos nele.

Ordem: rode `humanizar.py`, reescreva à mão os termos e estruturas sinalizados, rode `detectar.py` para comparar. Se não aprovar, corrija o critério mais fraco e repita; duas rodadas é normal. Se precisar de cinco, o problema é o rascunho, não o acabamento.

Seja honesto sobre a nota: são heurísticas locais, não um detector comercial. Nunca diga ao usuário que o texto é "indetectável". Mostre sempre o texto junto com a nota, nunca só a nota.

Confira sempre o resultado do script contra o original antes de entregar: o script não entende sentido, só padrões.

## Regra de ouro

Mude a forma, nunca o conteúdo técnico. Preserve exatamente: números de NR e itens, citações e trechos entre aspas, dados e fontes, termos técnicos (EPI, EPC, CA, APR, PT, LOTO, SEP, GRO/PGR), nomes de campanhas e hashtags. Se uma frase técnica estiver estranha, sinalize em vez de reescrever o sentido. Não reescreva a redação de uma norma citada.

## Marcas de IA a remover

### Expressões-muleta
"É importante ressaltar/destacar", "vale ressaltar", "vale lembrar", "nesse sentido", "dessa forma", "diante disso", "em suma", "em resumo", "no cenário atual", "nos dias de hoje", "cada vez mais", "não é segredo que", "sem dúvida", "de fato". Corte ou troque por uma ligação natural.

### Vocabulário inflado
"Fundamental", "crucial", "essencial", "primordial", "robusto", "potencializar", "alavancar", "jornada", "desempenha um papel", "transformador", "sinérgico", "ecossistema". Troque pelo concreto: em vez de "a APR desempenha um papel fundamental", "a APR é onde o risco aparece antes de virar acidente". Exceção: quando a palavra é termo técnico ou legal ("jornada de trabalho", "serviços essenciais", "transformador de potência"), mantenha.

### Estruturas repetitivas
- "Não é sobre X, é sobre Y" / "Mais do que X, é Y" / "Não apenas X, mas também Y": no máximo uma por texto, de preferência nenhuma.
- Listas sempre de três itens ("segurança, saúde e bem-estar"). Varie: dois, quatro ou um só.
- Perguntas retóricas empilhadas ("E você? Já parou para pensar? O que faria?"). Deixe uma.
- Abertura com "Imagine..." ou "Você sabia que...".
- Fecho moralista genérico ("Afinal, segurança é responsabilidade de todos.").

### Clichês de SST
"Segurança em primeiro lugar", "segurança não é custo, é investimento", "o EPI salva vidas", "acidente não acontece por acaso", "a vida não tem preço", "voltar para casa em segurança" usado como bordão. Se a ideia for necessária, diga de um jeito que só quem está no campo diria.

### Pontuação e formatação
- Travessão: **no máximo um por texto**. Com um só, o script o mantém. Com dois ou mais, ele troca todos por vírgula (ou ponto, dois-pontos); confira o resultado, porque um travessão duplo que abre e fecha um aposto pode pedir ajuste à mão. O detector tolera um travessão e penaliza os demais, a mesma regra.
- Dois-pontos anunciando revelação ("O resultado? Surpreendente:"), "Spoiler:".
- Emoji em toda linha ou emoji decorativo. Máximo 1 a 3, com função.
- Negrito ou maiúsculas espalhados para ênfase.

### Gramática que soa artificial
- Gerundismo ("vamos estar enviando").
- Voz passiva onde a ativa é mais natural ("foi realizada uma inspeção" → "inspecionamos").
- Frases todas do mesmo tamanho. Misture curtas e médias.
- Formalidade excessiva para o LinkedIn ("outrossim", "destarte", "no que tange").

## O que acrescentar

- Detalhe concreto no lugar de abstração: a situação, o equipamento, o horário, o que foi dito. Só use detalhe que o usuário informou; nunca invente número, caso ou vivência.
- Primeira pessoa quando o autor viveu aquilo.
- Uma opinião clara, em vez de "há vários pontos de vista".
- Linguagem de campo, sem gíria excessiva.

## Entrega

1. O texto revisado, pronto para colar.
2. Lista curta das principais mudanças (no máximo 6 itens, trecho antes → depois).
3. Se algo técnico parecer errado (norma, item, dado), um aviso separado. Se o usuário tiver a Skill `revisao-tecnica-post-sst` (opcional), sugira rodá-la; sem ela, indique conferir a norma no texto oficial antes de publicar.

Não aumente o texto: a versão final deve ficar do mesmo tamanho ou menor.
