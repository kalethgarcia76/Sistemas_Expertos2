
def interpretar_salida_case(probabilidad: float) -> str:
    match True:
        case _ if probabilidad >= 0.9:
            etiqueta = "Rechazo muy probable"
        case _ if probabilidad >= 0.7:
            etiqueta = "Rechazo probable"
        case _ if probabilidad >= 0.3:
            etiqueta = "Zona de incertidumbre (revisión manual recomendada)"
        case _ if probabilidad >= 0.1:
            etiqueta = "Aprobación probable"
        case _:
            etiqueta = "Aprobación muy probable"
    return f"{etiqueta} (probabilidad={probabilidad:.4f})"


def describir_arquitectura_case(n_entradas: int, n_ocultas: int, n_salida: int) -> str:
    """
    Reconoce, por la FORMA exacta de la tupla, si la arquitectura
    corresponde a un patrón típico y conocido en la industria.
    """
    match (n_entradas, n_ocultas, n_salida):
        case (n_e, n_o, 1) if n_o >= n_e:
            return (
                f"Arquitectura de clasificación BINARIA ({n_e}->{n_o}->1): "
                "1 sola neurona de salida con Sigmoide es el patrón estándar "
                "para problemas de sí/no."
            )
        case (n_e, n_o, n_s) if n_s > 1:
            return (
                f"Arquitectura de clasificación MULTICLASE ({n_e}->{n_o}->{n_s}): "
                f"{n_s} neuronas de salida sugieren Softmax en vez de Sigmoide."
            )
        case (n_e, n_o, n_s) if n_o < n_e:
            return (
                f"Arquitectura tipo 'cuello de botella' ({n_e}->{n_o}->{n_s}): "
                "la capa oculta comprime la información — típico de autoencoders."
            )
        case _:
            return "Arquitectura sin patrón reconocido, pero válida."
