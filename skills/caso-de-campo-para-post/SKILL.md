---
name: "caso-de-campo-para-post"
description: "Transforma um caso vivido em campo, um DDS ou uma investigação de acidente em post de LinkedIn anonimizado, com a lição técnica em primeiro plano. Faz triagem de risco, anonimiza por categoria, não inventa fatos e entrega o texto para o usuário publicar. Use quando o usuário contar uma situação de trabalho e pedir um post, ou colar um relato, um DDS ou um relatório e pedir para virar post."
---

# Caso de campo → post de LinkedIn

O conteúdo que mais constrói autoridade em SST é a experiência real de quem trabalha na área: o que viu, o que deu errado, qual barreira faltou. Esta Skill transforma esse material bruto em post, protegendo as pessoas e as empresas envolvidas.

A Skill escreve. Quem publica é o usuário, na própria conta. A Skill nunca publica, agenda nem opera o navegador no LinkedIn.

## Regras que valem em todos os passos

Leia e siga estes arquivos da pasta `referencia/`:

- `referencia/privacidade.md`: como identificar pessoas, o que nunca pedir nem repetir, reidentificação.
- `referencia/regras-de-fonte.md` (Regra A): como citar e marcar a origem de qualquer norma.
- `referencia/linkedin-regras.md`: a Skill escreve e o usuário publica; nada inventado; norma em conteúdo público.
- `referencia/glossario-sst.md`: vocabulário sem culpa presumida.

Resumo do que isso obriga aqui:

- **Nunca pedir nem repetir** nome, apelido, CPF, RG, matrícula, data de nascimento, CID, laudo, diagnóstico ou foto reconhecível. Se o usuário colar algum desses dados, não reproduza na resposta; avise uma vez, em uma linha, que foram omitidos, e siga identificando pela função.
- **Nunca inventar fatos.** Só entra no post o que o usuário contou ou o que está no material que ele colou. Se faltar um dado (o que aconteceu antes, qual barreira existia, como terminou), pergunte. Se o usuário não souber, o post fica sem esse dado ou o escreve como pergunta em aberto. Não crie diálogo, hora, número, resultado ou consequência.
- **Nunca atribuir culpa a pessoa, equipe ou gestão sem evidência** contada pelo usuário. Descreva o que foi feito ou observado e pergunte "o que levou a isso?".

## Entrada

- Relato solto de uma situação vivida (quase acidente, desvio observado, conversa com trabalhador, auditoria).
- Um DDS que o usuário aplicou.
- Um relatório de investigação de acidente, de qualquer origem. Se foi gerado pela Skill `investigacao-acidente-trabalho` deste repositório, melhor, mas ela é opcional.

Relatório ou documento interno de empresa não vira texto de post: use só os fatos, generalizados, e nunca copie trechos (ver `referencia/privacidade.md`, seção 4).

## Passo 1: triagem (antes de escrever)

Pergunte ou verifique, e pare se algum item for problema:

- O caso está sob investigação, processo trabalhista, cível ou criminal? Se sim, não vira post agora.
- Há vítima com lesão grave ou óbito recente? Se sim, só com muito cuidado e foco total na prevenção; ofereça esperar.
- A empresa ou o contrato do usuário proíbe divulgar? Na dúvida, recomende generalizar ainda mais ou pedir autorização.
- O caso ainda é reconhecível por quem estava lá, mesmo sem nome? Se sim, generalize mais.

## Passo 2: anonimização

Remova ou altere tudo que permita identificar alguém:

- Nomes, apelidos, matrícula, função muito específica.
- Empresa, contratante, concessionária, cliente, fazenda, usina.
- Cidade, bairro, endereço, subestação, alimentador, número de poste ou de equipamento.
- Data exata: troque por período ("há alguns anos", "numa manutenção de rotina").
- Combinação que aponta para uma pessoa (função rara + setor pequeno + data + cidade): generalize pelo menos um elemento.
- Detalhes não essenciais podem ser trocados, desde que a lição técnica continue verdadeira e o usuário saiba o que foi trocado.
- Fotos: só se não mostrarem rosto, crachá, placa, logotipo ou lesão, e sem expor desvio de quem não consentiu.

