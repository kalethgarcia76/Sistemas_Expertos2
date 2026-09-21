
import numpy as np
from mlp_experto import (
    forward_pass,
    contar_parametros,
    interpretar_salida,
    interpretar_salida_case,
    describir_arquitectura_case,
)


def separador(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def demo_taller_analitico():
    separador("TALLER ANALÍTICO: CONTANDO PARÁMETROS")
    conteo = contar_parametros(n_entradas=3, n_ocultas=4, n_salida=1)
    print(f"1. Pesos (entrada -> oculta):   3 x 4 = {conteo.pesos_entrada_oculta}")
    print(f"2. Sesgos de la capa oculta:    {conteo.sesgos_oculta}")
    print(f"3. Pesos (oculta -> salida):    4 x 1 = {conteo.pesos_oculta_salida}")
    print(f"   Sesgo de la capa de salida:  {conteo.sesgos_salida}")
    print(f"4. TOTAL de parámetros entrenables: {conteo.total}")

    print(f"\nDescripción de la arquitectura (match/case): "
          f"{describir_arquitectura_case(3, 4, 1)}")


def demo_forward_pass():
    separador("TALLER DE LABORATORIO: EXPLORANDO LAS MATRICES")

    W1 = np.array([
        [0.1, 0.2, -0.3, 0.4],
        [-0.5, 0.6, 0.7, -0.8],
        [0.9, -0.1, 0.2, 0.3],
    ])
    b1 = np.array([0.1, -0.2, 0.3, -0.4])
    W2 = np.array([0.5, -0.6, 0.7, 0.8])
    b2 = np.array([-0.1])

    print("--- Paso 1: UN solo cliente ---")
    X_uno = np.array([0.5, 0.8, 0.2])
    resultado = forward_pass(X_uno, W1, b1, W2, b2)
    print(f"Z1 = {resultado['Z1']}")
    print(f"A1 (sigmoide aplicada) = {resultado['A1']}")
    print(f"Predicción final: {np.round(resultado['salida'][0], 4)}")
    print(f"\nInterpretación (módulo): {interpretar_salida(resultado['salida'][0])}")
    print(f"Interpretación (case):   {interpretar_salida_case(resultado['salida'][0])}")

    print("\n--- Paso 3-4: Reto Dimensional — DOS clientes en batch ---")
    X_lote = np.array([
        [0.5, 0.8, 0.2],
        [0.1, 0.9, 0.9],
    ])
    resultado_lote = forward_pass(X_lote, W1, b1, W2, b2)
    print(f"Z1 (2x4, uno por cliente):\n{resultado_lote['Z1']}")
    print(f"Predicciones finales: {np.round(resultado_lote['salida'].flatten(), 4)}")
    for i, prob in enumerate(resultado_lote["salida"].flatten(), start=1):
        print(f"  Cliente {i} -> {interpretar_salida_case(prob)}")

    print(
        "\nNota: NO tuvimos que cambiar W1, b1, W2 ni b2 para procesar 2 "
        "clientes en vez de 1 — np.dot() maneja el batch automáticamente. "
        "Ese es el poder del cálculo tensorial que menciona el PDF."
    )


if __name__ == "__main__":
    demo_taller_analitico()
    demo_forward_pass()
