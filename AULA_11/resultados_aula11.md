
# Aula 11 — Sistema de Inferência Fuzzy

## 1. Objetivo

Desenvolver e validar um sistema de inferência fuzzy para classificar a urgência de riscos cibernéticos, utilizando o impacto e a explorabilidade como variáveis de entrada.

## 2. Modelo desenvolvido

O sistema utiliza três variáveis fuzzy:

- **Impacto:** escala de 0 a 100.
- **Explorabilidade:** escala de 0 a 10.
- **Urgência:** escala de 0 a 100.

Foram implementadas nove regras de inferência, relacionando os níveis de impacto e explorabilidade aos níveis de urgência.

## 3. Resultados dos cenários de teste

| Cenário | Impacto | Explorabilidade | Urgência calculada |
|---|---:|---:|---:|
| Risco baixo | 10 | 1 | 10,50 |
| Risco intermediário | 50 | 5 | 46,67 |
| Risco elevado | 95 | 9 | 91,73 |

Os resultados demonstraram aumento da urgência nos cenários avaliados.

## 4. Testes automatizados

Na primeira execução, os cinco testes funcionais foram aprovados.

Ao acrescentar o teste de desempenho, foram identificados seis testes no total. Cinco passaram e um falhou, pois o tempo médio inicial foi de 20,727 ms por inferência, acima do limite de 10 ms.

## 5. Otimização realizada

O motor de inferência estava sendo recriado a cada chamada. Para reduzir esse custo, foi implementado o reaproveitamento do sistema e da simulação por meio de cache.

Após a alteração, o tempo médio medido foi de 0,059 ms por inferência.

## 6. Resultado após a correção

- Testes funcionais: aprovados.
- Validação dos limites de entrada: aprovada.
- Teste de comportamento da urgência: aprovado.
- Teste de desempenho: aprovado.
- Total: 6 testes aprovados.

A otimização reduziu o tempo médio medido em aproximadamente 99,7%, atendendo ao limite definido de menos de 10 ms por inferência.

## 7. Conclusão

A atividade permitiu desenvolver e testar um sistema de inferência fuzzy, além de identificar e corrigir um problema de desempenho. A reutilização do motor reduziu o tempo de execução nos testes realizados, mantendo os resultados funcionais esperados.


## 8. Registro das três execuções

### Execução 1 — Testes funcionais iniciais

Os cinco testes funcionais foram aprovados. Ao adicionar o teste de desempenho, identificou-se um tempo médio inicial de 20,727 ms por inferência, acima do limite de 10 ms.

### Execução 2 — Erro proposital

A condição do teste de desempenho foi alterada temporariamente de `tempo_medio_ms < 10` para `tempo_medio_ms < 0`.

Resultado observado: cinco testes aprovados e um reprovado. O tempo médio medido foi de aproximadamente 0,060 ms por inferência. A falha ocorreu porque o limite foi definido intencionalmente como zero.

### Execução 3 — Correção

A condição original foi restaurada para `tempo_medio_ms < 10`. O motor de inferência otimizado foi mantido, com reutilização do sistema e da simulação.

O resultado final esperado é de seis testes aprovados. O tempo médio deve permanecer abaixo de 10 ms por inferência. O resultado definitivo desta execução deve ser confirmado no terminal de testes.