**Mostre ao usuário o que foi anonimizado por categoria, nunca pelo valor.** Exemplo ilustrativo do formato:

```
Anonimizado: nome do trabalhador, nome da empresa, cidade, data exata (trocada por período), número do equipamento.
Generalizado: função (de uma função específica para "profissional de manutenção"), tipo de local.
```

Não escreva o valor original em nenhum ponto da resposta (nem para "confirmar").

## Passo 3: extrair a lição

- Qual era o perigo, qual barreira falhou ou faltou e por quê (projeto, método, procedimento, organização do trabalho, prazo, treinamento), sempre com base no que o usuário contou.
- Qual controle teria evitado, na lógica da hierarquia de controles.
- Nunca concluir com culpa do trabalhador ("ele não prestou atenção"). O foco é o sistema.
- Se a lição depende de um fato que o usuário não informou, pergunte antes de escrever.

## Passo 4: escrever o post

Formato do post (as regras estão aqui, não dependem de outra Skill). Arquétipo: **storytelling pessoal com análise técnica**.

- **Gancho** nas duas primeiras linhas, que são as que aparecem antes do "ver mais": o momento de tensão ou a frase que ficou na memória, só se for fato que o usuário contou. Ilustrativo, não copiar: "Faltavam poucos minutos para acabar o turno quando...".
- **Corpo:** a situação em 2 a 3 parágrafos curtos (1 a 3 linhas cada, uma linha em branco entre eles), depois a análise técnica: barreira que falhou ou faltou e controle correto.
- **Fecho:** a lição em uma frase e uma única pergunta ao público. Ilustrativo: "Na sua área, qual barreira mais cai quando o prazo aperta?".
- **Hashtags:** 3 a 6, de nicho (por exemplo `#SegurancaDoTrabalho`).
- **Extensão sugerida:** 150 a 230 palavras. É sugestão de leitura, não regra do LinkedIn.
- Primeira pessoa só para o que o usuário viveu. Sem emoji no início de linha, sem lista de marcadores com emoji, sem frases de efeito vazias ("Segurança é prioridade", "Aprendizado do dia").
- Sem travessão em excesso (no máximo um) e sem as marcas típicas de texto de IA.
- Nada de hora, número de pessoas, valores ou estatísticas que o usuário não tenha informado.

### Norma citada no post

Só cite NR, item ou lei se ajudar a lição e se estiver conferida pela Regra A (`referencia/regras-de-fonte.md`):

- Cada citação sai com a marca ✅ Base local, 🌐 Fonte oficial ou ⚠️ Não conferido, e a data da conferência, na lista de entrega (não dentro do texto do post).
- Citação ⚠️ **não entra no texto do post**: escreva o argumento sem o item, ou deixe o item entre colchetes para o usuário conferir. Post com item ⚠️ não é marcado como pronto para publicar.
- Sem base local e sem busca na web nesta conversa, peça ao usuário o trecho da norma ou o PDF. Não cite item de memória.
- Para NR com redação em transição, use a redação vigente na data do fato (a data de referência é a do caso, não a de hoje).

## Passo 5: entregar

1. O post pronto para copiar.
2. A lista do que foi anonimizado, por categoria.
3. Fatos que ficaram sem informação (o que o usuário pode completar), para o post não ser preenchido com invenção.
4. As citações de norma, cada uma com a marca de origem e a data (ou "sem citação de norma").
5. Estado: "Pronto para o usuário revisar" ou "Pendente", se houver ⚠️ ou dúvida de triagem.

## Próximas etapas (opcionais)

Se o repositório tiver as Skills abaixo instaladas, ofereça em uma linha; se não, o usuário faz à mão:

- **`humanizer-ptbr`**: remove as marcas de texto de IA. Sem ela, o usuário relê o texto cortando frases genéricas, travessões e listas de três.
- **`revisao-tecnica-post-sst`**: confere NRs vigentes, termos técnicos e risco de expor pessoas ou empresas. Sem ela, o usuário confere cada NR citada na fonte oficial e relê o post procurando qualquer detalhe que identifique alguém.
- Se o caso render, o usuário pode pedir o roteiro de um carrossel (texto, slide a slide) com o formato "linha do tempo do evento e onde a barreira falhou".

Quem publica é o usuário.
