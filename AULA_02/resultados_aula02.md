# Resultados — AULA 02

## AC-1 Parte 1

### LAB-01 — Problema da Mochila por Enumeração Completa

Foi realizada a enumeração completa das possibilidades para o problema da mochila.

Foram utilizados 6 itens, com capacidade máxima de 5 unidades de peso.

Os itens foram:

| Item | Peso | Valor |
|---|---:|---:|
| Livro | 2 | 3 |
| Fone | 2 | 2 |
| Camiseta | 1 | 2 |
| Carregador | 2 | 3 |
| Chocolate | 1 | 1 |
| Tênis | 2 | 2 |

Como cada item pode ser escolhido ou não escolhido, existem:

`2^6 = 64`

soluções possíveis.

Resultado obtido:

- Soluções avaliadas: 64
- Melhor valor: 8
- Melhor combinação: `(1, 0, 1, 1, 0, 0)`

Itens escolhidos:

- Livro — peso 2, valor 3
- Camiseta — peso 1, valor 2
- Carregador — peso 2, valor 3

Peso total:

`2 + 1 + 2 = 5`

Valor total:

`3 + 2 + 3 = 8`

As 64 soluções são resultado de duas possibilidades para cada um dos 6 itens. Se fossem utilizados 15 itens, o espaço de busca seria:

`2^15 = 32.768`

possibilidades.

Um exemplo de problema real semelhante é a escolha de produtos para uma compra com orçamento limitado.

---

## LAB-02 — Problema do Caixeiro Viajante (TSP)

Neste laboratório foi utilizada uma abordagem de força bruta para encontrar a melhor rota no Problema do Caixeiro Viajante.

Os resultados obtidos foram:

| Número de cidades | Rotas avaliadas | Tempo (s) | Melhor custo |
|:---:|---:|---:|---:|
| 4 | 6 | 0.000101 | 80 |
| 5 | 24 | 0.000081 | 41 |
| 6 | 120 | 0.000381 | 91 |

### Melhores rotas

- 4 cidades: `(0, 1, 3, 2, 0)`
- 5 cidades: `(0, 1, 2, 3, 4, 0)`
- 6 cidades: `(0, 1, 3, 4, 5, 2, 0)`

### Reflexão

O número de rotas cresce muito mais rapidamente do que de forma linear ou quadrática. O crescimento é fatorial, seguindo a fórmula:

`(n-1)!`

Com 4 cidades são avaliadas 6 rotas, com 5 cidades são 24 e com 6 cidades são 120.

Para 10 cidades seriam avaliadas 362.880 rotas.

Usando como referência o tempo obtido para 6 cidades, de 0.000381 segundos, uma estimativa proporcional para 10 cidades seria aproximadamente:

`0.000381 × 3.024 = 1.152144 segundos`

Portanto, a estimativa é de aproximadamente 1,15 segundo.

O TSP é considerado um problema difícil porque a quantidade de possibilidades cresce rapidamente conforme o número de cidades aumenta. A força bruta pode funcionar para instâncias pequenas, mas pode se tornar inviável para problemas maiores.

---

## LAB-03 — Heurística Gulosa x Solução Ótima

Neste laboratório foram comparadas uma solução ótima, obtida por força bruta, e uma solução encontrada por uma heurística gulosa.

Foram executadas 20 instâncias.

| Instância | Solução Ótima | Solução Gulosa | Gap (%) |
|:---:|---:|---:|---:|
| 1 | 72 | 70 | 2,8 |
| 2 | 87 | 87 | 0,0 |
| 3 | 104 | 104 | 0,0 |
| 4 | 66 | 66 | 0,0 |
| 5 | 65 | 65 | 0,0 |
| 6 | 83 | 80 | 3,6 |
| 7 | 83 | 82 | 1,2 |
| 8 | 79 | 79 | 0,0 |
| 9 | 117 | 117 | 0,0 |
| 10 | 90 | 85 | 5,6 |
| 11 | 102 | 102 | 0,0 |
| 12 | 99 | 99 | 0,0 |
| 13 | 100 | 100 | 0,0 |
| 14 | 91 | 87 | 4,4 |
| 15 | 81 | 81 | 0,0 |
| 16 | 84 | 84 | 0,0 |
| 17 | 79 | 77 | 2,5 |
| 18 | 101 | 101 | 0,0 |
| 19 | 94 | 92 | 2,1 |
| 20 | 115 | 113 | 1,7 |

