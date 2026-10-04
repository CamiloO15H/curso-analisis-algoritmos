"""Bateria de pruebas unitarias para el subarreglo maximo.

Verifica la correccion de subarreglo_fuerza_bruta y subarreglo_maximo
frente a casos borde, casos de resultado conocido y listas aleatorias.
"""

import math
import os
import random
import sys

# Asegurar importacion robusta de subarreglo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subarreglo import (
    subarreglo_fuerza_bruta,
    suma_cruzada,
    subarreglo_maximo,
)


def test_serie_problema():
    """Verifica la serie de 8 dias de la cooperativa de tiendas."""
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    serie_copia = serie.copy()

    fb = subarreglo_fuerza_bruta(serie)
    dv = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert fb[2] == 17, f"Fuerza bruta fallo: esperado 17, obtenido {fb[2]}"
    assert dv[2] == 17, (
        f"Divide y venceras fallo: esperado 17, obtenido {dv[2]}"
    )
    assert serie == serie_copia, "La funcion no debe mutar la lista original"
    print("  [OK] Serie de 8 dias (situacion problema: suma = 17)")


def test_un_solo_elemento():
    """Verifica series con un unico elemento (positivo y negativo)."""
    serie_pos = [42.5]
    assert subarreglo_fuerza_bruta(serie_pos)[2] == 42.5
    assert subarreglo_maximo(serie_pos, 0, 0)[2] == 42.5
    assert subarreglo_fuerza_bruta(serie_pos)[:2] == (0, 0)
    assert subarreglo_maximo(serie_pos, 0, 0)[:2] == (0, 0)

    serie_neg = [-15.0]
    assert subarreglo_fuerza_bruta(serie_neg)[2] == -15.0
    assert subarreglo_maximo(serie_neg, 0, 0)[2] == -15.0
    assert subarreglo_fuerza_bruta(serie_neg)[:2] == (0, 0)
    assert subarreglo_maximo(serie_neg, 0, 0)[:2] == (0, 0)
    print("  [OK] Series de un solo elemento (positivo y negativo)")


def test_todos_negativos():
    """Verifica series donde todos los valores son negativos."""
    serie = [-24, -5, -12, -3, -8, -19]
    # El maximo subarreglo es el elemento menos negativo: -3 en el indice 3
    assert subarreglo_fuerza_bruta(serie)[2] == -3
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3
    print("  [OK] Serie con todos los valores negativos (suma = -3)")


def test_todos_positivos():
    """Verifica series donde todos los valores son positivos."""
    serie = [4, 7, 2, 9, 5]
    suma_esperada = sum(serie)  # 27
    assert subarreglo_fuerza_bruta(serie)[2] == suma_esperada
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == suma_esperada
    print(
        f"  [OK] Serie con todos los positivos (suma = {suma_esperada})"
    )


def test_caso_cruzado_especifico():
    """Verifica un caso donde la mejor racha cruza estrictamente el centro."""
    # Mitad izquierda: [ -10, 8, 7 ], Mitad derecha: [ 9, 6, -15 ]
    # medio = 2 (elemento 7). Tramo cruzado [8, 7, 9, 6] suma 30
    serie = [-10, 8, 7, 9, 6, -15]
    medio = (0 + len(serie) - 1) // 2  # 2

    cruz = suma_cruzada(serie, 0, medio, len(serie) - 1)
    assert cruz[2] == 30, (
        f"Suma cruzada fallo: esperado 30, obtenido {cruz[2]}"
    )
    assert cruz[0] == 1 and cruz[1] == 4

    fb = subarreglo_fuerza_bruta(serie)
    dv = subarreglo_maximo(serie, 0, len(serie) - 1)
    assert fb[2] == 30
    assert dv[2] == 30
    print("  [OK] Caso cruzado especifico (suma = 30)")


def test_listas_aleatorias(cantidad: int = 30):
    """Verifica que ambas soluciones coincidan en >= 20 listas aleatorias."""
    rng = random.Random(20261003)
    coincidencias = 0

    for i in range(cantidad):
        n = rng.randint(2, 200)
        serie = [rng.randint(-100, 100) for _ in range(n)]

        fb = subarreglo_fuerza_bruta(serie)
        dv = subarreglo_maximo(serie, 0, n - 1)

        # Se compara el valor de la suma en caso de empates en indices
        assert math.isclose(fb[2], dv[2], abs_tol=1e-7), (
            f"Discrepancia en lista {i} (n={n}): FB={fb[2]} != DV={dv[2]}"
        )
        coincidencias += 1

    print(f"  [OK] {coincidencias} listas aleatorias verificadas exitosamente")


if __name__ == "__main__":
    print("=== Ejecutando Bateria de Pruebas Unitarias (Lab 2) ===")
    test_serie_problema()
    test_un_solo_elemento()
    test_todos_negativos()
    test_todos_positivos()
    test_caso_cruzado_especifico()
    test_listas_aleatorias(30)
    print("=== Todas las pruebas pasaron satisfactoriamente (100% OK) ===")
