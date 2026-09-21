
DESCRIPCION_KERNELS = {
    "linear": "Traza una recta (o hiperplano) rígida. Ideal cuando las clases "
              "son separables con una línea recta.",
    "rbf": "Proyecta los datos a una dimensión superior para poder trazar "
           "fronteras curvas. Ideal cuando los datos NO son separables "
           "linealmente (ej. un anillo concéntrico).",
    "poly": "Frontera polinomial: más flexible que 'linear' pero menos "
            "costosa computacionalmente que 'rbf'.",
}


def describir_kernel(nombre: str) -> str:
    return DESCRIPCION_KERNELS.get(nombre, f"Kernel '{nombre}' no documentado.")
