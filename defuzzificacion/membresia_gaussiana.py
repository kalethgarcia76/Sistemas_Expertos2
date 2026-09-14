
import numpy as np


def membresia_gaussiana(x: np.ndarray, centro: float, sigma: float) -> np.ndarray:
    """
    Curva de membresía en forma de campana, centrada en `centro` con
    ancho controlado por `sigma` (a mayor sigma, campana más ancha).
    """
    x = np.asarray(x, dtype=float)
    if sigma <= 0:
        raise ValueError(f"sigma debe ser positivo (recibido: {sigma})")
    return np.exp(-((x - centro) ** 2) / (2 * sigma ** 2))
