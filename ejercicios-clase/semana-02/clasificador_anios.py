"""Clasificador de anios bisiestos.

Complete las funciones siguiendo la especificacion de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un anio es bisiesto.

    Un anio es bisiesto si es divisible por 4, excepto los anios
    divisibles por 100 que no lo sean tambien por 400.

    Args:
        anio: anio a evaluar (numero entero).

    Returns:
        True si el anio es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de anios separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas invalidas).

    Returns:
        Lista de anios como enteros.
    """
    while True:
        entrada: str = input("Ingrese anios separados por comas (ej. 2000,2023,2024): ").strip()
        if not entrada:
            print("Error: La entrada no puede estar vacia. Intente nuevamente.")
            continue

        try:
            partes = entrada.split(",")
            anios: list[int] = [int(parte.strip()) for parte in partes if parte.strip()]
            
            if not anios:
                print("Error: No se ingresaron numeros validos. Intente nuevamente.")
                continue

            return anios
        except ValueError:
            print("Error: Ingrese unicamente numeros enteros validos separados por comas.")


def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados: list[int] = leer_anios()
    anios_bisiestos: list[int] = [anio for anio in anios_ingresados if es_bisiesto(anio)]

    print("\n--- Resumen de Analisis ---")
    print(f"Anios ingresados: {anios_ingresados}")
    print(f"Anios bisiestos: {anios_bisiestos}")
    print(f"Cantidad de anios bisiestos: {len(anios_bisiestos)} de {len(anios_ingresados)}")


if __name__ == "__main__":
    main()
