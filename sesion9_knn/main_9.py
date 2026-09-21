
from knn_experto import (
    distancia_euclidiana,
    construir_dataset,
    NOMBRES_VARIABLES,
    CLIENTES,
    entrenar_knn,
    predecir,
    votar_mayoria,
    votar_mayoria_binaria,
    interpretar_dimensionalidad,
)


def separador(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def demo_taller_analitico():
    separador("TALLER ANALÍTICO: LA VOTACIÓN ESPACIAL")
    A, B, C = (20, 30), (40, 50), (35, 45)
    P = (30, 40)

    d_a, d_b, d_c = distancia_euclidiana(P, A), distancia_euclidiana(P, B), distancia_euclidiana(P, C)
    print(f"d(P,A) = {d_a:.2f}  (A -> NO COMPRA)")
    print(f"d(P,B) = {d_b:.2f}  (B -> COMPRA)")
    print(f"d(P,C) = {d_c:.2f}  (C -> COMPRA)")

    # K=1: el vecino más cercano es C
    print("\nK=1 -> vecino más cercano: C -> Clase = COMPRA")

    # K=3: votan los 3 (orden de cercanía no importa para la votación)
    votos = [0, 1, 1]  # A=NO(0), B=COMPRA(1), C=COMPRA(1)
    resultado_modulo = votar_mayoria(votos)
    resultado_case = votar_mayoria_binaria(votos)
    print(f"K=3 -> votos {votos} -> versión módulo (Counter): {resultado_modulo}")
    print(f"K=3 -> votos {votos} -> versión case (match/case): {resultado_case}")
    print(f"¿Coinciden ambas versiones? {'SÍ ✔' if resultado_modulo == resultado_case else 'NO ✘'}")
    print("¿Hubo cambio respecto a K=1? NO — ambos dan COMPRA.")


def demo_laboratorio():
    separador("TALLER DE LABORATORIO: CLASIFICADOR UNIVERSAL")
    print(f"Dataset ampliado: {len(CLIENTES)} clientes, columnas: {NOMBRES_VARIABLES}")

    X, Y = construir_dataset()
    nuevo_cliente = [33, 42, 2]  # Edad, Salario, Compras_Previas

    for k in (1, 5):
        modelo = entrenar_knn(X, Y, k=k)
        prediccion = predecir(modelo, nuevo_cliente)
        etiqueta = "COMPRA" if prediccion == 1 else "NO COMPRA"
        print(f"\nCon K={k}: predicción para {nuevo_cliente} -> {etiqueta}")


def demo_dimensionalidad():
    separador("PREGUNTA DE ANÁLISIS: LA MALDICIÓN DE LA DIMENSIONALIDAD")
    for n in (2, 3, 10, 50, 1000):
        print(f"\n{interpretar_dimensionalidad(n)}")


if __name__ == "__main__":
    demo_taller_analitico()
    demo_laboratorio()
    demo_dimensionalidad()
