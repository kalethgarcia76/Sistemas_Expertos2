
from dataclasses import dataclass, field
from .membresia import ConjuntoDifuso


@dataclass
class ResultadoFuzzificacion:
    valor: float
    grados: dict  # {"Novato": 0.4, "Intermedio": 0.6, "Experto": 0.0}
    categoria_dominante: str
    grado_dominante: float

    def __str__(self) -> str:
        detalle = ", ".join(f"{nombre}={grado:.2f}" for nombre, grado in self.grados.items())
        return (
            f"Experiencia = {self.valor} años -> {detalle} "
            f"=> Categoría dominante: {self.categoria_dominante} "
            f"({self.grado_dominante * 100:.0f}%)"
        )


def evaluar_experiencia(anios: float, conjuntos: list[ConjuntoDifuso]) -> ResultadoFuzzificacion:
    """
    Calcula el grado de membresía de `anios` en cada conjunto difuso y
    determina cuál es el dominante (mayor grado de verdad).

    Nota: si dos categorías empatan en el grado máximo (zona de
    transición, ej. justo en el vértice compartido entre dos
    triángulos), se reporta la primera en el orden de la lista. En un
    sistema difuso completo esta ambigüedad normalmente se resuelve
    combinando ambas categorías en la etapa de "defuzzificación", pero
    para este taller basta con max().
    """
    grados = {conjunto.nombre: conjunto.grado(anios) for conjunto in conjuntos}
    categoria_dominante = max(grados, key=grados.get)
    grado_dominante = grados[categoria_dominante]

    return ResultadoFuzzificacion(
        valor=anios,
        grados=grados,
        categoria_dominante=categoria_dominante,
        grado_dominante=grado_dominante,
    )


def evaluar_conductores(lista_anios: list[float], conjuntos: list[ConjuntoDifuso]) -> list[ResultadoFuzzificacion]:
    """Evalúa una lista completa de conductores (uno por cada valor de años)."""
    return [evaluar_experiencia(anios, conjuntos) for anios in lista_anios]
