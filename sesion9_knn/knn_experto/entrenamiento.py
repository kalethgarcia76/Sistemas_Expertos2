
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def entrenar_knn(X: np.ndarray, Y: np.ndarray, k: int) -> KNeighborsClassifier:
    """Entrena (memoriza) el dataset con un valor de K específico."""
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X, Y)
    return modelo


def predecir(modelo: KNeighborsClassifier, punto: list) -> int:
    """Predice la clase de un punto nuevo."""
    return int(modelo.predict(np.array([punto]))[0])
