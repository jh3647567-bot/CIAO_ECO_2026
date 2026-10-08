Resultados — Lab 1
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

Para o Lab 1, essa é a parte de resultados que você precisa colocar. Se o professor também pedir os gráficos, coloque abaixo desse texto os dois gráficos que você já gerou no Colab.
