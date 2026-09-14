
from logica_difusa import CONJUNTOS_EXPERIENCIA, evaluar_conductores


def main():
    anios_conductores = [3, 6, 12]

    print("=" * 70)
    print("ANÁLISIS DIFUSO — EXPERIENCIA DE CONDUCTORES")
    print("=" * 70)
    print("\nConjuntos difusos definidos:")
    for conjunto in CONJUNTOS_EXPERIENCIA:
        print(f"  - {conjunto.nombre}: triángulo ({conjunto.a}, {conjunto.b}, {conjunto.c})")

    resultados = evaluar_conductores(anios_conductores, CONJUNTOS_EXPERIENCIA)

    print("\nResultados por conductor:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"\nConductor {i}:")
        for nombre, grado in resultado.grados.items():
            print(f"  - Pertenece a {nombre.upper()} en un {grado * 100:.0f}%")
        print(
            f"  => Categoría dominante: {resultado.categoria_dominante} "
            f"(grado de verdad: {resultado.grado_dominante:.2f})"
        )


if __name__ == "__main__":
    main()
