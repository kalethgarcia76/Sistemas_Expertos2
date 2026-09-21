
import numpy as np


def funcion_escalon(z: float) -> int:
    """Función de Activación Escalón: 1 si z >= 0, 0 si z < 0."""
    return 1 if z >= 0 else 0


def perceptron(X: np.ndarray, W: np.ndarray, b: float) -> int:
    """
    Ecuación Forward completa de una neurona:
        Z = (X . W) + b        (combinación lineal / producto punto)
        salida = escalon(Z)    (activación)
    """
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)
