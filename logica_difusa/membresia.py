
from dataclasses import dataclass


def membresia_triangular(x: float, a: float, b: float, c: float) -> float:
    """
    Implementación computacional de la función triangular a trozos:
        μ(x) = 0                  si x <= a
        μ(x) = (x - a) / (b - a)  si a < x <= b
        μ(x) = (c - x) / (c - b)  si b < x < c
        μ(x) = 0                  si x >= c
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:  # b < x < c
        return (c - x) / (c - b)


@dataclass
class ConjuntoDifuso:
    """Un conjunto difuso triangular con nombre (ej. 'Novato')."""

    nombre: str
    a: float
    b: float
    c: float

    def __post_init__(self):
        # Validación: un triángulo mal definido produciría divisiones
        # por cero o resultados sin sentido dentro de membresia_triangular.
        if not (self.a <= self.b <= self.c):
            raise ValueError(
                f"Conjunto '{self.nombre}': los vértices deben cumplir a <= b <= c "
                f"(recibido a={self.a}, b={self.b}, c={self.c})"
            )

    def grado(self, x: float) -> float:
        """Grado de membresía de x en este conjunto difuso."""
        return membresia_triangular(x, self.a, self.b, self.c)
