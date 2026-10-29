import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl


def criar_sistema_fuzzy():
    impacto = ctrl.Antecedent(np.arange(0, 101, 1), "impacto")
    explorabilidade = ctrl.Antecedent(np.arange(0, 11, 1), "explorabilidade")
    urgencia = ctrl.Consequent(np.arange(0, 101, 1), "urgencia")

    urgencia.defuzzify_method = "centroid"

    impacto["baixo"] = fuzzy.trimf(impacto.universe, [0, 0, 40])
    impacto["medio"] = fuzzy.trimf(impacto.universe, [20, 50, 80])
    impacto["alto"] = fuzzy.trapmf(impacto.universe, [60, 80, 100, 100])

    explorabilidade["baixa"] = fuzzy.trimf(
        explorabilidade.universe, [0, 0, 4]
    )
    explorabilidade["moderada"] = fuzzy.trimf(
        explorabilidade.universe, [2, 5, 8]
    )
    explorabilidade["alta"] = fuzzy.trimf(
        explorabilidade.universe, [6, 10, 10]
    )

    urgencia["baixa"] = fuzzy.trimf(urgencia.universe, [0, 0, 30])
    urgencia["media"] = fuzzy.trimf(urgencia.universe, [20, 50, 70])
    urgencia["alta"] = fuzzy.trimf(urgencia.universe, [60, 80, 90])
    urgencia["critica"] = fuzzy.trapmf(
        urgencia.universe, [80, 90, 100, 100]
    )

    return impacto, explorabilidade, urgencia
