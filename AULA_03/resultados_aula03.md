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

### Considerações da dupla/trio

A gente entendeu que o algoritmo genético vai testando diferentes possibilidades e, através da seleção, crossover e mutação, vai mantendo e criando soluções melhores. Nesse caso, o objetivo era encontrar o maior valor de `x` e, como a função utilizada é `f(x) = x²`, quanto maior o valor de `x`, maior também será o resultado da função.

Ao longo das gerações, foi possível perceber que as soluções foram melhorando. Na geração 0, o melhor resultado encontrado foi `x = 17`, com `f(x) = 289`. Na geração 1, o melhor passou para `x = 23`, com `f(x) = 529`. Já na geração 2, o algoritmo conseguiu encontrar `x = 31`, com `f(x) = 961`, que é o ótimo global.

Depois disso, o algoritmo continuou mantendo o melhor indivíduo encontrado nas gerações seguintes. No resultado final, o melhor indivíduo foi `[1, 1, 1, 1, 1]`, que representa `x = 31`, obtendo `f(x) = 961` e erro igual a `0`.

Com esse laboratório, conseguimos entender na prática como um algoritmo genético trabalha com uma população de possíveis soluções e vai evoluindo essas soluções ao longo das gerações até encontrar o melhor resultado.
