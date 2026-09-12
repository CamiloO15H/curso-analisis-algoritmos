"""Generadores de lotes de registros para los escenarios de Tamiza.

Genera listas de tamano n con indices de riesgo unicos para los 3 escenarios:
- Escenario A: Aleatorio
- Escenario B: Casi ordenado (98% ordenado descendente, 2% desordenado al final)
- Escenario C: Orden inverso (ordenado ascendente, de menor a mayor)
"""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador pseudoaleatorio para reproducibilidad.

    Returns:
        list[int]: Lista de n enteros distintos desordenados.
    """
    rng = random.Random(semilla)
    datos: list[int] = list(range(n))
    rng.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador pseudoaleatorio.

    Returns:
        list[int]: Lista de n enteros distintos con el primer 98% en orden
        descendente y el 2% final desordenado.
    """
    rng = random.Random(semilla)
    n_ordenado: int = int(n * 0.98)
    n_desordenado: int = n - n_ordenado

    # Primer 98% ordenado de mayor a menor
    parte_ordenada: list[int] = list(range(n - 1, n - 1 - n_ordenado, -1))
    # 2% restante desordenado
    parte_desordenada: list[int] = list(range(n_desordenado))
    rng.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Al requerir Tamiza orden descendente (mayor a menor), el orden inverso
    corresponde a una lista ordenada ascendentemente (menor a mayor).

    Args:
        n: Cantidad de registros del lote.

    Returns:
        list[int]: Lista de n enteros distintos de menor a mayor.
    """
    return list(range(n))
