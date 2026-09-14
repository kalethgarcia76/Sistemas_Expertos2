
import numpy as np
from .centroide import centro_de_gravedad
from .membresia_gaussiana import membresia_gaussiana


def calcular_fuerza_frenado(centro: float = 70.0, sigma: float = 10.0,
                             n_puntos: int = 100) -> tuple[np.ndarray, np.ndarray, float]:
    """
    Construye el universo de discurso (0-100 N) con `n_puntos`
    elementos, genera la curva Gaussiana de respuesta y la defuzzifica.

    Devuelve (x, curva, fuerza_crisp).
    """
    x_frenado = np.linspace(0, 100, n_puntos)
    curva_respuesta = membresia_gaussiana(x_frenado, centro=centro, sigma=sigma)
    fuerza_crisp = centro_de_gravedad(x_frenado, curva_respuesta)
    return x_frenado, curva_respuesta, fuerza_crisp
