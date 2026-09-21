
def describir_kernel_case(nombre: str) -> str:
    match nombre:
        case "linear":
            return "Recta rígida: solo separa clases perfectamente divisibles con una línea."
        case "rbf":
            return "Frontera curva: puede 'envolver' clases mezcladas o anidadas (anillos, círculos)."
        case "poly":
            return "Frontera polinomial: un punto intermedio de flexibilidad."
        case _:
            return f"Kernel '{nombre}' no reconocido."


def recomendar_kernel_case(escenario: str) -> str:
    """
    Responde la Reflexión del Taller de Laboratorio: ¿en qué escenario
    del mundo real un kernel lineal fallaría por completo?
    """
    texto = escenario.lower()

    match True:
        case _ if any(p in texto for p in ("anillo", "círculo", "concéntrico", "rodead")):
            return (
                "RBF recomendado: el patrón descrito ('anillo'/'rodeado') es el caso "
                "clásico donde una clase queda completamente encerrada dentro de otra. "
                "Ninguna línea recta puede separar un círculo interior de uno exterior."
            )
        case _ if any(p in texto for p in ("facial", "rostro", "imagen médica", "tumor")):
            return (
                "RBF recomendado: en reconocimiento facial o imágenes médicas, las "
                "fronteras entre clases casi nunca son líneas rectas en el espacio "
                "de características — el kernel lineal subajustaría el problema."
            )
        case _ if any(p in texto for p in ("lineal", "recta", "simple", "separable")):
            return "Kernel 'linear' es suficiente: el escenario describe clases claramente separables."
        case _:
            return "No hay suficiente información para recomendar un kernel con certeza."
