---
name: "programa-desenergizacao-nr10"
description: "Monta o roteiro de desenergização e reenergização (programa de manobra) de um equipamento elétrico nomeado, pela sequência da NR-10, e a justificativa quando alguém propõe trabalho energizado. Entrevista com uma pergunta por vez, recusa pedido vago e marca [LACUNA] em vez de inventar ponto de seccionamento, aterramento ou energia incidente. Use ao pedir roteiro de manobra, bloqueio elétrico, liberação de serviço elétrico, desligamento programado ou linha viva. Para PT de altura, espaço confinado, trabalho a quente, escavação ou içamento, use permissao-de-trabalho."
---

# Programa de desenergização (NR-10)

Roteiro de campo para levar um equipamento elétrico **nomeado** do estado energizado à condição segura de trabalho e de volta. Princípio: **desenergizar primeiro**. Trabalho energizado é exceção que precisa de justificativa, e EPI é sempre a última camada, nunca o controle principal.

O resultado é um **rascunho** para revisão e assinatura. Quem libera o serviço é o responsável autorizado pela empresa; a Skill apoia a decisão, não a substitui. Não presuma a profissão de quem pede nem de quem assina.

Regras comuns, que esta Skill segue sem repetir aqui (leia quando for usar):

- `referencia/regras-de-fonte.md`: Regra A para toda citação de norma (✅ Base local, 🌐 Fonte oficial, ⚠️ Não conferido).
- `referencia/privacidade.md`: pessoas por função, nunca por nome; o que não pedir nem repetir.
- `referencia/glossario-sst.md`: termos e grafia padronizada.
- `referencia/modelo-de-saida.md`: estrutura do roteiro entregue.

Os arquivos de `referencia/` ficam na pasta desta Skill. Abra cada um pelo caminho, com a ferramenta de leitura, sem depender de busca por arquivos: a pasta da Skill pode estar oculta e não aparecer na busca.

## 1. Entrevista (uma pergunta por vez)

Não redija o roteiro sem estas respostas. Faça uma pergunta por vez e espere a resposta.

1. **Equipamento nomeado:** tipo, identificação e tensão (por exemplo, "alimentador 13,8 kV AL-02 até a chave fusível CF-15" ou "quadro QGBT-3, 380 V, gaveta 5"). Recuse "a subestação", "o painel", "a rede": peça o equipamento e o trecho.
2. **Tensão e sistema:** baixa, média ou alta tensão; Sistema Elétrico de Potência (SEP) ou instalação de consumidor. Isso define as zonas de risco e controlada, o aterramento e quem pode autorizar.
3. **Todos os pontos de seccionamento**, inclusive fontes de retorno (gerador, nobreak, banco de capacitores, transformador auxiliar, sistema fotovoltaico, indução de linha paralela), e onde entra o aterramento temporário. Roteiro sem a lista de pontos não é montado.
4. **Tipo de serviço:** trabalho em circuito desenergizado, energização controlada para teste ou ensaio, ou os dois. Mantenha separados: a liberação para trabalhar não autoriza energizar para teste, e o teste exige retirada do pessoal e controle próprio.
5. **Desenergizar ou trabalhar energizado?** O padrão é desenergizado. Se for energizado, siga a seção 4.
6. **Quem:** executantes autorizados, responsável pela liberação e, quando houver, centro de operação ou concessionária. Por função, sem nome.
7. **Data prevista do serviço:** é a data de referência da Regra A e decide qual redação da NR-10 vale (seção 2).

Devolva um resumo das respostas e confirme antes de montar. Dado ausente vira `[LACUNA]`, nunca ponto de seccionamento, aterramento ou valor inventado.

## 2. Qual redação da NR-10 vale

A NR-10 tem duas redações em circulação: a atual e a nova redação dada pela Portaria MTE nº 737/2026, que muda a numeração e a ordem das etapas. Antes de citar, confira pela Regra A qual delas está vigente na data de referência e diga qual usou.

| Tema | Redação atual | Nova redação |
|---|---|---|
| Prioridade da desenergização | 10.2.8.1 e 10.2.8.2 | 10.5.1 |
| Medidas seguintes quando não der para desenergizar, com EPI por último | 10.2.8.2.1 e 10.2.9.1 | 10.5.3 (ordem de prioridade da NR-01), 10.5.4 e 10.11.1 |
| Sequência de desenergização | 10.5.1, alíneas a a f | 10.13.1, alíneas a a g |
| Sequência de reenergização | 10.5.2, alíneas a a e | 10.13.2, alíneas a a g |
| Alteração das etapas por profissional legalmente habilitado, com justificativa formalizada | 10.5.3 | 10.13.4 |
| Instalação desligada com possibilidade de energização | 10.5.4 | 10.5.2 |
| Requisitos de serviço em instalação energizada | 10.6 (inclusive 10.6.2, zona controlada) e, em AT e SEP, 10.7 (inclusive 10.7.4 e 10.7.6) | capítulo 10.14 (inclusive 10.14.1) |
| Serviço energizado não realizado individualmente | 10.7.3 (AT e SEP) | 10.14.2 (média e alta tensão e SEP) |
| Bloqueio do religamento automático na zona de risco | 10.7.7 (AT) | 10.14.3 (média e alta tensão) |
| Raios das zonas de risco e controlada | Anexo II | Anexo II |

