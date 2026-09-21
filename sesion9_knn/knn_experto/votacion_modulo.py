
from collections import Counter


def votar_mayoria(votos: list) -> int:
    """
    Recibe las etiquetas de los K vecinos más cercanos (ej. [0, 1, 1])
    y devuelve la clase ganadora por votación democrática.
    """
    conteo = Counter(votos)
    clase_ganadora, _ = conteo.most_common(1)[0]
    return clase_ganadora
