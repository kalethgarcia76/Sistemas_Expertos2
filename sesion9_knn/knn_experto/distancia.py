
import numpy as np


def distancia_euclidiana(punto_a, punto_b) -> float:
    """Distancia euclidiana entre dos puntos de N dimensiones."""
    a = np.asarray(punto_a, dtype=float)
    b = np.asarray(punto_b, dtype=float)
    if a.shape != b.shape:
        raise ValueError(f"Los puntos deben tener la misma dimensión ({a.shape} vs {b.shape})")
    return float(np.sqrt(np.sum((b - a) ** 2)))
