
import numpy as np
from sklearn.svm import SVC


def entrenar_svm(X: np.ndarray, Y: np.ndarray, kernel: str = "linear") -> SVC:
    """Entrena un SVC con el kernel indicado ('linear' o 'rbf')."""
    modelo = SVC(kernel=kernel)
    modelo.fit(X, Y)
    return modelo


def obtener_vectores_soporte(modelo: SVC) -> np.ndarray:
    """Los puntos críticos que sostienen la frontera de decisión."""
    return modelo.support_vectors_


def predecir_punto(modelo: SVC, punto: list) -> int:
    return int(modelo.predict(np.array([punto]))[0])
