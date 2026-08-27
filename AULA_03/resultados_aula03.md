# Resultados - Aula 03

## LAB-01 - Algoritmo Genético

### Output da execução

```text
=================================================
ALGORITMO GENÉTICO PASSO A PASSO
==================================================

População inicial: [[0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1]]

==================== GERAÇÃO 0 ====================

Avaliação dos indivíduos:
  [0, 1, 1, 0, 0] → x=12 → f(x)=144
  [0, 1, 1, 1, 0] → x=14 → f(x)=196
  [0, 1, 0, 0, 0] → x= 8 → f(x)= 64
  [0, 1, 0, 0, 0] → x= 8 → f(x)= 64
  [0, 1, 0, 0, 1] → x= 9 → f(x)= 81
  [1, 0, 0, 0, 1] → x=17 → f(x)=289

 Melhor: x = 17 → f(x) = 289

==================== GERAÇÃO 1 ====================

Avaliação dos indivíduos:
  [1, 0, 0, 0, 1] → x=17 → f(x)=289
  [0, 1, 0, 1, 1] → x=11 → f(x)=121
  [0, 1, 1, 0, 0] → x=12 → f(x)=144
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [0, 1, 0, 0, 0] → x= 8 → f(x)= 64
  [0, 1, 1, 1, 0] → x=14 → f(x)=196

 Melhor: x = 23 → f(x) = 529

==================== GERAÇÃO 2 ====================

Avaliação dos indivíduos:
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [0, 1, 0, 1, 1] → x=11 → f(x)=121
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [0, 0, 1, 1, 1] → x= 7 → f(x)= 49
  [1, 1, 1, 1, 1] → x=31 → f(x)=961

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 3 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 1, 1, 1, 1] → x=15 → f(x)=225

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 4 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [0, 1, 1, 1, 1] → x=15 → f(x)=225
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 1, 1, 1, 1] → x=31 → f(x)=961

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 5 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 1, 1, 1, 1] → x=15 → f(x)=225
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 1, 0, 0, 0] → x=24 → f(x)=576

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 6 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 1, 1, 1, 0] → x=14 → f(x)=196
  [1, 1, 1, 0, 1] → x=29 → f(x)=841
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 1, 0, 0, 1] → x=25 → f(x)=625

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 7 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [1, 1, 1, 1, 0] → x=30 → f(x)=900
  [0, 1, 0, 0, 1] → x= 9 → f(x)= 81
  [1, 0, 0, 1, 0] → x=18 → f(x)=324
  [0, 1, 1, 1, 0] → x=14 → f(x)=196

 Melhor: x = 31 → f(x) = 961

==================================================
RESULTADO FINAL
==================================================

Melhor indivíduo: [1, 1, 1, 1, 1]
x = 31
f(x) = 961

Ótimo global: x = 31, f(x) = 961
Erro: 0
```
<img width="850" height="393" alt="image" src="https://github.com/user-attachments/assets/c99a7bd9-e185-4130-a2e6-b32496b67d24" />

### Considerações

A gente entendeu que o algoritmo genético vai testando diferentes possibilidades e, através da seleção, crossover e mutação, vai mantendo e criando soluções melhores. Nesse caso, o objetivo era encontrar o maior valor de `x` e, como a função utilizada é `f(x) = x²`, quanto maior o valor de `x`, maior também será o resultado da função.

Ao longo das gerações, foi possível perceber que as soluções foram melhorando. Na geração 0, o melhor resultado encontrado foi `x = 17`, com `f(x) = 289`. Na geração 1, o melhor passou para `x = 23`, com `f(x) = 529`. Já na geração 2, o algoritmo conseguiu encontrar `x = 31`, com `f(x) = 961`, que é o ótimo global.

Depois disso, o algoritmo continuou mantendo o melhor indivíduo encontrado nas gerações seguintes. No resultado final, o melhor indivíduo foi `[1, 1, 1, 1, 1]`, que representa `x = 31`, obtendo `f(x) = 961` e erro igual a `0`.

