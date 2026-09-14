
import numpy as np


def centro_de_gravedad(x: np.ndarray, mu: np.ndarray) -> float:
    """
    Calcula el valor Crisp (defuzzificado) de una curva difusa discreta
    usando el método del Centroide.

    Parámetros
    ----------
    x  : valores del universo de discurso (eje X).
    mu : grados de membresía correspondientes a cada x (eje Y, en [0,1]).

    Devuelve
    --------
    El valor x que representa el centro de masa del área bajo la curva.
    """
    x = np.asarray(x, dtype=float)
    mu = np.asarray(mu, dtype=float)

    if x.shape != mu.shape:
        raise ValueError(
            f"x y mu deben tener el mismo tamaño (recibido x={x.shape}, mu={mu.shape})"
        )

    area_total = np.sum(mu)
    if area_total == 0:
        raise ValueError(
            "El área total (Σ μ(x)) es 0: ninguna regla se disparó, "
            "no hay nada que defuzzificar."
        )

    numerador = np.sum(x * mu)
    return float(numerador / area_total)
