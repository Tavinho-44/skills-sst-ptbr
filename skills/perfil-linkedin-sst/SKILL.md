---
name: "perfil-linkedin-sst"
description: "Nota rápida (0 a 100, em 10 dimensões) e reescrita do perfil do LinkedIn de um profissional de Segurança do Trabalho: título, Sobre, experiências, destaques, banner. Use quando alguém de SST pedir \"avalia meu perfil\", \"melhora meu LinkedIn\", \"reescreve meu título\", \"arruma meu Sobre\" ou colar o perfil perguntando como está. Para outras profissões, ou para diagnóstico de carreira, pesquisa de mercado, benchmarking e estratégia de posicionamento, use a skill linkedin-professional-intelligence (repositório próprio)."
---

# Perfil do LinkedIn para SST

Adaptado de li-profile (linkedin-agent-skill, Jake Schincariol, MIT) para português e para quem trabalha com Segurança do Trabalho. O aviso de licença MIT está em `LICENCA-linkedin-agent-skill.txt`, nesta pasta.

Regras comuns: siga `referencia/linkedin-regras.md` (a Skill escreve, o usuário cola; nada inventado) e `referencia/privacidade.md` (dados de terceiros). As NRs que entram no perfil são as que o usuário informou, com o treinamento e a data que ele deu. Se for preciso citar item, carga horária, validade ou vigência de norma, siga `referencia/regras-de-fonte.md` (Regra A): só com origem conferida; sem ela, cite a NR sem o item. Os arquivos de `referencia/` ficam na pasta desta Skill. Abra cada um pelo caminho, com a ferramenta de leitura, sem depender de busca por arquivos: a pasta da Skill pode estar oculta e não aparecer na busca.

Perfil não é currículo. O currículo responde "o que você já fez". O perfil responde, em uns quatro segundos, "vale a pena chamar essa pessoa?", a partir do título e das duas primeiras linhas do Sobre. E, para quem busca oportunidade, ele também precisa ser encontrado: recrutadores buscam por termos como "Técnico em Segurança do Trabalho", "NR-10", "NR-35", "SESMT", e esses termos têm que estar no título e nas experiências.

Esta skill faz a nota e a reescrita. Para o trabalho completo (mercado, referências, posicionamento, plano de 90 dias), existe a skill linkedin-professional-intelligence (repositório próprio, ainda não publicado); as duas usam as mesmas 10 dimensões e os mesmos pesos, então a nota de uma vale na outra.

## Entrada

Peça ao usuário para colar: título, Sobre, cargo atual e as duas últimas experiências, e dizer se tem banner, destaques e recomendações. Um print do topo do perfil basta para a primeira rodada. Não entre no LinkedIn em nome dele.

Se houver informações do usuário já conhecidas na conversa (formação, NRs, empresas, áreas de atuação), use-as, mas nunca invente certificação, número ou resultado.

## Dar a nota

Leia `rubrica.json` nesta pasta: 10 dimensões, 100 pontos, cada uma com o que vale nota cheia. Avalie todas, mostre a tabela e o total. Seja honesto: a maioria dos perfis fica entre 30 e 50 na primeira avaliação, e uma nota generosa não ajuda ninguém. Dimensão que não deu para ver (sem print da foto, por exemplo) fica "não avaliada", fora do total.

A nota é um índice desta metodologia, não uma nota do LinkedIn.

```
NOTA DO PERFIL  38/100

  foto e banner                  4/10   foto boa; banner padrão
  título                         4/15   só cargo e empresa
  Sobre                          3/15   abre com "profissional dedicado"
  experiências                   8/20   atribuições, sem resultado
  competências e certificações   3/10   genéricas; NRs não cadastradas
  ...
```

## Reescrever, nesta ordem

Corrija da dimensão que mais perde pontos para a que menos perde. Não reescreva tudo de uma vez: o usuário precisa colar cada parte.

**Título.** Fórmula: `{função} | {especialidades buscáveis: NRs, setores} | {uma prova} | {o que busca ou oferece}`. Exemplo de forma (não de conteúdo): "Técnico em Segurança do Trabalho | NR-10 · NR-12 · NR-35 | Indústria, agro e setor elétrico | {prova}". Dê três opções, com a contagem de caracteres. O limite de caracteres muda: confira o que o campo de edição do LinkedIn mostra em vez de confiar num número fixo.

**Sobre, duas primeiras linhas.** No celular, o resto fica atrás do "ver mais". Essas linhas dizem em que contexto o usuário trabalha e o que muda quando ele está lá. Nada de "profissional dedicado", "apaixonado por", "focado em resultados", nem bio em terceira pessoa.

**Sobre, corpo.** Escrito para um leitor (gestor, recrutador, colega), em primeira pessoa. Estrutura: o tipo de risco e de operação com que trabalha, o que faz a respeito (PGR, APR, PT, investigação, treinamentos), uma prova com número, e como entrar em contato. Curto: uns quatro parágrafos.

**Experiências.** Cada cargo com uma linha de escopo (tipo de empresa, setor, tamanho da equipe ou da obra) e dois a três resultados com número, não lista de atribuições. "Elaborei APRs" é atribuição; "reduzi de X para Y os desvios de EPI em 6 meses" é resultado. O verbo segue o que ele fez de fato: participei, executei, liderei ou respondi tecnicamente. Cargos com mais de dez anos viram uma linha.

**Competências e certificações.** As três primeiras competências são as do cargo que ele quer. Treinamentos de NR entram em Licenças e certificados, com instituição e data.

**Destaques e recomendações.** Três destaques: o melhor post, uma prova de trabalho (um material, um treinamento, um certificado relevante) e a forma de contato. Recomendação a skill não escreve em nome de terceiros: redija o pedido para duas ou três pessoas, sugerindo que citem um resultado concreto.

**Banner.** Uma frase de posicionamento e uma forma de contato, na identidade visual do usuário se ele tiver uma. O banner padrão é o sinal mais claro de perfil abandonado.

Onde faltar um número que o usuário não deu, deixe `{{seu número}}` e avise. Não invente.

## Saída

Tabela de notas e, em seguida, as reescritas em blocos prontos para colar, na ordem de correção, cada uma passada pela skill humanizer-ptbr. No fim, dê a nova nota com honestidade: se chegar a 82 e não a 98, diga 82 e o que falta (normalmente recomendações, banner e frequência de posts, que reescrita nenhuma cria).

Nada é salvo no LinkedIn por esta skill. O usuário cola cada parte.
