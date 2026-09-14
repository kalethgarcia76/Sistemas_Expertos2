"toca instalar este comando para correr el programa    pip install numpy --break-system-packages"
from defuzzificacion import (
    validar_contra_taller_analitico,
    X_TALLER,
    MU_TALLER,
    calcular_fuerza_frenado,
)


def separador(titulo: str):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


def demo_validacion():
    separador("PASOS 1-2: VALIDACIÓN CONTRA EL TALLER ANALÍTICO")
    print(f"x  = {X_TALLER.tolist()}")
    print(f"mu = {MU_TALLER.tolist()}")

    coincide, resultado = validar_contra_taller_analitico()

    print(f"\nNumerador  Σ(x·μ(x)) = {sum(x * m for x, m in zip(X_TALLER, MU_TALLER))}")
    print(f"Denominador Σμ(x)     = {sum(MU_TALLER)}")
    print(f"COG calculado por la función = {resultado:.4f}")
    print(f"COG calculado a mano          = 23.3333")
    print(f"\n¿Coincide con el cálculo manual? {'SÍ ✔' if coincide else 'NO ✘'}")
    print(f"=> Descuento exacto (crisp) a otorgar: {resultado:.2f}%")


def demo_frenado():
    separador("PASOS 3-4: SISTEMA DE FRENADO AUTOMÁTICO")
    x, curva, fuerza_crisp = calcular_fuerza_frenado(centro=70.0, sigma=10.0, n_puntos=100)

    print(f"Universo de discurso: {len(x)} puntos entre {x[0]:.0f} y {x[-1]:.0f} Newtons")
    print("Curva de respuesta: Gaussiana centrada en 70 N (sigma = 10)")
    print(f"\n>>> Fuerza de frenado exacta (Crisp) = {fuerza_crisp:.4f} N")


if __name__ == "__main__":
    demo_validacion()
    demo_frenado()
