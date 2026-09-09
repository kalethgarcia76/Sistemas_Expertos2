from dataclasses import dataclass, field
from .regla import Regla


@dataclass
class ResultadoInferencia:
    hechos_finales: dict
    traza: list[str] = field(default_factory=list)

    def explicar(self) -> str:
        if not self.traza:
            return "Ninguna regla se disparó. La memoria no cambió."
        return "\n".join(self.traza)


class MotorInferencia:
    """
    Motor de encadenamiento hacia adelante, dirigido por datos.

    Estrategia de resolución de conflictos: FIFO por orden de la lista
    de reglas (la primera regla de la lista que cumpla condiciones y
    aporte un hecho nuevo se dispara primero en cada pasada). Es la
    misma estrategia usada en el motor de la Sección 2 del PDF.
    """

    def __init__(self, reglas: list[Regla]):
        self.reglas = reglas

    def ejecutar(self, hechos_iniciales: dict) -> ResultadoInferencia:
        hechos = dict(hechos_iniciales)  # nunca mutar el diccionario original
        traza: list[str] = []
        hay_hechos_nuevos = True
        ciclo = 0

        while hay_hechos_nuevos:
            ciclo += 1
            hay_hechos_nuevos = False

            for regla in self.reglas:
                if not regla.condiciones_cumplidas(hechos):
                    continue

                nuevos = regla.hechos_nuevos(hechos)
                if not nuevos:
                    # La regla "vuelve a cumplirse" pero ya no aporta nada:
                    # el motor no la vuelve a disparar (evita bucles infinitos).
                    continue

                hechos.update(nuevos)
                hay_hechos_nuevos = True
                for clave, valor in nuevos.items():
                    traza.append(f"[Ciclo {ciclo}] {regla.id} dispara -> {clave} = {valor}")

        traza.append(f"Motor detenido: punto fijo alcanzado en el ciclo {ciclo}.")
        return ResultadoInferencia(hechos_finales=hechos, traza=traza)