### Estatísticas

- Gap médio: **1,20%**
- Maior gap: **5,56%**
- Menor gap: **0,00%**

A heurística gulosa apresentou bom desempenho nas instâncias analisadas. Em várias delas, encontrou exatamente a mesma solução que a força bruta, resultando em gap de 0%.

Entretanto, a heurística gulosa não garante encontrar a solução ótima em todos os casos. Ela toma decisões locais, podendo escolher determinados itens e impedir uma combinação melhor posteriormente.

A força bruta garante a solução ótima porque testa todas as possibilidades, mas seu custo computacional cresce rapidamente com o tamanho do problema.

---

## LAB-04 — Modelagem de um Problema Real

### Problema escolhido

Foi escolhido o problema de montar uma lista de compras com orçamento limitado, buscando maximizar a utilidade dos produtos escolhidos.

Foram considerados 8 produtos. Cada produto possui um preço e uma utilidade.

A solução foi representada por uma sequência de zeros e uns:

- `0` = produto não escolhido
- `1` = produto escolhido

Como existem 8 produtos, o espaço de busca possui:

`2^8 = 256`

soluções possíveis.

### Função objetivo

O objetivo é maximizar a utilidade total dos produtos escolhidos.

### Restrição

O custo total dos produtos escolhidos não pode ultrapassar o orçamento de R$ 50,00.

### Classificação

O problema é semelhante ao Problema da Mochila (Knapsack Problem). Para poucos produtos é possível testar todas as combinações, mas o número de possibilidades cresce exponencialmente conforme novos produtos são adicionados.

Por isso, a versão geral do problema pode ser considerada computacionalmente difícil e relacionada a problemas NP-difíceis.

### Resultado da solução aleatória

A solução aleatória obtida foi:

`[0, 0, 0, 1, 0, 0, 1, 1]`

Produtos escolhidos:

- Frango — R$ 15,00 — utilidade 10
- Sabonete — R$ 4,00 — utilidade 6
- Papel higiênico — R$ 9,00 — utilidade 10

Custo total:

`R$ 28,00`

Utilidade total:

`26`

Orçamento disponível:

`R$ 50,00`

Orçamento restante:

`R$ 22,00`

A solução foi considerada **factível**, pois o custo total de R$ 28,00 não ultrapassou o orçamento disponível de R$ 50,00.

É importante destacar que a solução foi gerada aleatoriamente e, portanto, não necessariamente representa a melhor solução possível.

---

## Conclusão da AULA 02

As atividades permitiram aplicar conceitos de otimização combinatória utilizando diferentes estratégias.

Na primeira atividade, foi utilizada força bruta para encontrar a solução ótima de um problema da mochila. Na segunda, a força bruta foi aplicada ao Problema do Caixeiro Viajante, demonstrando o crescimento fatorial do número de rotas.

Na terceira atividade, uma heurística gulosa foi comparada com a solução ótima. Os resultados mostraram que a heurística conseguiu encontrar soluções muito próximas da ótima, com gap médio de apenas 1,20% nas 20 instâncias analisadas.

Por fim, foi realizada a modelagem de um problema real de compras com orçamento limitado, demonstrando como representar uma solução, definir uma função objetivo, estabelecer restrições e verificar a viabilidade de uma solução.

As atividades demonstraram que métodos de força bruta conseguem encontrar soluções ótimas para problemas pequenos, mas podem se tornar inviáveis quando o espaço de busca cresce. Heurísticas e outras técnicas de otimização podem ser utilizadas para obter boas soluções em problemas maiores.
