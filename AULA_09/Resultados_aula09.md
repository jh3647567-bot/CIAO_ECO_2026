Resultados — 

# Laboratório 1 — Ventilador Fuzzy
Foi desenvolvido e executado um sistema de controle fuzzy para determinar a velocidade de um ventilador de acordo com a temperatura do ambiente.

Foram utilizadas três categorias para a temperatura: frio, morno e quente. Para a velocidade do ventilador, foram utilizadas as categorias baixa, média e alta.

Foram realizados testes com cinco valores de temperatura:

Temperatura	Velocidade do ventilador
10 °C	17%
20 °C	44%
25 °C	50%
30 °C	56%
38 °C	83%
Os resultados mostram que, conforme a temperatura aumenta, a velocidade do ventilador também aumenta. Em 10 °C, o sistema determinou uma velocidade de 17%, enquanto em 38 °C a velocidade aumentou para 83%.

<img width="580" height="434" alt="image" src="https://github.com/user-attachments/assets/d21eb369-2eda-41d1-b618-a9f7e8fa04d4" />

A lógica fuzzy permite trabalhar com graus de pertencimento, fazendo com que uma temperatura possa estar parcialmente relacionada às categorias "frio", "morno" e "quente". Dessa forma, o sistema não precisa tomar decisões rígidas e consegue produzir uma transição mais gradual entre as velocidades baixa, média e alta.

Também foram gerados os gráficos das funções de pertinência, permitindo visualizar os conjuntos fuzzy utilizados para a temperatura e para a velocidade do ventilador.

Considerações:
O experimento demonstrou que a lógica fuzzy pode ser utilizada para controlar um sistema de forma gradual. A partir das regras definidas, o controlador transforma a temperatura de entrada em uma velocidade adequada para o ventilador, apresentando resultados coerentes com o aumento da temperatura.


# Laboratório 2 — AULA DE LÓGICA FUZZY

**Gorjeta = 12,5%**

Apesar da alteração no formato das funções de pertinência e nos gráficos, o resultado final permaneceu igual para essas entradas.

<img width="576" height="434" alt="image" src="https://github.com/user-attachments/assets/d0ec5e00-9e27-4d74-93ca-0e117c9e1492" />

---

## Experimento 3 — Métodos de defuzzificação

Foram comparados três métodos de defuzzificação para as entradas serviço = 7 e comida = 3.

| Método   | Gorjeta |
| -------- | ------: |
| Centroid |  12,55% |
| Bisector |  12,58% |
| MOM      |  12,75% |

Os três métodos produziram resultados próximos, porém diferentes. O método MOM apresentou o maior resultado, com **12,75%**.

Isso demonstra que diferentes métodos de defuzzificação podem produzir pequenas diferenças no valor final da saída fuzzy.

<img width="576" height="434" alt="image" src="https://github.com/user-attachments/assets/617a5c96-421a-4697-a7bd-89b0577c80a3" />

---

## Experimento 4 — Conjunto "excelente"

Foi adicionado um quarto conjunto fuzzy chamado **excelente** para representar notas muito altas do serviço.

Também foi adicionada a regra:

**Se o serviço for excelente, então a gorjeta será alta.**

Para serviço = 7 e comida = 3, o resultado foi de **12,55%**.

A nova regra não teve influência significativa nesse caso, pois a nota 7 não apresenta uma pertinência relevante no conjunto "excelente".

<img width="576" height="434" alt="image" src="https://github.com/user-attachments/assets/2b1dab67-8aa7-4f10-a38e-eacaccbf2e7e" />

---

## Experimento 5 — Testes com diferentes entradas

Foram realizados testes com três combinações de notas:

| Nota do serviço | Nota da comida | Gorjeta |
| --------------: | -------------: | ------: |
|               0 |              0 |   4,33% |
|              10 |             10 |  21,00% |
|               5 |              5 |  12,67% |

Os resultados mostram que o sistema apresenta um comportamento coerente. Para notas baixas, a gorjeta tende a ser menor. Para notas altas, a gorjeta aumenta. Para notas intermediárias, o resultado também fica em uma faixa intermediária.

---

## Gráficos das funções de pertinência

Também foram gerados os gráficos das funções de pertinência utilizadas pelo sistema fuzzy, permitindo visualizar as categorias de serviço, comida e gorjeta.

**[COLOCAR AQUI O GRÁFICO DAS FUNÇÕES DE PERTINÊNCIA DO SERVIÇO]**

*Figura 6 — Funções de pertinência utilizadas para a variável serviço.*

**[COLOCAR AQUI O GRÁFICO DAS FUNÇÕES DE PERTINÊNCIA DA COMIDA]**

*Figura 7 — Funções de pertinência utilizadas para a variável comida.*

**[COLOCAR AQUI O GRÁFICO DAS FUNÇÕES DE PERTINÊNCIA DA GORJETA]**

*Figura 8 — Funções de pertinência utilizadas para a variável gorjeta.*

---

## Considerações

O experimento demonstrou como a lógica fuzzy pode ser utilizada para determinar uma gorjeta a partir de avaliações do serviço e da comida. A utilização de conjuntos fuzzy e regras linguísticas permite trabalhar com situações intermediárias, evitando decisões totalmente rígidas.

