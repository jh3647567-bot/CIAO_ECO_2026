# RELATÓRIO FINAL PSO

## PARTE 1: O QUE VOCÊ APRENDEU?

### 1. Explique com suas palavras o que é o PSO e como ele funciona.

O PSO (Particle Swarm Optimization) é um algoritmo de otimização inspirado no comportamento de grupos de animais, como enxames de pássaros. Ele utiliza várias partículas que exploram o espaço de busca em busca da melhor solução. Cada partícula considera sua própria melhor posição encontrada (pBest) e a melhor posição encontrada pelo enxame (gBest) para atualizar sua velocidade e sua posição. Com várias iterações, o enxame busca convergir para uma solução de menor custo.

### 2. Qual a diferença entre pBest e gBest? Por que ambos são importantes?

O pBest representa a melhor posição que uma determinada partícula encontrou durante sua busca. Já o gBest representa a melhor posição encontrada por todo o enxame. O pBest permite que cada partícula utilize sua própria experiência, enquanto o gBest permite que todas aproveitem a melhor experiência encontrada pelo grupo. Os dois são importantes para equilibrar a exploração individual e a cooperação entre as partículas.

---

# PARTE 2: SUA EXPERIÊNCIA COM AS MISSÕES

## Missão 1 - A Partícula Solitária

**A partícula encontrou o mínimo?** ( ) Sim **(X) Não**

**Quantas iterações foram necessárias?** 20 iterações

**Dificuldade:** ( ) Fácil **(X) Médio** ( ) Difícil

A partícula começou em -7.7449 e terminou em -3.6223, com fitness final de 13.1213. O mínimo global seria x = 0, com fitness igual a 0. Portanto, a partícula melhorou sua posição, mas não encontrou o mínimo global dentro das 20 iterações.

** Resultados: 
============================================================

Posição inicial: -7.7449
Fitness inicial: 59.9842

Iteração  1: pos = -8.3375, fitness =  69.5145
Iteração  2: pos = -7.9935, fitness =  63.8964
Iteração  3: pos = -7.1033, fitness =  50.4562
Iteração  4: pos = -6.3910, fitness =  40.8453
Iteração  5: pos = -5.8213, fitness =  33.8870
Iteração  6: pos = -5.3654, fitness =  28.7879
Iteração  7: pos = -5.0008, fitness =  25.0078
Iteração  8: pos = -4.7091, fitness =  22.1752
Iteração  9: pos = -4.4757, fitness =  20.0316
Iteração 10: pos = -4.2890, fitness =  18.3952
Iteração 11: pos = -4.1396, fitness =  17.1363
Iteração 12: pos = -4.0201, fitness =  16.1613
Iteração 13: pos = -3.9245, fitness =  15.4019
Iteração 14: pos = -3.8480, fitness =  14.8075
Iteração 15: pos = -3.7869, fitness =  14.3404
Iteração 16: pos = -3.7379, fitness =  13.9721
Iteração 17: pos = -3.6988, fitness =  13.6809
Iteração 18: pos = -3.6674, fitness =  13.4501
Iteração 19: pos = -3.6424, fitness =  13.2670
Iteração 20: pos = -3.6223, fitness =  13.1213

============================================================
 RESULTADO FINAL
============================================================
Posição final: -3.622338
Fitness final: 13.121335
Ótimo global: x = 0.000000, f(x) = 0.000000
Erro: 3.622338

============================================================

<img width="1189" height="490" alt="image" src="https://github.com/user-attachments/assets/b1396872-9aae-48b4-88d7-ec7b68fd2a69" />

--- 

## Missão 2 - O Enxame

**O enxame encontrou o mínimo global?** ( ) Sim **(X) Não**

**Compare com a Missão 1: O enxame foi mais rápido?** **(X) Sim** ( ) Não

**Dificuldade:** ( ) Fácil **(X) Médio** ( ) Difícil

O enxame chegou a um fitness de 0.001945 após 50 iterações, ficando muito próximo do mínimo global, que possui fitness igual a 0. Em comparação com a Missão 1, o enxame apresentou uma aproximação muito melhor do ótimo.

**Resultados:

============================================================
 PSO - FUNÇÃO DE ROSENBROCK
============================================================
Início: Melhor fitness = 4.741384
Iteração  10: Melhor = 0.130766
Iteração  20: Melhor = 0.112664
Iteração  30: Melhor = 0.003058
Iteração  40: Melhor = 0.003058
Iteração  50: Melhor = 0.001945

Fim: Melhor fitness = 0.001945
Ótimo global: f(1,1) = 0.000000


<img width="1362" height="490" alt="image" src="https://github.com/user-attachments/assets/a1c8bf06-e555-424f-ae5d-16729a36c8da" />

---
 
## Missão 3 - Problema Corporativo

**Compare com o custo inicial: Melhorou?** **(X) Sim** ( ) Não

**Quantos centros foram alocados?** 5

