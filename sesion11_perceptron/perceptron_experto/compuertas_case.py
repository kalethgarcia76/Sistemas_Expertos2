
import numpy as np


def obtener_pesos_case(nombre: str) -> tuple:
    """Devuelve (W, b) para la compuerta lógica pedida, vía match/case."""
    match nombre.upper():
        case "AND":
            return np.array([0.5, 0.5]), -0.8
        case "OR":
            return np.array([1.0, 1.0]), -0.5
        case "NAND":
            return np.array([-0.5, -0.5]), 0.8
        case _:
            raise ValueError(f"Compuerta '{nombre}' no reconocida (usa AND, OR o NAND)")
