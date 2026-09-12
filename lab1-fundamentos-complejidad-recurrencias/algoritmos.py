"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1.

Este modulo contiene las implementaciones de Insertion Sort y Merge Sort
adaptadas para ordenar indices de riesgo de mayor a menor (orden descendente),
contando de forma exacta el numero de comparaciones entre elementos.
"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor riesgo (descendente). Trabaja sobre una copia
    de la lista para no mutar los datos originales.

    Args:
        datos: Lista de indices de riesgo a ordenar.

    Returns:
        tuple[list[int], int]: Lista ordenada y el numero total de
        comparaciones realizadas entre elementos de la lista.
    """
    copia: list[int] = list(datos)
    n: int = len(copia)
    comparaciones: int = 0

    for i in range(1, n):
        clave: int = copia[i]
        j: int = i - 1

        while j >= 0:
            comparaciones += 1
            # Tamiza requiere de MAYOR a MENOR: si la clave es mayor, desplaza a la derecha
            if copia[j] < clave:
                copia[j + 1] = copia[j]
                j -= 1
            else:
                break
        copia[j + 1] = clave

    return copia, comparaciones


def _merge(
    izquierda: list[int],
    derecha: list[int]
) -> tuple[list[int], int]:
    """Combina dos sublistas ordenadas en orden descendente.

    Args:
        izquierda: Primera sublista ordenada descendentemente.
        derecha: Segunda sublista ordenada descendentemente.

    Returns:
        tuple[list[int], int]: Sublista combinada y comparaciones realizadas.
    """
    resultado: list[int] = []
    i: int = 0
    j: int = 0
    comparaciones: int = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor riesgo (descendente). Implementa divide,
    conquista y combina de manera recursiva sin modificar la lista original.

    Args:
        datos: Lista de indices de riesgo a ordenar.

    Returns:
        tuple[list[int], int]: Lista ordenada y el total acumulado de
        comparaciones realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return list(datos), 0

    medio: int = len(datos) // 2
    izq_ordenada, comp_izq = merge_sort(datos[:medio])
    der_ordenada, comp_der = merge_sort(datos[medio:])

    mezclada, comp_merge = _merge(izq_ordenada, der_ordenada)
    return mezclada, comp_izq + comp_der + comp_merge
