"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for i in range(n):
        suma_acumulada = 0
        for j in range(i, n):
            suma_acumulada += valores[j]
            if suma_acumulada > mejor_suma:
                mejor_suma = suma_acumulada
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    mejor_inicio = medio
    suma_izq = 0
    mejor_suma_izq = float("-inf")
    for i in range(medio, inicio - 1, -1):
        suma_izq += valores[i]
        if suma_izq > mejor_suma_izq:
            mejor_suma_izq = suma_izq
            mejor_inicio = i

    mejor_fin = medio + 1
    suma_der = 0
    mejor_suma_der = float("-inf")
    for j in range(medio + 1, fin + 1):
        suma_der += valores[j]
        if suma_der > mejor_suma_der:
            mejor_suma_der = suma_der
            mejor_fin = j

    return mejor_inicio, mejor_fin, mejor_suma_izq + mejor_suma_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izq_inicio, izq_fin, izq_suma = subarreglo_maximo(valores, inicio, medio)
    der_inicio, der_fin, der_suma = subarreglo_maximo(valores, medio + 1, fin)
    cruz_inicio, cruz_fin, cruz_suma = suma_cruzada(
        valores, inicio, medio, fin
    )

    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return izq_inicio, izq_fin, izq_suma
    if der_suma >= izq_suma and der_suma >= cruz_suma:
        return der_inicio, der_fin, der_suma
    return cruz_inicio, cruz_fin, cruz_suma
