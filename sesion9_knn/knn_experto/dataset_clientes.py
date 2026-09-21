
import numpy as np

CLIENTES = [
    {"edad": 20, "salario": 30, "compras_previas": 0, "compra": 0},
    {"edad": 22, "salario": 28, "compras_previas": 1, "compra": 0},
    {"edad": 25, "salario": 32, "compras_previas": 0, "compra": 0},
    {"edad": 28, "salario": 35, "compras_previas": 1, "compra": 0},
    {"edad": 35, "salario": 45, "compras_previas": 3, "compra": 1},
    {"edad": 38, "salario": 48, "compras_previas": 2, "compra": 1},
    {"edad": 40, "salario": 50, "compras_previas": 4, "compra": 1},
    {"edad": 45, "salario": 55, "compras_previas": 5, "compra": 1},
    {"edad": 30, "salario": 40, "compras_previas": 2, "compra": 1},
    {"edad": 24, "salario": 33, "compras_previas": 0, "compra": 0},
    {"edad": 50, "salario": 60, "compras_previas": 6, "compra": 1},
    {"edad": 26, "salario": 31, "compras_previas": 1, "compra": 0},
]

NOMBRES_VARIABLES = ["Edad", "Salario", "Compras_Previas"]


def construir_dataset() -> tuple[np.ndarray, np.ndarray]:
    """Convierte la lista de clientes en los arrays X, Y para scikit-learn."""
    X = np.array([[c["edad"], c["salario"], c["compras_previas"]] for c in CLIENTES])
    Y = np.array([c["compra"] for c in CLIENTES])
    return X, Y
