
import numpy as np


def sigmoide(x: np.ndarray) -> np.ndarray:
    """Función de activación: comprime cualquier valor real al rango (0,1)."""
    return 1 / (1 + np.exp(-x))


def forward_pass(X: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                  W2: np.ndarray, b2: np.ndarray) -> dict:
    """
    Propagación hacia adelante completa (2 capas: oculta + salida).

    X puede ser UN cliente (vector 1D de forma (n_entradas,)) o un LOTE
    de varios clientes (matriz 2D de forma (n_clientes, n_entradas)) —
    np.dot maneja ambos casos sin cambiar ni una línea de código, que es
    justo el "Reto Dimensional" del Taller de Laboratorio.
    """
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoide(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoide(Z2)

    return {"Z1": Z1, "A1": A1, "Z2": Z2, "salida": A2}
