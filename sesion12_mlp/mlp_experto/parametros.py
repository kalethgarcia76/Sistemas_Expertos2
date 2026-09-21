
from dataclasses import dataclass


@dataclass
class ConteoParametros:
    pesos_entrada_oculta: int
    sesgos_oculta: int
    pesos_oculta_salida: int
    sesgos_salida: int

    @property
    def total(self) -> int:
        return (
            self.pesos_entrada_oculta
            + self.sesgos_oculta
            + self.pesos_oculta_salida
            + self.sesgos_salida
        )


def contar_parametros(n_entradas: int, n_ocultas: int, n_salida: int) -> ConteoParametros:
    """
    Calcula los 4 componentes de una red de 1 capa oculta:
      - Pesos entre entrada y oculta: cada entrada se conecta con cada
        neurona oculta -> n_entradas * n_ocultas
      - Sesgos de la capa oculta: 1 por neurona -> n_ocultas
      - Pesos entre oculta y salida: n_ocultas * n_salida
      - Sesgos de la capa de salida: n_salida
    """
    return ConteoParametros(
        pesos_entrada_oculta=n_entradas * n_ocultas,
        sesgos_oculta=n_ocultas,
        pesos_oculta_salida=n_ocultas * n_salida,
        sesgos_salida=n_salida,
    )
