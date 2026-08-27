# Resultados - Aula 04

## Exercício 1 - Análise do Elitismo

### Execução com elitismo

```text
============================================================
RESULTADOS — ALGORITMO GENÉTICO
============================================================
Elitismo utilizado: True
Melhor rota encontrada: [0 4 1 6 9 7 2 8 3 5]
Custo base da rota: 290.31
Penalidade: 0.00
Fitness final: 290.31
Tempo de execução: 2212.12 ms
============================================================
```

### Execução sem elitismo

```text
============================================================
RESULTADOS — ALGORITMO GENÉTICO
============================================================
Elitismo utilizado: False
Melhor rota encontrada: [8 7 2 9 6 1 4 0 5 3]
Custo base da rota: 290.32
Penalidade: 0.00
Fitness final: 290.32
Tempo de execução: 1508.97 ms
============================================================
```

### Considerações

Nesse exercício, alteramos a variável `USAR_ELITISMO` para comparar o comportamento do algoritmo genético com e sem a preservação do melhor indivíduo.

Com o elitismo ativado, o algoritmo encontrou uma rota com custo de `290.31`, sem nenhuma penalidade. Já sem o elitismo, foi encontrada uma rota diferente, mas com um custo muito próximo, de `290.32`, também sem penalidade.

A diferença entre os dois resultados foi pequena. Mesmo assim, foi possível perceber a importância do elitismo, pois ele garante que a melhor solução encontrada seja preservada para a próxima geração. Sem elitismo, essa solução pode ser modificada ou perdida durante o processo de reprodução e mutação.

Nesse teste específico, os dois métodos chegaram a resultados praticamente iguais, mostrando que o elitismo não necessariamente gera uma diferença grande em todas as execuções, mas ajuda a manter as melhores soluções encontradas ao longo das gerações.

## Exercício 2 - Penalidade de SLA

### Output da execução

```text
============================================================
EXERCÍCIO 2 — PENALIDADE DE SLA
============================================================
Rota testada: [0 1 2 3 4 5]
Custo Total (Com Penalizações de SLA): 1160.00 ms
============================================================
```

### Considerações

Nesse exercício, implementamos uma penalidade para representar o cumprimento de um SLA de latência. O limite definido foi de `50 ms` por enlace.

Quando a latência de um enlace ultrapassa esse limite, é adicionada uma penalidade de `1000 ms` ao custo da rota. Dessa forma, o algoritmo passa a considerar não somente o custo normal da rota, mas também as violações do SLA.

Na execução realizada, a rota testada foi `[0 1 2 3 4 5]` e o custo total, considerando as penalizações, foi de `1160.00 ms`.

Com isso, entendemos que as penalizações são uma forma de fazer o algoritmo evitar soluções que não atendam às restrições definidas no problema.

## Exercício 3 - Balanceamento de Carga em Servidores

### Output da execução

```text
============================================================
EXERCÍCIO 3 — BALANCEAMENTO DE CARGA
============================================================
Melhor alocação: [2 1 2 2 0 3 3 0 0 2 0 3 3 3 1 2 1 2 1 1]
Makespan final: 137.00 segundos

Carga por servidor:
Servidor 0: 134.00 segundos
Servidor 1: 136.00 segundos
Servidor 2: 134.00 segundos
Servidor 3: 137.00 segundos
============================================================

DISTRIBUIÇÃO DAS TAREFAS:

Servidor 0:
Tarefas: [4, 7, 8, 10]
Tempos: [15, 45, 60, 14]

Servidor 1:
Tarefas: [1, 14, 16, 18, 19]
Tempos: [35, 25, 42, 5, 29]

Servidor 2:
Tarefas: [0, 2, 3, 9, 15, 17]
Tempos: [12, 40, 8, 31, 33, 10]

Servidor 3:
Tarefas: [5, 6, 11, 12, 13]
Tempos: [22, 19, 28, 50, 18]
```

### Considerações

Nesse exercício, o objetivo foi distribuir 20 tarefas entre 4 servidores tentando deixar as cargas o mais equilibradas possível.

O principal objetivo era minimizar o `makespan`, que representa o maior tempo de processamento entre os servidores. Na solução encontrada, o servidor 0 ficou com `134 segundos`, o servidor 1 com `136 segundos`, o servidor 2 com `134 segundos` e o servidor 3 com `137 segundos`.

Dessa forma, o `makespan` final foi de `137 segundos`.

As cargas ficaram próximas umas das outras, mostrando que o algoritmo conseguiu realizar uma distribuição equilibrada das tarefas. O servidor 3 ficou com a maior carga, com `137 segundos`, sendo esse o valor utilizado como makespan.

Com esse exercício, entendemos como um algoritmo genético pode ser utilizado para distribuir tarefas entre diferentes servidores buscando evitar que um servidor fique muito mais carregado que os outros.

## Desafio de Fechamento - SD-WAN Zero-Trust

### Output da execução

```text
=================================================================
DESAFIO DE FECHAMENTO — SD-WAN ZERO-TRUST
=================================================================
Origem: 0
Destino: 11
Melhor rota encontrada: [0, 11]
Latência total: 18.00 ms
Perda de pacotes total: 4.88 %
Penalidade de segurança: 0.00
Fitness final: 66.80
Tempo de execução: 438.87 ms
=================================================================

REPUTAÇÃO DOS NÓS DA ROTA:

Nó 0: Reputação = 92.52 → CONFIÁVEL
Nó 11: Reputação = 66.30 → CONFIÁVEL
```

### Relatório técnico

O algoritmo selecionou a rota `[0, 11]`, conectando diretamente o nó de origem `0` ao nó de destino `11`.

A rota apresentou latência total de `18.00 ms` e perda de pacotes total de `4.88%`. Como os nós utilizados possuem reputação superior a `50`, não foi aplicada nenhuma penalidade de segurança.

O nó `0` apresentou reputação de `92.52`, sendo considerado confiável. O nó `11` apresentou reputação de `66.30`, também sendo considerado confiável.

A penalidade de segurança não foi aplicada porque nenhum dos nós pertencentes à rota possui reputação inferior a `50`. Dessa forma, a rota direta foi selecionada por apresentar uma combinação adequada de baixa latência, baixa perda de pacotes e segurança.

O fitness final obtido foi de `66.80`. Nesse caso, o algoritmo conseguiu chegar diretamente ao destino sem precisar passar por outros nós que poderiam apresentar maior risco de segurança ou aumentar a latência da comunicação.

### Considerações

Com esse desafio, entendemos como diferentes critérios podem ser considerados ao mesmo tempo na escolha de uma rota. Além da latência e da perda de pacotes, o algoritmo também considera a reputação dos nós para evitar caminhos que apresentem risco de segurança.

A penalização de segurança faz com que uma rota que passe por um nó com reputação inferior a `50` tenha seu fitness aumentado, tornando essa opção menos interessante para o algoritmo.

No resultado obtido, a rota `[0, 11]` não apresentou penalização de segurança e teve uma latência baixa. Isso mostra que o algoritmo conseguiu encontrar uma rota que atende aos critérios de desempenho e segurança definidos no problema.