**Dificuldade:** ( ) Fácil **(X) Médio** ( ) Difícil

O PSO conseguiu reduzir o custo ao longo das iterações, passando por 3716.12 na iteração 20 e chegando a 3514.93 na iteração 100. Foram alocados 5 centros de distribuição.

** Resultados:

============================================================
 OPTIMUS TECH - LOGÍSTICA INTELIGENTE
============================================================

 DADOS DO PROBLEMA:
   - 50 clientes
   - 5 centros de distribuição
   - Demanda média: 51.0 unidades

 OTIMIZANDO...
  Iteração  20: Custo = 3716.12
  Iteração  40: Custo = 3581.58
  Iteração  60: Custo = 3526.28
  Iteração  80: Custo = 3517.56
  Iteração 100: Custo = 3514.93

 RESULTADO FINAL:
   Tempo de execução: 1.80 segundos
   Custo total: 3514.93
   Melhor custo possível: 0.00
   Centros de distribuição:
      Centro 1: (2.70, 5.32)
      Centro 2: (0.59, 8.65)
      Centro 3: (5.47, 1.76)
      Centro 4: (0.90, 1.94)
      Centro 5: (7.74, 6.12)


<img width="1389" height="490" alt="image" src="https://github.com/user-attachments/assets/69bdd42b-1172-47c8-85b7-e0d6683e5e9a" />

---

## Missão 4 - Otimização de Parâmetros

**Melhor configuração encontrada:**
w = 0.7, c1 = 1.8, c2 = 2.5, partículas = 30

**Custo médio:** 15812.90

**Pior configuração encontrada:**
w = 0.7, c1 = 1.8, c2 = 1.8, partículas = 60

**Custo médio:** 20164.06

**Dificuldade:** ( ) Fácil **(X) Médio** ( ) Difícil

** Resultados:

============================================================
 EXPERIMENTOS COM PARÂMETROS DO PSO
============================================================

 Experimento: Padrão
   Parâmetros: w=0.7, c1=1.8, c2=1.8, partículas=30
   Custo médio: 16764.48 ± 1317.48

 Experimento: Inércia Alta
   Parâmetros: w=0.9, c1=1.8, c2=1.8, partículas=30
   Custo médio: 19262.97 ± 1918.66

 Experimento: Inércia Baixa
   Parâmetros: w=0.5, c1=1.8, c2=1.8, partículas=30
   Custo médio: 16386.38 ± 1818.45

 Experimento: Cognitivo Alto
   Parâmetros: w=0.7, c1=2.5, c2=1.8, partículas=30
   Custo médio: 16570.90 ± 2672.41

 Experimento: Social Alto
   Parâmetros: w=0.7, c1=1.8, c2=2.5, partículas=30
   Custo médio: 15812.90 ± 1636.68

 Experimento: Mais Partículas
   Parâmetros: w=0.7, c1=1.8, c2=1.8, partículas=60
   Custo médio: 20164.06 ± 1664.27

============================================================
 ANÁLISE DOS RESULTADOS
============================================================

| Experimento        | Custo Médio | Melhor Custo | Pior Custo  |
|--------------------|-------------|--------------|-------------|
| Padrão             |   16764.48 |     19025.98 |    15443.17 |
| Inércia Alta       |   19262.97 |     21460.47 |    16955.05 |
| Inércia Baixa      |   16386.38 |     19025.98 |    13552.66 |
| Cognitivo Alto     |   16570.90 |     21460.47 |    13552.66 |
| Social Alto        |   15812.90 |     16955.05 |    12756.20 |
| Mais Partículas    |   20164.06 |     21460.47 |    16955.05 |

<img width="1389" height="790" alt="image" src="https://github.com/user-attachments/assets/4c072d8e-dabb-4150-b02c-e996e8cb9169" />

### Observações sobre os parâmetros

* **Inércia (w):** a inércia baixa (w = 0.5) apresentou resultado melhor que a configuração padrão, enquanto a inércia alta (w = 0.9) apresentou resultado pior.
* **Cognitivo (c1):** aumentar c1 de 1.8 para 2.5 apresentou uma pequena melhora no custo médio.
* **Social (c2):** aumentar c2 de 1.8 para 2.5 apresentou o melhor resultado entre as configurações testadas.
* **Número de partículas:** aumentar de 30 para 60 partículas não melhorou o resultado neste experimento; pelo contrário, apresentou o maior custo médio.

### Conclusões

A configuração **Social Alto**, com w = 0.7, c1 = 1.8, c2 = 2.5 e 30 partículas, obteve o melhor resultado, com custo médio de **15812.90**.

A configuração **Mais Partículas**, com 60 partículas, obteve o pior resultado, com custo médio de **20164.06**.

Para este problema, recomendo a configuração **Social Alto**, pois apresentou o menor custo médio entre todas as configurações testadas. Os resultados indicam que uma maior influência social ajudou as partículas a aproveitar melhor a melhor solução encontrada pelo enxame.
