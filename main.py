from motor_experto import (
    MotorInferencia,
    REGLAS_FRAUDE,
    construir_hechos,
    REGLAS_MOTOCICLETA,
    HECHOS_INICIALES_MOTOCICLETA,
)


def separador(titulo: str):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


def demo_fraude():
    separador("TALLER DE LABORATORIO: MOTOR DE FRAUDE BANCARIO")
    motor = MotorInferencia(REGLAS_FRAUDE)

    # Caso 1: transacción sospechosa (monto alto + país extranjero)
    hechos_sospechosos = construir_hechos(
        monto_transaccion=7500,
        pais_transaccion="Extranjero",
        multiples_reintentos=True,
        tarjeta_reportada_robada=False,
    )
    resultado = motor.ejecutar(hechos_sospechosos)
    print("\n--- Caso 1: Transacción sospechosa ---")
    print(resultado.explicar())
    print("Memoria final:", resultado.hechos_finales)
    print("¿Se bloquea la tarjeta?", resultado.hechos_finales.get("bloquear_tarjeta", False))

    # Caso 2: transacción normal (no debería disparar ninguna regla)
    hechos_normales = construir_hechos(
        monto_transaccion=800,
        pais_transaccion="Nacional",
        multiples_reintentos=False,
        tarjeta_reportada_robada=False,
    )
    resultado_normal = motor.ejecutar(hechos_normales)
    print("\n--- Caso 2: Transacción normal ---")
    print(resultado_normal.explicar())
    print("Memoria final:", resultado_normal.hechos_finales)
    print("¿Se bloquea la tarjeta?", resultado_normal.hechos_finales.get("bloquear_tarjeta", False))

    # Caso 3 (bonus): tarjeta reportada como robada, sin importar el monto
    hechos_robo = construir_hechos(
        monto_transaccion=100,
        pais_transaccion="Nacional",
        multiples_reintentos=False,
        tarjeta_reportada_robada=True,
    )
    resultado_robo = motor.ejecutar(hechos_robo)
    print("\n--- Caso 3 (bonus): Tarjeta reportada robada ---")
    print(resultado_robo.explicar())
    print("Memoria final:", resultado_robo.hechos_finales)


def demo_motocicleta():
    separador("VERIFICACIÓN POR CÓDIGO: TALLER ANALÍTICO 2 (MOTOCICLETA)")
    motor = MotorInferencia(REGLAS_MOTOCICLETA)
    resultado = motor.ejecutar(HECHOS_INICIALES_MOTOCICLETA)
    print(resultado.explicar())
    print("Memoria final:", resultado.hechos_finales)
    print(
        "\nCoincide con la traza manual del taller: "
        "Motor+Ruedas -> Motocicleta -> Casco -> Permiso Denegado"
    )


if __name__ == "__main__":
    demo_fraude()
    demo_motocicleta()