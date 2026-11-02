---
name: "humanizer-ptbr"
description: "Tira as marcas de texto de IA de posts e textos em português do Brasil (LinkedIn e SST), mantendo termos técnicos, NRs e dados intactos."
---

# Humanizer PT-BR

Revisa um texto em português para que soe escrito por uma pessoa: um técnico de segurança experiente falando com colegas de profissão, não um assistente de IA nem um folheto institucional. Use esta skill no lugar do humanizer original (baseado em inglês) para textos em português.

## Ferramentas (rode, não avalie no olho)

A pasta `scripts/` tem dois programas Python sem dependências que rodam no ambiente e não enviam o texto para lugar nenhum. Quando houver shell disponível, use-os; sem shell, aplique as mesmas regras à mão.

```bash
python3 scripts/humanizar.py rascunho.txt -o limpo.txt --relatorio   # limpa e mostra o que mudou
python3 scripts/detectar.py rascunho.txt limpo.txt                   # nota antes e depois
```

- **humanizar.py** apaga caracteres invisíveis, troca travessão por vírgula, aspas curvas por retas, apaga muletas seguras ("é importante ressaltar que", "vale lembrar que", "em suma") e troca formalidades ("utilizar" → "usar", "a fim de" → "para"). Palavras como "fundamental", "crucial", "jornada" e os clichês de SST são só **sinalizados**, porque trocar automaticamente quebraria a concordância. URLs, e-mails e hashtags nunca são tocados.
- **detectar.py** dá uma nota de 0 a 100 em cinco critérios: VARIAÇÃO (tamanho das frases), CONCRETUDE (números, NRs, siglas, nomes), MULETAS, TIPOGRAFIA (invisíveis, travessões, aspas curvas) e VOZ (primeira pessoa e estruturas de IA). Aprovado = nota 70+ e nenhum critério abaixo de 55.
- O léxico fica em `scripts/lexico-ptbr.json` e pode ser editado. Nunca coloque siglas, NRs ou termos técnicos nele.

Ordem: rode `humanizar.py`, reescreva à mão os termos e estruturas sinalizados, rode `detectar.py` para comparar. Se não aprovar, corrija o critério mais fraco e repita; duas rodadas é normal. Se precisar de cinco, o problema é o rascunho, não o acabamento.

Seja honesto sobre a nota: são heurísticas locais, não um detector comercial. Nunca diga ao usuário que o texto é "indetectável". Mostre sempre o texto junto com a nota, nunca só a nota.

## Regra de ouro

Mude a forma, nunca o conteúdo técnico. Preserve exatamente: números de NR e itens, dados e fontes, termos técnicos (EPI, EPC, CA, APR, PT, LOTO, SEP, GRO/PGR), nomes de campanhas e hashtags. Se uma frase técnica estiver estranha, sinalize em vez de reescrever o sentido.

## Marcas de IA a remover

### Expressões-muleta
"É importante ressaltar/destacar", "vale ressaltar", "vale lembrar", "nesse sentido", "dessa forma", "diante disso", "em suma", "em resumo", "no cenário atual", "nos dias de hoje", "cada vez mais", "não é segredo que", "sem dúvida", "de fato". Corte ou troque por uma ligação natural.

### Vocabulário inflado
"Fundamental", "crucial", "essencial", "primordial", "robusto", "potencializar", "alavancar", "jornada", "desempenha um papel", "transformador", "sinérgico", "ecossistema". Troque pelo concreto: em vez de "a APR desempenha um papel fundamental", "a APR é onde o risco aparece antes de virar acidente".

### Estruturas repetitivas
- "Não é sobre X, é sobre Y" / "Mais do que X, é Y" / "Não apenas X, mas também Y": no máximo uma por texto, de preferência nenhuma.
- Listas sempre de três itens ("segurança, saúde e bem-estar"). Varie: dois, quatro ou um só.
- Perguntas retóricas empilhadas ("E você? Já parou para pensar? O que faria?"). Deixe uma.
- Abertura com "Imagine..." ou "Você sabia que...".
- Fecho moralista genérico ("Afinal, segurança é responsabilidade de todos.").

### Clichês de SST
"Segurança em primeiro lugar", "segurança não é custo, é investimento", "o EPI salva vidas", "acidente não acontece por acaso", "a vida não tem preço", "voltar para casa em segurança" usado como bordão. Se a ideia for necessária, diga de um jeito que só quem está no campo diria.

### Pontuação e formatação
- Travessões em excesso: no máximo um por texto; troque por vírgula, ponto ou dois-pontos.
- Dois-pontos anunciando revelação ("O resultado? Surpreendente:"), "Spoiler:".
- Emoji em toda linha ou emoji decorativo. Máximo 1 a 3, com função.
- Negrito ou maiúsculas espalhados para ênfase.

### Gramática que soa artificial
- Gerundismo ("vamos estar enviando").
- Voz passiva onde a ativa é mais natural ("foi realizada uma inspeção" → "inspecionamos").
- Frases todas do mesmo tamanho. Misture curtas e médias.
- Formalidade excessiva para o LinkedIn ("outrossim", "destarte", "no que tange").

## O que acrescentar

- Detalhe concreto no lugar de abstração: a situação, o equipamento, o horário, o que foi dito.
- Primeira pessoa quando o autor viveu aquilo.
- Uma opinião clara, em vez de "há vários pontos de vista".
- Linguagem de campo, sem gíria excessiva.

## Entrega

1. O texto revisado, pronto para colar.
2. Lista curta das principais mudanças (no máximo 6 itens, trecho antes → depois).
3. Se algo técnico parecer errado, um aviso separado sugerindo a skill revisao-tecnica-post-sst.

Não aumente o texto: a versão final deve ficar do mesmo tamanho ou menor.