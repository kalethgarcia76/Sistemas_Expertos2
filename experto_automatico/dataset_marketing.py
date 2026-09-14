
import numpy as np

# Cada cliente: (Edad, Horas_Online, Compras_Previas, Hizo_Clic)
CLIENTES = [
    {"edad": 22, "horas_online": 6, "compras_previas": 1, "hizo_clic": 1},
    {"edad": 25, "horas_online": 5, "compras_previas": 0, "hizo_clic": 1},
    {"edad": 19, "horas_online": 7, "compras_previas": 2, "hizo_clic": 1},
    {"edad": 30, "horas_online": 4, "compras_previas": 3, "hizo_clic": 1},
    {"edad": 40, "horas_online": 3, "compras_previas": 4, "hizo_clic": 1},
    {"edad": 50, "horas_online": 1, "compras_previas": 0, "hizo_clic": 0},
    {"edad": 55, "horas_online": 2, "compras_previas": 1, "hizo_clic": 0},
    {"edad": 60, "horas_online": 0, "compras_previas": 0, "hizo_clic": 0},
    {"edad": 45, "horas_online": 1, "compras_previas": 2, "hizo_clic": 0},
    {"edad": 48, "horas_online": 2, "compras_previas": 0, "hizo_clic": 0},
    {"edad": 35, "horas_online": 5, "compras_previas": 3, "hizo_clic": 1},
    {"edad": 62, "horas_online": 1, "compras_previas": 1, "hizo_clic": 0},
]

NOMBRES_VARIABLES = ["Edad", "Horas_Online", "Compras_Previas"]


def construir_dataset() -> tuple[np.ndarray, np.ndarray]:
    """
    Convierte la lista de clientes en los arrays X (features) e Y
    (etiquetas) que espera scikit-learn.
    """
    X = np.array([
        [c["edad"], c["horas_online"], c["compras_previas"]]
        for c in CLIENTES
    ])
    Y = np.array([c["hizo_clic"] for c in CLIENTES])
    return X, Y