A tabela diz **onde procurar**, não substitui a leitura: a marca de cada citação é da conferência feita na conversa, pela ordem da Regra A (base local, fonte oficial, pedido do trecho). Sem acesso ao texto, a citação sai ⚠️ e o roteiro descreve a etapa sem número de item.

Diferenças que mudam o roteiro na nova redação (confirme no texto): a constatação de ausência de tensão vem antes do impedimento de reenergização e é repetida antes do aterramento; entram a proteção contra os efeitos do arco e a delimitação e sinalização da área; na reenergização, a retirada da delimitação vem primeiro.

## 3. Roteiro de desenergização e reenergização

Um passo por linha, cada um com: ponto ou equipamento, ação, quem executa, quem confere, horário e rubrica. Siga a sequência da redação vigente (seção 2), na ordem da norma, sem pular etapa.

Boas práticas que completam a norma (diga que são boa prática, não obrigação legal):

- Bloqueio individual: um cadeado e uma etiqueta por executante.
- Ausência de tensão: testar o detector antes e depois da medição, em todas as fases e em todos os pontos de trabalho.
- Aterramento temporário com equipotencialização dos dois lados do ponto de trabalho quando houver mais de uma fonte possível.

Sem acesso ao texto da norma (Regra A sem base local e sem web), não monte a ordem de memória: siga o procedimento de manobra da empresa, se o usuário tiver, marque a sequência ⚠️ e peça o trecho da NR-10. Em qualquer redação, na reenergização ninguém fica na zona controlada nem sobra ferramenta antes de retirar aterramento, sinalização e bloqueios.

Barre e aponte como falha: serviço liberado sem constatação de ausência de tensão, ou sem aterramento onde o procedimento exige. O roteiro não fecha com essa falha.

Se o usuário quiser mudar, substituir ou eliminar uma etapa, lembre que a norma só admite isso por profissional legalmente habilitado, autorizado, com justificativa técnica formalizada antes e o mesmo nível de segurança (seção 2). Registre a justificativa como `[LACUNA]` até ela existir.

## 4. Se for proposto trabalho energizado

1. **Justificativa:** por que não dá para desenergizar (impedimento técnico ou risco maior ao desligar). Prazo, produção ou conveniência não servem; com justificativa fraca, volte ao roteiro desenergizado.
2. **Requisitos da NR-10 para instalações energizadas e para AT e SEP** (linhas da tabela da seção 2), conferidos pela Regra A: procedimento específico, ordem de serviço, análise de risco, trabalhadores autorizados e capacitados, equipe (o serviço não é feito individualmente nos casos da seção 2), zonas de risco e controlada pela tensão (Anexo II) e bloqueio do religamento automático na zona de risco, nas tensões que a redação vigente indica (AT na atual; média e alta tensão na nova).
3. **Método** (à distância, ao potencial, ao contato) e controles na ordem de prioridade da NR-01, item 1.4.1, alínea g: eliminação, proteção coletiva (isolamento de partes vivas, barreiras, bloqueio do religamento), medidas administrativas e, por último, EPI. Confira o item pela Regra A.
4. **Vestimenta e EPI contra arco:** use a energia incidente do estudo de arco elétrico da instalação, se existir. Se não existir, `[LACUNA]`; nunca invente valor de cal/cm².

## 5. Revisão antes de entregar

Revise como encarregado de manobra experiente e como fiscal:

1. **Omissões primeiro**, sem olhar o checklist: o que um profissional competente teria posto aqui e não está? Toda omissão vira `[LACUNA]` ou pergunta ao usuário.
2. Depois confira: toda fonte isolada, inclusive retorno; ausência de tensão em todos os pontos; aterramento onde exigido; reenergização na ordem da norma; teste separado da liberação; responsável em cada passo; redação da NR-10 declarada.
3. Confira cada citação pela Regra A. Se a Skill `conferencia-documento-sst` estiver instalada (opcional), use-a no roteiro pronto.

## 6. Entrega

- **Padrão: Markdown**, na estrutura de `referencia/modelo-de-saida.md`.
- **Word (.docx), se o usuário pedir** e a conversa tiver ferramenta para isso: mesma estrutura, com os campos a preencher entre colchetes (`[Empresa]`, `[CNPJ]`, `[Unidade]`) destacados para o usuário achar. Sem ferramenta de Word, entregue o Markdown e diga que pode ser colado no editor.
- Se a empresa ou o cliente tiver formulário próprio de manobra ou liberação, preencha o dele em vez de criar outro.
- Sem nome de trabalhador nem dado de saúde: campos em branco, pessoas por função.
- Feche com as pendências (`[LACUNA]` e citações ⚠️) e com a linha: o documento é rascunho de apoio; quem libera o serviço é o responsável autorizado.
