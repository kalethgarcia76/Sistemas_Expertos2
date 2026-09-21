
def votar_mayoria_binaria(votos: list[int]) -> int:
    """
    Cuenta votos de "Compra" (1) vs "No Compra" (0) para K=3 y decide
    por pattern matching exacto sobre la tupla de conteos.
    """
    compras = votos.count(1)
    no_compras = votos.count(0)

    match (compras, no_compras):
        case (3, 0) | (2, 1):
            return 1  # mayoría de "Compra"
        case (0, 3) | (1, 2):
            return 0  # mayoría de "No Compra"
        case _:
            raise ValueError(
                f"Empate o combinación inválida para K=3: compras={compras}, no_compras={no_compras}"
            )
