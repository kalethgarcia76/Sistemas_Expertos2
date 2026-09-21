
from svm_experto import (
    X_BASE,
    Y_BASE,
    agregar_punto_conflictivo,
    entrenar_svm,
    obtener_vectores_soporte,
    predecir_punto,
    describir_kernel,
    describir_kernel_case,
    recomendar_kernel_case,
)


def separador(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def demo_kernel_lineal():
    separador("PASO 1: KERNEL LINEAL SOBRE EL DATASET ORIGINAL")
    modelo = entrenar_svm(X_BASE, Y_BASE, kernel="linear")
    print("Vectores de Soporte encontrados por la IA:")
    print(obtener_vectores_soporte(modelo))
    print(f"\nDescripción (módulo): {describir_kernel('linear')}")
    print(f"Descripción (case):   {describir_kernel_case('linear')}")

    pred = predecir_punto(modelo, [5, 4])
    print(f"\nPredicción para el punto [5,4]: Clase {pred}")


def demo_punto_conflictivo():
    separador("PASOS 2-3: AGREGANDO UN PUNTO CONFLICTIVO Y REENTRENANDO LINEAL")
    X_nuevo, Y_nuevo = agregar_punto_conflictivo(X_BASE, Y_BASE)
    print("Nuevo dataset con el punto [5,5] etiquetado como Clase A (0):")
    print(X_nuevo)

    modelo_lineal = entrenar_svm(X_nuevo, Y_nuevo, kernel="linear")
    aciertos = sum(modelo_lineal.predict(X_nuevo) == Y_nuevo)
    print(f"\nCon kernel LINEAL: el modelo clasifica correctamente "
          f"{aciertos}/{len(Y_nuevo)} puntos de entrenamiento.")
    print("(Si aciertos < total, la recta se vio 'forzada' y no logra separar bien)")

    return X_nuevo, Y_nuevo


def demo_kernel_rbf(X_nuevo, Y_nuevo):
    separador("PASO 4: CAMBIANDO A KERNEL RBF")
    modelo_rbf = entrenar_svm(X_nuevo, Y_nuevo, kernel="rbf")
    aciertos = sum(modelo_rbf.predict(X_nuevo) == Y_nuevo)
    print(f"Con kernel RBF: el modelo clasifica correctamente "
          f"{aciertos}/{len(Y_nuevo)} puntos de entrenamiento.")
    print(f"\nDescripción (módulo): {describir_kernel('rbf')}")
    print(f"Descripción (case):   {describir_kernel_case('rbf')}")

    pred = predecir_punto(modelo_rbf, [5, 4])
    print(f"\nPredicción para el punto [5,4] con RBF: Clase {pred}")


def demo_reflexion():
    separador("PASO 5: REFLEXIÓN (match/case sobre el escenario en texto libre)")
    escenarios = [
        "Un sistema de reconocimiento facial que debe distinguir rostros",
        "Detección de un tumor rodeado completamente por tejido sano",
        "Clasificar correos como spam vs no-spam con palabras claramente separables",
    ]
    for escenario in escenarios:
        print(f"\nEscenario: \"{escenario}\"")
        print(f"  -> {recomendar_kernel_case(escenario)}")


if __name__ == "__main__":
    demo_kernel_lineal()
    X_nuevo, Y_nuevo = demo_punto_conflictivo()
    demo_kernel_rbf(X_nuevo, Y_nuevo)
    demo_reflexion()
