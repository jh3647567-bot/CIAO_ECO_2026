
from functools import lru_cache
from skfuzzy import control as ctrl
from src.model import criar_sistema_fuzzy


@lru_cache(maxsize=1)
def construir_motor_inferencia():
    impacto, explorabilidade, urgencia = criar_sistema_fuzzy()

    regras = [
        ctrl.Rule(impacto["baixo"] & explorabilidade["baixa"], urgencia["baixa"]),
        ctrl.Rule(impacto["baixo"] & explorabilidade["moderada"], urgencia["baixa"]),
        ctrl.Rule(impacto["baixo"] & explorabilidade["alta"], urgencia["media"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["baixa"], urgencia["baixa"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["moderada"], urgencia["media"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["alta"], urgencia["alta"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["baixa"], urgencia["media"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["moderada"], urgencia["alta"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["alta"], urgencia["critica"]),
    ]

    return ctrl.ControlSystem(regras)


@lru_cache(maxsize=1)
def _obter_simulacao():
    sistema = construir_motor_inferencia()
    return ctrl.ControlSystemSimulation(sistema)


def calcular_urgencia(valor_impacto, valor_explorabilidade):
    if not 0 <= valor_impacto <= 100:
        raise ValueError("O impacto deve estar entre 0 e 100.")

    if not 0 <= valor_explorabilidade <= 10:
        raise ValueError("A explorabilidade deve estar entre 0 e 10.")

    simulacao = _obter_simulacao()
    simulacao.input["impacto"] = valor_impacto
    simulacao.input["explorabilidade"] = valor_explorabilidade
    simulacao.compute()

    return simulacao.output["urgencia"]
