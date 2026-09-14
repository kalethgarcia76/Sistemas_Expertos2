
import numpy as np
from .centroide import centro_de_gravedad

# Datos EXACTOS del Taller Analítico (página 2 del PDF)
X_TALLER = np.array([10, 20, 30, 40])
MU_TALLER = np.array([0.2, 0.8, 0.8, 0.0])

# Resultado esperado calculado a mano:
#   numerador = 10*0.2 + 20*0.8 + 30*0.8 + 40*0.0 = 42
#   denominador = 0.2 + 0.8 + 0.8 + 0.0 = 1.8
#   COG = 42 / 1.8 = 23.333...
COG_ESPERADO = 42 / 1.8


def validar_contra_taller_analitico(tolerancia: float = 1e-9) -> tuple[bool, float]:
    """
    Ejecuta centro_de_gravedad() con los datos del taller analítico y
    compara contra el resultado calculado a mano.

    Devuelve (coincide: bool, valor_calculado: float).
    """
    resultado = centro_de_gravedad(X_TALLER, MU_TALLER)
    coincide = abs(resultado - COG_ESPERADO) < tolerancia
    return coincide, resultado
