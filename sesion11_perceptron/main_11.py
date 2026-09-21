
import numpy as np
from perceptron_experto import perceptron, obtener_pesos, obtener_pesos_case


def separador(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def demo_taller_analitico():
    separador("TALLER ANALÍTICO: CALCULANDO EL DISPARO")
    W = np.array([0.8, -0.5])
    b = -10
    X = np.array([50, 20])  # Ingresos=50, Deudas=20

    Z = np.dot(X, W) + b
    print(f"Z = (50 × 0.8) + (20 × -0.5) + (-10) = {Z}")

    resultado = perceptron(X, W, b)
    veredicto = "APRUEBA el crédito" if resultado == 1 else "RECHAZA el crédito"
    print(f"Función Escalón(Z={Z}) = {resultado} -> La neurona {veredicto}")
    print(
        "\nInterpretación: W2 es negativo porque cada dólar de deuda debe "
        "restarle puntos a la decisión — más deuda, menos probable la aprobación."
    )


def probar_compuerta(nombre: str, obtener_fn):
    print(f"\nCompuerta {nombre} (usando {obtener_fn.__name__}):")
    W, b = obtener_fn(nombre)
    for x1 in (0, 1):
        for x2 in (0, 1):
            entrada = np.array([x1, x2])
            salida = perceptron(entrada, W, b)
            print(f"  {nombre}({x1}, {x2}) = {salida}")


def demo_compuertas():
    separador("TALLER DE LABORATORIO: HACKEANDO LOS PESOS")

    # Verificamos que AND funciona igual en ambas versiones (módulo y case)
    probar_compuerta("AND", obtener_pesos)
    probar_compuerta("AND", obtener_pesos_case)

    # El Reto: resolver la Compuerta OR modificando manualmente W y b
    probar_compuerta("OR", obtener_pesos)
    probar_compuerta("OR", obtener_pesos_case)

    print(
        "\nPesos encontrados para OR: W=[1.0, 1.0], b=-0.5\n"
        "Verificación: con solo 1 entrada activa, Z = 1 - 0.5 = 0.5 >= 0 -> dispara 1.\n"
        "Con ambas entradas en 0, Z = -0.5 < 0 -> no dispara. ¡Funciona!"
    )


if __name__ == "__main__":
    demo_taller_analitico()
    demo_compuertas()
