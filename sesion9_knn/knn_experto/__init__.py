from .distancia import distancia_euclidiana
from .dataset_clientes import construir_dataset, NOMBRES_VARIABLES, CLIENTES
from .entrenamiento import entrenar_knn, predecir
from .votacion_modulo import votar_mayoria
from .votacion_case import votar_mayoria_binaria
from .interpretacion_case import interpretar_dimensionalidad

__all__ = [
    "distancia_euclidiana",
    "construir_dataset",
    "NOMBRES_VARIABLES",
    "CLIENTES",
    "entrenar_knn",
    "predecir",
    "votar_mayoria",
    "votar_mayoria_binaria",
    "interpretar_dimensionalidad",
]
