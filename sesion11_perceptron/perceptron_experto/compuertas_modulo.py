
import numpy as np

COMPUERTAS = {
    "AND": (np.array([0.5, 0.5]), -0.8),
    "OR": (np.array([1.0, 1.0]), -0.5),
    "NAND": (np.array([-0.5, -0.5]), 0.8),
}


def obtener_pesos(nombre: str) -> tuple:
    """Devuelve (W, b) para la compuerta lógica pedida."""
    if nombre not in COMPUERTAS:
        raise ValueError(f"Compuerta '{nombre}' no definida. Opciones: {list(COMPUERTAS)}")
    return COMPUERTAS[nombre]