Com esse laboratório, conseguimos entender na prática como um algoritmo genético trabalha com uma população de possíveis soluções e vai evoluindo essas soluções ao longo das gerações até encontrar o melhor resultado.


**LAB-02 - ONEMAX

Output da execução

```text
==================================================
ONEMAX - AG com 30 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 14/20, Média = 10.23
Geração  10: Melhor = 19/20, Média = 18.20
Geração  20: Melhor = 20/20, Média = 19.60
Geração  30: Melhor = 20/20, Média = 19.57
Geração  40: Melhor = 20/20, Média = 19.63

MELHOR FITNESS: 20/20
Ótimo = 20 (todos os bits são 1)

<img width="1188" height="390" alt="image" src="https://github.com/user-attachments/assets/f13c1f14-c57d-4a4c-ba13-b4c42fa36e6e" />

### Considerações

No LAB-02, entendemos que o objetivo do problema ONEMAX é fazer o algoritmo genético encontrar uma sequência formada apenas por bits 1. Nesse caso, são 20 bits, então o melhor resultado possível é 20/20.

No início da execução, na geração 0, o melhor indivíduo tinha 14 bits iguais a 1, enquanto a média da população era 10.23. Conforme as gerações foram passando, os resultados foram melhorando. Na geração 10, o melhor já tinha 19/20 bits iguais a 1 e, na geração 20, o algoritmo conseguiu chegar ao resultado máximo de 20/20.

Depois de encontrar o ótimo, o algoritmo continuou mantendo esse melhor resultado nas gerações seguintes. No final, o melhor fitness foi 20/20, o que significa que todos os bits do indivíduo eram 1.

Também entendemos que os parâmetros do algoritmo podem influenciar diretamente seu comportamento. A taxa de mutação pode aumentar a variedade das soluções, o tamanho da população influencia a quantidade de possibilidades avaliadas e o número de gerações determina por quanto tempo o algoritmo pode evoluir. Já o elitismo ajuda a preservar os melhores indivíduos encontrados.

O resultado mostrou na prática que o algoritmo genético conseguiu encontrar a solução ótima antes do final das 50 gerações, mostrando a evolução da população ao longo do processo.

Desafio - Mudança dos parâmetros
1. Aumentar a TAXA_MUT para 0.1

Alteração realizada:

TAXA_MUT = 0.1

Resultado:

==================================================
ONEMAX - AG com 30 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 14/20, Média = 9.63
Geração  10: Melhor = 19/20, Média = 15.83
Geração  20: Melhor = 20/20, Média = 17.03
Geração  30: Melhor = 20/20, Média = 17.33
Geração  40: Melhor = 20/20, Média = 16.83

MELHOR FITNESS: 20/20
Ótimo = 20 (todos os bits são 1)

Resposta:

Ao aumentar a taxa de mutação para 0.1, o algoritmo passou a realizar mais alterações aleatórias nos indivíduos. Isso aumenta a diversidade da população e permite testar novas possibilidades. No nosso resultado, mesmo com a maior taxa de mutação, o algoritmo conseguiu encontrar o ótimo de 20/20 na geração 20.

2. Diminuir a POPULACAO para 10

Alteração realizada:

POPULACAO = 10

Resultado:

==================================================
ONEMAX - AG com 10 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 13/20, Média = 10.30
Geração  10: Melhor = 18/20, Média = 15.70
Geração  20: Melhor = 19/20, Média = 17.50
Geração  30: Melhor = 19/20, Média = 17.10
Geração  40: Melhor = 19/20, Média = 17.90

MELHOR FITNESS: 19/20
Ótimo = 20 (todos os bits são 1)

Resposta:

Ao diminuir a população de 30 para 10 indivíduos, o algoritmo passou a ter menos possibilidades sendo avaliadas em cada geração. No nosso resultado, o melhor fitness chegou a 19/20, mas não conseguiu encontrar o ótimo de 20/20 durante as 50 gerações. Isso mostra que uma população menor pode dificultar a busca pela melhor solução.

3. Aumentar GERACOES para 100

Alteração realizada:

GERACOES = 100

Resultado:

==================================================
ONEMAX - AG com 30 indivíduos, 100 gerações
==================================================
Geração   0: Melhor = 13/20, Média = 9.73
Geração  10: Melhor = 19/20, Média = 15.63
Geração  20: Melhor = 20/20, Média = 16.23
Geração  30: Melhor = 20/20, Média = 16.63
Geração  40: Melhor = 20/20, Média = 16.93
Geração  50: Melhor = 20/20, Média = 17.10
Geração  60: Melhor = 20/20, Média = 17.43
Geração  70: Melhor = 20/20, Média = 16.83
Geração  80: Melhor = 20/20, Média = 17.30
Geração  90: Melhor = 20/20, Média = 16.70

MELHOR FITNESS: 20/20
Ótimo = 20 (todos os bits são 1)

Resposta:

Ao aumentar o número de gerações de 50 para 100, o algoritmo passou a ter mais oportunidades para evoluir a população e buscar uma solução melhor. Nesse resultado, o algoritmo encontrou o ótimo de 20/20 na geração 20 e continuou mantendo esse resultado até o final. As gerações adicionais permitem que o algoritmo tenha mais oportunidades de encontrar e manter uma boa solução.

4. Mudar ELITE para 0

Alteração realizada:

ELITE = 0

Resultado:

==================================================
ONEMAX - AG com 30 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 17/20, Média = 9.60
Geração  10: Melhor = 20/20, Média = 15.43
Geração  20: Melhor = 18/20, Média = 15.03
Geração  30: Melhor = 20/20, Média = 14.87
Geração  40: Melhor = 19/20, Média = 14.97

MELHOR FITNESS: 19/20
Ótimo = 20 (todos os bits são 1)

Resposta:

Ao mudar ELITE para 0, o melhor indivíduo deixa de ser preservado automaticamente para a próxima geração. Por isso, mesmo depois de encontrar uma solução de 20/20 na geração 10, o algoritmo acabou perdendo essa solução nas gerações seguintes. No resultado final, o melhor fitness foi 19/20.

Isso mostra que o elitismo ajuda a preservar as melhores soluções encontradas durante a evolução e evita que uma solução boa seja perdida durante o processo.**
````markdown
```

