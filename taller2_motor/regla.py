from dataclasses import dataclass


@dataclass
class Regla:
    id: str
    condiciones: dict   # ej. {"monto_alto": True, "pais_extranjero": True}
    conclusion: dict    # ej. {"bloquear_tarjeta": True}

    def condiciones_cumplidas(self, hechos: dict) -> bool:
        """
        Compuerta lógica AND: TODAS las condiciones deben coincidir
        exactamente con los hechos actuales de la memoria de trabajo.
        """
        return all(hechos.get(clave) == valor for clave, valor in self.condiciones.items())

    def hechos_nuevos(self, hechos: dict) -> dict:
        """Devuelve solo las claves de la conclusión que AÚN no existen en memoria."""
        return {
            clave: valor
            for clave, valor in self.conclusion.items()
            if clave not in hechos
        }
