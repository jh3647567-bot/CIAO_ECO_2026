# Aula 10 — Lógica Fuzzy: Desafio dos Extremos

## 1. Objetivo
A atividade utiliza um sistema de inferência fuzzy do tipo Mamdani para relacionar Impacto e Explorabilidade a uma saída chamada Urgência. O objetivo é observar como as funções de pertinência e o método de defuzzificação influenciam os resultados nos extremos.

## 2. Variáveis fuzzy
- **Impacto:** baixo (0–40), médio (20–80) e alto (60–100).
- **Explorabilidade:** baixa (0–4), moderada (2–8) e alta (6–10).
- **Urgência:** baixa, média, alta e crítica.

## 3. Matriz de regras 3 × 3

| Impacto / Explorabilidade | Baixa (0–4) | Moderada (2–8) | Alta (6–10) |
|---|---|---|---|
| Baixo (0–40) | Urgência Baixa | Urgência Baixa | Urgência Média |
| Médio (20–80) | Urgência Média | Urgência Alta | Urgência Alta |
| Alto (60–100) | Urgência Crítica | Urgência Crítica | Urgência Crítica |

O modelo utiliza nove regras. Quando o impacto é alto, a urgência é crítica independentemente da explorabilidade.

## 4. Desafio dos extremos
O método **Centroide** calcula o centro de gravidade da área fuzzy resultante. Por isso, a saída pode não alcançar exatamente 0% ou 100%, mesmo quando as entradas estão nos valores extremos.

No modelo-base, com a função crítica triangular `[62.5, 100, 100]`, os resultados foram:
- Impacto = 0 e Explorabilidade = 0: **Urgência = 4,33%**.
- Impacto = 100 e Explorabilidade = 10: **Urgência = 87,50%**.

Na abordagem A, a função crítica foi alterada para o trapézio `[80, 95, 100, 100]`, mantendo o Centroide. O extremo máximo chegou a **93,00%**, sem alcançar 100%.

Na abordagem B, foi utilizado o método **MOM (Mean of Maximum)** com a função crítica `[80, 100, 100]`. Os resultados nos extremos foram:
- Extremo mínimo: **0,00%**.
- Extremo máximo: **100,00%**.

O MOM considera a média dos pontos que apresentam o maior grau de pertinência. Como o pico da função crítica está em 100, a saída máxima pode alcançar 100%.

## 5. Interpretação da superfície de decisão 3D
A superfície representa a relação entre Impacto, Explorabilidade e Urgência. Quando o impacto é baixo, a urgência tende a ser baixa ou média. Para impacto médio, a urgência tende a aumentar conforme as regras aplicadas. Quando o impacto é alto, a urgência se torna crítica em todos os níveis de explorabilidade.

O gráfico permite visualizar como o sistema fuzzy combina as duas entradas para produzir uma saída gradual, sem depender somente de limites rígidos.

<img width="895" height="790" alt="image" src="https://github.com/user-attachments/assets/cc52f852-4a61-417b-a261-fcea937d5444" />

*Figura 1 — Superfície de decisão do sistema fuzzy Mamdani com método MOM.*

## 6. Arquivos
- `lab01_aula10.py`: código-fonte, regras, testes dos extremos e geração do gráfico.
- `resultados_aula10_ciao.md`: relatório da atividade.
- `superficie_decisao.png`: gráfico 3D gerado pelo programa.

## 7. Como executar
Instale as dependências:

```bash
pip install numpy scikit-fuzzy matplotlib
```

Execute o código:

```bash
python lab01_aula10.py
```

O programa imprime os resultados dos testes e salva o gráfico `superficie_decisao.png` na pasta de execução.

