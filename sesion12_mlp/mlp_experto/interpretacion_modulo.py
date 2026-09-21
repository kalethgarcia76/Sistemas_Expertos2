
UMBRALES = [
    (0.9, "Rechazo muy probable"),
    (0.7, "Rechazo probable"),
    (0.3, "Zona de incertidumbre (revisión manual recomendada)"),
    (0.1, "Aprobación probable"),
    (0.0, "Aprobación muy probable"),
]


def interpretar_salida(probabilidad: float) -> str:
    """
    Nota: en este ejemplo, la neurona de salida representa la
    probabilidad de "fraude"/"rechazo" (valores cercanos a 1 = más
    riesgo), así que umbrales altos = más certeza de rechazo.
    """
    for umbral, etiqueta in UMBRALES:
        if probabilidad >= umbral:
            return f"{etiqueta} (probabilidad={probabilidad:.4f})"
    return f"Sin clasificar (probabilidad={probabilidad:.4f})"
