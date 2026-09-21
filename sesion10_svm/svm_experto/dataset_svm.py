
import numpy as np

X_BASE = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])
Y_BASE = np.array([0, 0, 0, 1, 1, 1])


def agregar_punto_conflictivo(X: np.ndarray, Y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Agrega el punto [5, 5] con etiqueta 0 (Clase A), tal como pide el
    Taller de Laboratorio. Este punto cae geométricamente muy cerca de
    la Clase B, lo que "engaña" a una frontera lineal.
    """
    X_nuevo = np.vstack([X, [5, 5]])
    Y_nuevo = np.append(Y, 0)
    return X_nuevo, Y_nuevo
