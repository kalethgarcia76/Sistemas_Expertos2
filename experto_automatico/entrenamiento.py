
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text


def entrenar_arbol(X: np.ndarray, Y: np.ndarray, max_depth: int = 3) -> DecisionTreeClassifier:
    """
    Entrena un DecisionTreeClassifier sobre el dataset histórico.

    `max_depth` limita qué tan "profundo" (complejo) puede ser el árbol.
    Un árbol muy profundo puede memorizar el dataset (sobreajuste) en
    vez de aprender un patrón generalizable — por eso se deja como
    parámetro configurable en vez de fijo.
    """
    arbol = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    arbol.fit(X, Y)
    return arbol


def extraer_reglas(arbol: DecisionTreeClassifier, nombres_variables: list[str]) -> str:
    """
    Traduce el árbol entrenado a texto legible (Base de Reglas del
    Sistema Experto), usando export_text de scikit-learn.
    """
    return export_text(arbol, feature_names=nombres_variables)


def predecir_cliente(arbol: DecisionTreeClassifier, edad: int, horas_online: int,
                      compras_previas: int) -> tuple[int, float]:
    """
    Usa el árbol ya entrenado para predecir si un cliente NUEVO haría
    clic o no, junto con la probabilidad estimada por el modelo.
    """
    cliente = np.array([[edad, horas_online, compras_previas]])
    prediccion = int(arbol.predict(cliente)[0])
    probabilidad = float(arbol.predict_proba(cliente)[0][prediccion])
    return prediccion, probabilidad
