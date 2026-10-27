"""Pruebas unitarias y de consistencia para ListaEnlazada y TablaHash."""

import math
import random
from estructuras import ListaEnlazada, TablaHash


def probar_busqueda_basica() -> None:
    """Verifica busquedas exitosas e infructuosas en lista y tabla."""
    # ListaEnlazada
    lista = ListaEnlazada()
    assert lista.buscar(1000000001) is None
    assert lista.tamano == 0

    lista.insertar(1000000001, "en bodega")
    lista.insertar(1000000002, "en reparto")

    assert lista.buscar(1000000001) == "en bodega"
    assert lista.buscar(1000000002) == "en reparto"
    assert lista.buscar(9999999999) is None
    assert lista.tamano == 2

    # TablaHash
    tabla = TablaHash(11)
    assert tabla.buscar(1000000001) is None
    assert tabla.tamano == 0

    tabla.insertar(1000000001, "en bodega")
    tabla.insertar(1000000002, "en reparto")

    assert tabla.buscar(1000000001) == "en bodega"
    assert tabla.buscar(1000000002) == "en reparto"
    assert tabla.buscar(9999999999) is None
    assert tabla.tamano == 2
    assert math.isclose(tabla.factor_carga(), 2 / 11)


def probar_colision_forzada() -> None:
    """Verifica el manejo de colisiones con m = 7 y las guias 10, 24 y 17."""
    tabla = TablaHash(7)
    guias_colision = (10, 24, 17)

    for g in guias_colision:
        assert tabla.hash(g) == 3, f"La guia {g} no cayo en la casilla 3"
        tabla.insertar(g, "en bodega")

    # Verificar recuperacion de todos los elementos colisionados
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"

    # Busqueda infructuosa
    assert tabla.buscar(99) is None

    # Verificar tamano de la casilla con colisiones
    assert tabla.casillas[3].tamano == 3
    for indice in range(7):
        if indice != 3:
            assert tabla.casillas[indice].tamano == 0

    # Verificar tamano total y factor de carga
    assert tabla.tamano == 3
    assert math.isclose(tabla.factor_carga(), 3 / 7)


def probar_colecciones_aleatorias(num_colecciones: int = 25) -> None:
    """Verifica equivalencia entre lista y tabla en colecciones aleatorias.

    Args:
        num_colecciones: numero de colecciones aleatorias a evaluar.
    """
    generador = random.Random(42)
    estados = ("en bodega", "en reparto", "entregado", "cancelado")

    for i in range(num_colecciones):
        tamano = generador.randint(30, 150)
        m = generador.choice([7, 13, 19, 31, 53, 97])
        lista = ListaEnlazada()
        tabla = TablaHash(m)

        datos: dict[int, str] = {}
        while len(datos) < tamano:
            guia = generador.randint(10**9, 10**10 - 1)
            estado = generador.choice(estados)
            datos[guia] = estado

        # Insercion en ambas estructuras
        for guia, estado in datos.items():
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        assert lista.tamano == tamano
        assert tabla.tamano == tamano
        assert math.isclose(tabla.factor_carga(), tamano / m)

        # Verificacion de guias existentes
        for guia, estado_esperado in datos.items():
            res_lista = lista.buscar(guia)
            res_tabla = tabla.buscar(guia)
            assert res_lista == estado_esperado
            assert res_tabla == estado_esperado
            assert res_lista == res_tabla

        # Verificacion de guias inexistentes
        inexistentes_probadas = 0
        while inexistentes_probadas < 30:
            candidata = generador.randint(10**9, 10**10 - 1)
            if candidata not in datos:
                assert lista.buscar(candidata) is None
                assert tabla.buscar(candidata) is None
                inexistentes_probadas += 1


def main() -> None:
    """Ejecuta toda la suite de pruebas unitarias."""
    print("Iniciando pruebas unitarias de estructuras.py...")
    probar_busqueda_basica()
    print("  [OK] Busqueda basica (exitosa e infructuosa)")

    probar_colision_forzada()
    print("  [OK] Colision forzada (m=7, guias 10, 24, 17 en casilla 3)")

    probar_colecciones_aleatorias(25)
    print("  [OK] 25 colecciones aleatorias (equivalencia total lista vs tabla)")

    print("\nTodas las pruebas pasaron exitosamente.")


if __name__ == "__main__":
    main()
