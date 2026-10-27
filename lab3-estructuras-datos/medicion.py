"""Experimentos de rendimiento y generacion de graficas para el Laboratorio 3."""

import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def es_primo(numero: int) -> bool:
    """Determina si un numero entero es primo.

    Args:
        numero: entero a verificar.

    Returns:
        True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    if numero in (2, 3):
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def siguiente_primo(inicio: int) -> int:
    """Encuentra el menor numero primo mayor o igual a inicio.

    Args:
        inicio: valor entero de partida.

    Returns:
        Primer numero primo >= inicio.
    """
    candidato = max(2, inicio)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_dataset(
    n: int, semilla: int = 42
) -> tuple[list[tuple[int, str]], set[int]]:
    """Genera n pares (guia, estado) con claves unicas de diez digitos.

    Args:
        n: cantidad de pares a generar.
        semilla: semilla para reproducibilidad.

    Returns:
        Tupla con lista de pares (guia, estado) y el conjunto de guias.
    """
    azar = random.Random(semilla)
    estados = ("en bodega", "en reparto", "entregado")
    existentes: set[int] = set()
    pares: list[tuple[int, str]] = []

    while len(pares) < n:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            existentes.add(guia)
            pares.append((guia, azar.choice(estados)))

    return pares, existentes


def cronometrar_busquedas(
    estructura: ListaEnlazada | TablaHash,
    guias_consulta: list[int],
    repeticiones: int = 5,
) -> float:
    """Mide el tiempo medio por busqueda individual sobre guias dadas.

    Args:
        estructura: instancia de ListaEnlazada o TablaHash.
        guias_consulta: lista de claves a consultar.
        repeticiones: numero de rondas para promediar.

    Returns:
        Tiempo medio por busqueda expresado en microsegundos (µs).
    """
    tiempos_rondas: list[float] = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in guias_consulta:
            _ = estructura.buscar(guia)
        fin = time.perf_counter()
        duracion_total = fin - inicio
        tiempo_por_consulta = duracion_total / len(guias_consulta)
        tiempos_rondas.append(tiempo_por_consulta)

    # Convertir promedio a microsegundos (µs)
    promedio_segundos = sum(tiempos_rondas) / len(tiempos_rondas)
    return promedio_segundos * 1_000_000


def ejecutar_experimento_a() -> list[dict[str, float | int]]:
    """Ejecuta el Experimento A: Comparativa ListaEnlazada vs TablaHash.

    Returns:
        Lista de diccionarios con los resultados de cada valor de n.
    """
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    num_busquedas = 200
    repeticiones = 5
    resultados: list[dict[str, float | int]] = []

    print("=" * 70)
    print("EXPERIMENTO A: Comparativa Lista Enlazada vs Tabla Hash (Caso Inexistente)")
    print("=" * 70)

    for n in valores_n:
        m = siguiente_primo(round(n / 2))
        alfa_esperado = n / m

        # 1. Generar datos
        pares, existentes = generar_dataset(n, semilla=42 + n)
        guias_inexistentes = generar_guias_inexistentes(
            existentes, num_busquedas, semilla=7 + n
        )

        # 2. Poblar estructuras
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia, estado in pares:
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # 3. Verificacion de consistencia en muestra de claves existentes
        muestra_verif = list(pares)[: min(50, n)]
        for g_verif, est_verif in muestra_verif:
            assert lista.buscar(g_verif) == est_verif
            assert tabla.buscar(g_verif) == est_verif
            assert lista.buscar(g_verif) == tabla.buscar(g_verif)

        # 4. Cronometrar unicamente las busquedas infructuosas
        t_lista = cronometrar_busquedas(lista, guias_inexistentes, repeticiones)
        t_tabla = cronometrar_busquedas(tabla, guias_inexistentes, repeticiones)

        registro = {
            "n": n,
            "m": m,
            "alfa": alfa_esperado,
            "t_lista_us": t_lista,
            "t_tabla_us": t_tabla,
            "ratio_lista_tabla": t_lista / t_tabla if t_tabla > 0 else 0.0,
        }
        resultados.append(registro)

        print(
            f"n = {n:5d} | m = {m:5d} | alfa = {alfa_esperado:.3f} | "
            f"Lista: {t_lista:8.2f} us | Tabla: {t_tabla:6.3f} us | "
            f"Ventaja Tabla: {t_lista / t_tabla:7.1f}x"
        )

    return resultados


def ejecutar_experimento_b() -> list[dict[str, float | int]]:
    """Ejecuta el Experimento B: Efecto del Factor de Carga en TablaHash.

    Returns:
        Lista de diccionarios con los resultados de cada valor de alfa.
    """
    n_fijo = 20000
    alfas_objetivo = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 10.0]
    num_busquedas = 200
    repeticiones = 5
    resultados: list[dict[str, float | int]] = []

    print("\n" + "=" * 70)
    print("EXPERIMENTO B: Efecto del Factor de Carga alfa (n = 20.000 Fijo)")
    print("=" * 70)

    # Generar datos comunes para todas las tablas
    pares, existentes = generar_dataset(n_fijo, semilla=101)
    guias_inexistentes = generar_guias_inexistentes(
        existentes, num_busquedas, semilla=303
    )

    for alfa_obj in alfas_objetivo:
        m_objetivo = round(n_fijo / alfa_obj)
        m = siguiente_primo(m_objetivo)
        tabla = TablaHash(m)

        for guia, estado in pares:
            tabla.insertar(guia, estado)

        alfa_real = tabla.factor_carga()

        # Verificacion en muestra
        for g_verif, est_verif in list(pares)[:30]:
            assert tabla.buscar(g_verif) == est_verif

        # Cronometraje
        t_tabla = cronometrar_busquedas(tabla, guias_inexistentes, repeticiones)

        registro = {
            "n": n_fijo,
            "m": m,
            "alfa_objetivo": alfa_obj,
            "alfa_real": alfa_real,
            "t_tabla_us": t_tabla,
        }
        resultados.append(registro)

        print(
            f"alfa_obj = {alfa_obj:5.2f} | m = {m:5d} | alfa_real = {alfa_real:6.3f} | "
            f"Tiempo medio busqueda: {t_tabla:6.3f} us"
        )

    return resultados


def graficar_experimento_a(
    resultados: list[dict[str, float | int]], ruta_salida: str
) -> None:
    """Genera y guarda la grafica comparativa de Lista vs Tabla.

    Args:
        resultados: datos medidos en el Experimento A.
        ruta_salida: ruta del archivo de imagen a generar.
    """
    ns = [r["n"] for r in resultados]
    t_lista = [r["t_lista_us"] for r in resultados]
    t_tabla = [r["t_tabla_us"] for r in resultados]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel 1: Escala lineal
    ax1.plot(
        ns,
        t_lista,
        marker="o",
        color="#d9534f",
        linewidth=2,
        label="Lista Enlazada (Θ(n))",
    )
    ax1.plot(
        ns,
        t_tabla,
        marker="s",
        color="#0275d8",
        linewidth=2,
        label="Tabla Hash con Encadenamiento (Θ(1 + α))",
    )
    ax1.set_title("Comparativa de Desempeño (Escala Lineal)", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Número de guías (n)", fontsize=10)
    ax1.set_ylabel("Tiempo medio por búsqueda (µs)", fontsize=10)
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="upper left")

    # Panel 2: Escala logaritmica (log-log)
    ax2.plot(
        ns,
        t_lista,
        marker="o",
        color="#d9534f",
        linewidth=2,
        label="Lista Enlazada (pendiente ~ 1.0)",
    )
    ax2.plot(
        ns,
        t_tabla,
        marker="s",
        color="#0275d8",
        linewidth=2,
        label="Tabla Hash (pendiente ~ 0.0)",
    )
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_title("Comparativa de Desempeño (Escala Log-Log)", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Número de guías (n) [escala log]", fontsize=10)
    ax2.set_ylabel("Tiempo medio por búsqueda (µs) [escala log]", fontsize=10)
    ax2.grid(True, which="both", linestyle="--", alpha=0.6)
    ax2.legend(loc="upper left")

    plt.suptitle(
        "Experimento A: Tiempo de Búsqueda de Guías Inexistentes vs. Cantidad de Guías (n)",
        fontsize=13,
        fontweight="bold",
        y=0.98,
    )
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
    print(f"Grafica guardada: {ruta_salida}")


def graficar_experimento_b(
    resultados: list[dict[str, float | int]], ruta_salida: str
) -> None:
    """Genera y guarda la grafica del tiempo frente al factor de carga.

    Args:
        resultados: datos medidos en el Experimento B.
        ruta_salida: ruta del archivo de imagen a generar.
    """
    alfas = [r["alfa_real"] for r in resultados]
    t_tabla = [r["t_tabla_us"] for r in resultados]

    plt.figure(figsize=(8, 5.5))
    plt.plot(
        alfas,
        t_tabla,
        marker="D",
        color="#5cb85c",
        linewidth=2.2,
        markersize=7,
        label="Tabla Hash (tiempo medido en µs)",
    )

    plt.title(
        "Experimento B: Efecto del Factor de Carga (α) en el Tiempo de Búsqueda (n = 20.000)",
        fontsize=11,
        fontweight="bold",
    )
    plt.xlabel("Factor de carga (α = n / m)", fontsize=10)
    plt.ylabel("Tiempo medio por búsqueda (µs)", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper left")

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
    print(f"Grafica guardada: {ruta_salida}")


def main() -> None:
    """Punto de entrada principal para ejecucion experimental."""
    os.makedirs("graficas", exist_ok=True)

    res_a = ejecutar_experimento_a()
    graficar_experimento_a(res_a, os.path.join("graficas", "lista_vs_tabla.png"))

    res_b = ejecutar_experimento_b()
    graficar_experimento_b(res_b, os.path.join("graficas", "tiempo_vs_alfa.png"))

    print("\n" + "=" * 70)
    print("RESUMEN DE DATOS MEDIDOS (PARA INFORME README.md)")
    print("=" * 70)
    print("\nTABLA EXPERIMENTO A:")
    print("| n | m | alfa | Tiempo Lista (us) | Tiempo Tabla (us) | Ventaja Tabla |")
    print("|---|---|---|---|---|---|")
    for r in res_a:
        print(
            f"| {r['n']} | {r['m']} | {r['alfa']:.3f} | "
            f"{r['t_lista_us']:.2f} | {r['t_tabla_us']:.3f} | {r['ratio_lista_tabla']:.1f}x |"
        )

    print("\nTABLA EXPERIMENTO B:")
    print("| alfa Objetivo | m | alfa Real | Tiempo Tabla (us) |")
    print("|---|---|---|---|")
    for r in res_b:
        print(
            f"| {r['alfa_objetivo']} | {r['m']} | {r['alfa_real']:.3f} | {r['t_tabla_us']:.3f} |"
        )


if __name__ == "__main__":
    main()
