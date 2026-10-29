
import sys
from pathlib import Path

AULA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AULA))

import pytest
from src.engine import calcular_urgencia


def test_urgencia_dentro_dos_limites():
    resultado = calcular_urgencia(50, 5)
    assert 0 <= resultado <= 100


def test_risco_alto_supera_risco_baixo():
    risco_baixo = calcular_urgencia(10, 1)
    risco_alto = calcular_urgencia(95, 9)
    assert risco_alto > risco_baixo


def test_impacto_invalido():
    with pytest.raises(ValueError):
        calcular_urgencia(-1, 5)

    with pytest.raises(ValueError):
        calcular_urgencia(101, 5)


def test_explorabilidade_invalida():
    with pytest.raises(ValueError):
        calcular_urgencia(50, -1)

    with pytest.raises(ValueError):
        calcular_urgencia(50, 11)


def test_urgencia_nao_decresce_com_impacto():
    resultado_baixo = calcular_urgencia(20, 5)
    resultado_alto = calcular_urgencia(80, 5)
    assert resultado_alto >= resultado_baixo


def test_desempenho_100_inferencias():
    import time

    inicio = time.perf_counter()

    for _ in range(100):
        calcular_urgencia(50, 5)

    tempo_total = time.perf_counter() - inicio
    tempo_medio_ms = (tempo_total / 100) * 1000

    print(f"\nTempo médio por inferência: {tempo_medio_ms:.3f} ms")

    assert tempo_medio_ms < 10, (
        f"Desempenho abaixo do esperado: "
        f"{tempo_medio_ms:.3f} ms por inferência"
    )
