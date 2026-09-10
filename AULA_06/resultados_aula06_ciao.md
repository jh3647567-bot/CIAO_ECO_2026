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

2 - 

Experimento	Parâmetro	Resultado

1	ALPHA = 0,1	Rota [0,1,2,3,4,5] — custo 8,0

1	ALPHA = 1,0	Rota [0,1,2,3,4,5] — custo 8,0

1	ALPHA = 5,0	Rota [0,1,2,3,4,5] — custo 8,0

2	BETA = 0,5	Rota [0,1,2,3,4,5] — custo 8,0

2	BETA = 5,0	Rota [0,1,2,3,4,5] — custo 8,0

3	Evaporação = 0,1	Rota [0,1,2,4,5] — custo 8,0

3	Evaporação = 0,9	Rota [0,1,2,3,4,5] — custo 8,0

4	Formigas = 5	Rota [0,1,2,3,4,5] — custo 8,0

4	Formigas = 50	Rota [0,1,2,3,4,5] — custo 8,0


Respostas que você pode colocar no relatório


Experimento 1 — ALPHA

Quando aumentamos o ALPHA, aumenta a influência da experiência acumulada pelas formigas, representada pelo feromônio. Nos testes realizados, entretanto, o melhor custo permaneceu 8,0 e a melhor rota também permaneceu praticamente a mesma.

Experimento 2 — BETA

Quando o BETA aumenta, a influência da informação heurística, relacionada ao custo do caminho, aumenta. Assim, caminhos de menor custo tornam-se mais atrativos. Nos testes realizados, o melhor custo permaneceu 8,0.

Experimento 3 — Evaporação

Com uma taxa de evaporação alta, o algoritmo esquece mais rapidamente as experiências anteriores, pois o feromônio desaparece mais rapidamente. Com evaporação de 0,1 foi encontrada a rota [0,1,2,4,5], enquanto com 0,9 foi encontrada [0,1,2,3,4,5]. O custo permaneceu 8,0.

Experimento 4 — Número de formigas

Aumentar o número de formigas permite explorar mais soluções a cada iteração. No experimento, tanto com 5 quanto com 50 formigas foi encontrada a rota [0,1,2,3,4,5], com custo 8,0.

<img width="846" height="471" alt="image" src="https://github.com/user-attachments/assets/41acc56b-09bb-41d9-876b-d412a64c90de" />

<img width="607" height="519" alt="image" src="https://github.com/user-attachments/assets/1ae33f08-5985-4581-90b4-e8b68ef001f5" />
