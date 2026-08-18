"""Modulo para el calculo de estadisticas y promedios.

Este script aplica convenciones de estilo PEP 8 y type hints sobre
el algoritmo basico de calculo de promedio.
"""


def calcular_promedio(numeros: list[float | int]) -> float:
    """Calcula la media aritmetica de una lista de numeros.

    Args:
        numeros: Lista que contiene valores numericos (enteros o flotantes).

    Returns:
        float: El promedio aritmetico de los elementos de la lista.

    Raises:
        ValueError: Si la lista proporcionada esta vacia.
    """
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacia.")

    suma_total: float = 0.0
    for valor in numeros:
        suma_total += valor

    return suma_total / len(numeros)


def main() -> None:
    """Punto de entrada principal del script."""
    lista_ejemplo: list[int] = [1, 2, 3, 4, 5]
    promedio: float = calcular_promedio(lista_ejemplo)
    print(f"El promedio de la lista {lista_ejemplo} es: {promedio}")


if __name__ == "__main__":
    main()
