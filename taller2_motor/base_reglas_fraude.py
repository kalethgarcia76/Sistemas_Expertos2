from .regla import Regla


def construir_hechos(monto_transaccion: float, pais_transaccion: str,
                      multiples_reintentos: bool,
                      tarjeta_reportada_robada: bool) -> dict:
    """Convierte datos crudos de una transacción en hechos booleanos."""
    return {
        "monto_alto": monto_transaccion > 5000,
        "pais_extranjero": pais_transaccion == "Extranjero",
        "multiples_reintentos": multiples_reintentos,
        "tarjeta_reportada_robada": tarjeta_reportada_robada,
    }


# Base de Reglas (4 reglas, en orden de precedencia de evaluación)
REGLAS_FRAUDE = [
    Regla(
        id="R1",
        condiciones={"monto_alto": True},
        conclusion={"transaccion_inusual": True},
    ),
    Regla(
        id="R2",
        condiciones={"transaccion_inusual": True, "pais_extranjero": True},
        conclusion={"bloquear_tarjeta": True},
    ),
    Regla(
        id="R3",
        condiciones={"multiples_reintentos": True},
        conclusion={"transaccion_inusual": True},
    ),
    Regla(
        id="R4",
        condiciones={"tarjeta_reportada_robada": True},
        conclusion={"bloquear_tarjeta": True, "alerta_seguridad": True},
    ),
]
