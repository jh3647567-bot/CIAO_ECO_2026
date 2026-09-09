Resultados da execução

1- 

Melhor rota encontrada:
[0, 1, 2, 3, 4, 5]

Custo da melhor rota:
8.0

Curva de convergência:
A curva mostrou que o algoritmo encontrou rapidamente uma rota com custo 8.0 e permaneceu nesse valor durante as iterações. Isso indica que, nessa execução, o ACO encontrou uma solução de baixo custo e não encontrou outra rota melhor.

Matriz final de feromônio:
A matriz final mostrou uma grande concentração de feromônio nas conexões 0→1, 1→2, 2→3, 3→4 e 4→5. Essas conexões formam a melhor rota encontrada pelo algoritmo. Isso demonstra que as melhores rotas foram reforçadas pelo depósito de feromônio.

Questões
1. Por que o ACO utiliza várias formigas?

O ACO utiliza várias formigas para explorar diferentes caminhos da rede. Cada formiga pode encontrar uma rota diferente, permitindo que várias possibilidades sejam analisadas. Essa exploração aumenta a chance de encontrar uma solução melhor e evita que o algoritmo fique preso em apenas um caminho.

2. Por que uma rota de menor custo recebe mais feromônio?

Uma rota de menor custo recebe mais feromônio porque representa uma solução melhor. As próximas formigas são influenciadas pela quantidade de feromônio e tendem a escolher os caminhos que foram utilizados pelas melhores rotas. Dessa forma, os caminhos de menor custo são reforçados durante as iterações.

3. O que aconteceria sem evaporação?

Sem a evaporação do feromônio, as informações das primeiras rotas encontradas permaneceriam acumuladas. Isso poderia fazer com que as formigas continuassem escolhendo caminhos antigos, mesmo quando fossem encontradas soluções melhores. A evaporação reduz a influência das informações antigas e permite que o algoritmo continue explorando novas possibilidades.

<img width="846" height="471" alt="image" src="https://github.com/user-attachments/assets/85da2425-7ba5-481d-a350-ff3007d64338" />
<img width="598" height="519" alt="image" src="https://github.com/user-attachments/assets/db583051-f503-4ba1-ae08-86038e9f4bcd" />

