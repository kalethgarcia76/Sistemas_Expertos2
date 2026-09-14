"""
Requiere: scikit-learn y numpy
    pip install scikit-learn numpy --break-system-packages

"""

from experto_automatico import (
    construir_dataset,
    NOMBRES_VARIABLES,
    CLIENTES,
    entrenar_arbol,
    extraer_reglas,
    predecir_cliente,
)


def separador(titulo: str):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


def main():
    separador("PASO 2: DATASET DE MARKETING (12 clientes históricos)")
    for i, c in enumerate(CLIENTES, start=1):
        resultado = "HIZO CLIC" if c["hizo_clic"] == 1 else "lo ignoró"
        print(f"  Cliente {i:2d}: Edad={c['edad']:2d}, Horas_Online={c['horas_online']}, "
              f"Compras_Previas={c['compras_previas']} -> {resultado}")

    X, Y = construir_dataset()

    separador("PASO 3: ENTRENAMIENTO DEL ÁRBOL DE DECISIÓN (CART)")
    arbol = entrenar_arbol(X, Y, max_depth=3)
    print("Modelo entrenado con .fit(X, Y). El algoritmo analizó Entropía y")
    print("Ganancia de Información en cada columna para construir el árbol.")

    separador("PASO 4: BASE DE REGLAS APRENDIDA AUTOMÁTICAMENTE")
    reglas_texto = extraer_reglas(arbol, NOMBRES_VARIABLES)
    print(reglas_texto)

    separador("PASO 5: DISCUSIÓN — PROBANDO CLIENTES NUEVOS")
    casos_nuevos = [
        {"edad": 23, "horas_online": 6, "compras_previas": 1},  # parecido a un "sí"
        {"edad": 58, "horas_online": 1, "compras_previas": 0},  # parecido a un "no"
    ]
    for caso in casos_nuevos:
        prediccion, probabilidad = predecir_cliente(arbol, **caso)
        veredicto = "HARÍA CLIC" if prediccion == 1 else "LO IGNORARÍA"
        print(
            f"Cliente nuevo {caso} -> Predicción: {veredicto} "
            f"(confianza del modelo: {probabilidad * 100:.0f}%)"
        )

    print(
        "\nPregunta para la discusión grupal: ¿las reglas impresas arriba "
        "tienen sentido comercial? ¿Coinciden con la intuición de que "
        "clientes jóvenes con muchas horas online tienden a hacer clic?"
    )


if __name__ == "__main__":
    main()