Os experimentos também mostraram que alterações nas regras, nas funções de pertinência e no método de defuzzificação podem influenciar o resultado do sistema. Mesmo assim, os valores obtidos apresentaram comportamento coerente com as notas fornecidas como entrada.


# Laboratório 3: Sistema de Inferência Fuzzy

## 1. Definição do problema

O objetivo deste projeto é desenvolver um sistema de inferência fuzzy
para determinar o nível de alerta de um ambiente a partir de duas
informações: o nível de ruído e a intensidade de movimento detectada.

O ruído é medido em decibéis (dB), enquanto o movimento é representado
em uma escala de 0 a 10. A saída do sistema representa o nível de alerta
em uma escala de 0% a 100%.

A lógica fuzzy é adequada para este problema porque conceitos como
"baixo", "médio" e "alto" não possuem limites exatos. Assim, o sistema
consegue trabalhar com situações intermediárias e produzir uma resposta
gradual.

## 2. Modelagem

### Entrada 1 — Ruído

- Universo de discurso: 0 a 100 dB
- Termos linguísticos: baixo, médio e alto
- Funções de pertinência: trapezoidais e triangulares

  <img width="580" height="434" alt="image" src="https://github.com/user-attachments/assets/0ce5be01-f665-4712-ac5a-93be98054c37" />


### Entrada 2 — Movimento

- Universo de discurso: 0 a 10
- Termos linguísticos: parado, leve e intenso
- Funções de pertinência: trapezoidais e triangulares

<img width="580" height="434" alt="image" src="https://github.com/user-attachments/assets/2c0b0b7e-cdcd-4ca9-9eb6-b4e4012a5ff2" />


### Saída — Nível de alerta

- Universo de discurso: 0% a 100%
- Termos linguísticos: baixo, médio e alto
- Funções de pertinência: triangulares

<img width="580" height="434" alt="image" src="https://github.com/user-attachments/assets/0396b7a8-8ede-47c5-92af-19fab44c8735" />

## 3. Base de regras

Foram utilizadas nove regras fuzzy:

1. SE o ruído é baixo E o movimento é parado, ENTÃO o alerta é baixo.
2. SE o ruído é baixo E o movimento é leve, ENTÃO o alerta é baixo.
3. SE o ruído é baixo E o movimento é intenso, ENTÃO o alerta é médio.
4. SE o ruído é médio E o movimento é parado, ENTÃO o alerta é baixo.
5. SE o ruído é médio E o movimento é leve, ENTÃO o alerta é médio.
6. SE o ruído é médio E o movimento é intenso, ENTÃO o alerta é alto.
7. SE o ruído é alto E o movimento é parado, ENTÃO o alerta é médio.
8. SE o ruído é alto E o movimento é leve, ENTÃO o alerta é alto.
9. SE o ruído é alto OU o movimento é intenso, ENTÃO o alerta é alto.

As regras utilizam os operadores E e OU.

## 4. Testes

Foram realizados cinco testes com diferentes combinações de ruído e
movimento.

| Situação | Ruído | Movimento | Alerta obtido |
|---|---:|---:|---:|
| Ambiente tranquilo | 20 dB | 1 | 13,3% |
| Movimento moderado | 50 dB | 5 | 50,0% |
| Muito movimento | 30 dB | 9 | 64,3% |
| Ruído elevado | 85 dB | 2 | 64,3% |
| Ruído e movimento altos | 90 dB | 9 | 86,7% |

## 5. Análise dos resultados

No primeiro teste, com ruído de 20 dB e movimento 1, o sistema produziu
um alerta de 13,3%. Esse resultado é coerente com um ambiente tranquilo,
pois tanto o ruído quanto o movimento são baixos.

No segundo teste, com ruído de 50 dB e movimento 5, o resultado foi de
50,0%, representando uma situação intermediária e um nível de alerta
médio.

No terceiro teste, o ruído foi de 30 dB e o movimento foi intenso,
com valor 9. O sistema produziu um alerta de 64,3%. Isso demonstra que
o movimento intenso pode aumentar significativamente o nível de alerta.

No quarto teste, o ruído foi elevado, chegando a 85 dB, enquanto o
movimento foi baixo. O resultado foi de 64,3%, mostrando que um nível
elevado de ruído também pode aumentar o alerta.

No último teste, tanto o ruído quanto o movimento apresentaram valores
altos. O sistema produziu um alerta de 86,7%, sendo o maior resultado
obtido nos testes.

Os resultados demonstram que o sistema fuzzy consegue combinar as duas
entradas e produzir uma saída gradual, em vez de utilizar somente
decisões rígidas baseadas em limites fixos.

## 6. Conclusão

O projeto demonstrou a aplicação da lógica fuzzy em um problema de
detecção de nível de alerta. O sistema utilizou duas entradas numéricas,
uma saída numérica e nove regras de inferência fuzzy.

A lógica fuzzy mostrou-se adequada porque permite representar conceitos
vagos como baixo, médio e alto e combinar diferentes condições por meio
dos operadores E e OU.

Os testes apresentaram resultados coerentes com as situações avaliadas:
ambientes tranquilos produziram alertas baixos, enquanto situações com
ruído elevado, movimento intenso ou ambos produziram alertas maiores.

Portanto, o sistema desenvolvido consegue transformar informações
numéricas de ruído e movimento em um nível de alerta de maneira gradual.
