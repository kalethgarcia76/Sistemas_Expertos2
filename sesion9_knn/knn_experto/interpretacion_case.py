
def interpretar_dimensionalidad(n_dimensiones: int) -> str:
    match True:
        case _ if n_dimensiones <= 3:
            return (
                f"{n_dimensiones} dimensiones: la distancia euclidiana es intuitiva "
                "y geométricamente confiable (como en el taller analítico)."
            )
        case _ if n_dimensiones <= 20:
            return (
                f"{n_dimensiones} dimensiones: la distancia sigue siendo útil, pero "
                "ya empieza a perder algo de poder discriminativo entre puntos."
            )
        case _ if n_dimensiones <= 100:
            return (
                f"{n_dimensiones} dimensiones: zona de riesgo. Empieza la 'Maldición "
                "de la Dimensionalidad': todos los puntos comienzan a parecer "
                "equidistantes entre sí, y KNN pierde capacidad de distinguir vecinos."
            )
        case _:
            return (
                f"{n_dimensiones} dimensiones (ej. píxeles de una imagen): la "
                "distancia euclidiana prácticamente deja de servir. Matemáticamente, "
                "en espacios de muy alta dimensión, la distancia entre el punto más "
                "cercano y el más lejano tiende a volverse insignificante en términos "
                "relativos — todos los vecinos 'se ven igual de lejos'. Por eso, para "
                "datos de alta dimensión (imágenes, texto) se prefiere reducir "
                "dimensiones primero (PCA, embeddings) o usar otros algoritmos."
            )