# LAB-03 - Algoritmo Genético

```text
## Problema

Encontrar um valor de `x` no intervalo `[0, 10]` que maximize a função:

```text
f(x) = x * sin(3x)
````

## Output da execução

```text
==================================================
OTIMIZANDO f(x) = x * sin(3x)
==================================================
Geração   0: Melhor f(x) = 8.7280 (x = 8.9804)
Geração  10: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  20: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  30: Melhor f(x) = 8.9019 (x = 8.9020)
Geração  40: Melhor f(x) = 8.9019 (x = 8.9020)
```
<img width="1189" height="490" alt="image" src="https://github.com/user-attachments/assets/f0172817-bee4-4e0f-a6ee-6b0ccae218c0" />

MELHOR SOLUÇÃO: x = 8.9020, f(x) = 8.9019
``` 
## Considerações

Nesse laboratório, completamos as funções que estavam faltando no algoritmo genético. Foram implementadas a conversão dos bits para um valor real de `x`, o cálculo do fitness e a mutação dos indivíduos.

O objetivo era encontrar um valor de `x` entre 0 e 10 que maximizasse a função `f(x) = x * sin(3x)`. No início da execução, o melhor resultado encontrado foi `f(x) = 8.7280`, com `x = 8.9804`.

Conforme as gerações foram passando, o algoritmo encontrou uma solução melhor. Na geração 10, chegou a `x = 8.9020`, obtendo `f(x) = 8.9019`. Esse resultado continuou sendo mantido até a geração 40.

Com esse laboratório, entendemos melhor como o algoritmo genético utiliza seleção, crossover, mutação e elitismo para encontrar soluções melhores. Também percebemos que, como estamos utilizando uma representação de 8 bits, o algoritmo encontra uma aproximação do melhor valor possível dentro do intervalo definido.

```
```

