# -*- coding: utf-8 -*-
"""Experimento y generacion de graficas de tiempo de ejecucion.

Mide el desempeno de subarreglo_fuerza_bruta vs subarreglo_maximo
para diferentes tamanos de entrada, valida la consistencia de resultados
y genera la grafica comparativa de tiempo vs n.
"""

import math
import os
import random
import sys
import time
import matplotlib.pyplot as plt

# Asegurar importacion robusta de subarreglo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def generar_serie(n: int, semilla: int = 42) -> list[float]:
    """Genera una serie de variacion diaria de caja reproducible.

    Args:
        n: Cantidad de dias a generar.
        semilla: Semilla fija para reproducibilidad cientifica.

    Returns:
        Lista de n enteros aleatorios en el intervalo [-100, 100].
    """
    rng = random.Random(semilla + n)
    return [float(rng.randint(-100, 100)) for _ in range(n)]


def ejecutar_mediciones() -> None:
    """Ejecuta el protocolo experimental de medicion de tiempos y grafica."""
    tamanos: list[int] = [10, 50, 100, 250, 500, 1000, 2000, 4000, 8000]
    repeticiones: int = 5

    tiempos_fb: list[float] = []
    tiempos_dv: list[float] = []

    print("=" * 68)
    print("  EXPERIMENTO: SUBARREGLO MAXIMO (FB VS DIVIDE Y VENCERAS)")
    print(f"  Semilla base: 42 | Repeticiones por tamano: {repeticiones}")
    print("=" * 68)
    encabezado = (
        f"{'n':>7} | {'T_FB (ms)':>11} | {'T_DV (ms)':>11} | "
        f"{'Suma FB':>9} | {'Suma DV':>9} | Estado"
    )
    print(encabezado)
    print("-" * 68)

    for n in tamanos:
        datos = generar_serie(n, semilla=42)

        # 1. Medicion Fuerza Bruta
        acum_fb = 0.0
        suma_fb_val = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            res_fb = subarreglo_fuerza_bruta(datos)
            t_fin = time.perf_counter()
            acum_fb += (t_fin - t_ini)
            suma_fb_val = res_fb[2]
        t_prom_fb_ms = (acum_fb / repeticiones) * 1000.0
        tiempos_fb.append(t_prom_fb_ms)

        # 2. Medicion Divide y Venceras
        acum_dv = 0.0
        suma_dv_val = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            res_dv = subarreglo_maximo(datos, 0, n - 1)
            t_fin = time.perf_counter()
            acum_dv += (t_fin - t_ini)
            suma_dv_val = res_dv[2]
        t_prom_dv_ms = (acum_dv / repeticiones) * 1000.0
        tiempos_dv.append(t_prom_dv_ms)

        # 3. Verificacion de consistencia estricta
        assert math.isclose(suma_fb_val, suma_dv_val, abs_tol=1e-5), (
            f"Fallo en n={n}: FB={suma_fb_val} != DV={suma_dv_val}"
        )

        fila = (
            f"{n:>7} | {t_prom_fb_ms:>11.4f} | {t_prom_dv_ms:>11.4f} | "
            f"{suma_fb_val:>9.1f} | {suma_dv_val:>9.1f} | OK"
        )
        print(fila)

    # Crear directorio para almacenar graficas si no existe
    directorio_base = os.path.dirname(os.path.abspath(__file__))
    dir_graficas = os.path.join(directorio_base, "graficas")
    os.makedirs(dir_graficas, exist_ok=True)
    ruta_grafica = os.path.join(dir_graficas, "tiempo_vs_n.png")

    # Configuracion de graficas: Panel doble (Escala Lineal y Logaritmica)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Panel 1: Escala Lineal ---
    ax1.plot(
        tamanos,
        tiempos_fb,
        marker="o",
        color="#d62728",
        linewidth=2,
        label=r"Fuerza Bruta $\Theta(n^2)$",
    )
    ax1.plot(
        tamanos,
        tiempos_dv,
        marker="s",
        color="#1f77b4",
        linewidth=2,
        label=r"Divide y Vencerás $\Theta(n \log n)$",
    )
    ax1.set_title(
        "Comparativa de Tiempo vs. Tamaño (Escala Lineal)",
        fontsize=11,
        fontweight="bold",
    )
    ax1.set_xlabel(
        "Tamaño de la serie $n$ (número de días / registros)",
        fontsize=10,
    )
    ax1.set_ylabel(
        "Tiempo de ejecución promedio (milisegundos [ms])",
        fontsize=10,
    )
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(fontsize=9, loc="upper left")

    # --- Panel 2: Escala Logaritmica (log-log) ---
    ax2.plot(
        tamanos,
        tiempos_fb,
        marker="o",
        color="#d62728",
        linewidth=2,
        label=r"Fuerza Bruta $\Theta(n^2)$",
    )
    ax2.plot(
        tamanos,
        tiempos_dv,
        marker="s",
        color="#1f77b4",
        linewidth=2,
        label=r"Divide y Vencerás $\Theta(n \log n)$",
    )
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_title(
        "Comparativa Asintótica vs. Tamaño (Escala Logarítmica)",
        fontsize=11,
        fontweight="bold",
    )
    ax2.set_xlabel(
        "Tamaño de la serie $n$ (escala logarítmica)",
        fontsize=10,
    )
    ax2.set_ylabel(
        "Tiempo promedio (ms, escala logarítmica)",
        fontsize=10,
    )
    ax2.grid(True, which="both", linestyle="--", alpha=0.6)
    ax2.legend(fontsize=9, loc="upper left")

    plt.suptitle(
        "Análisis Experimental de Desempeño: Subarreglo Máximo\n"
        r"Fuerza Bruta $\Theta(n^2)$ vs. Divide y Vencerás $\Theta(n \log n)$",
        fontsize=13,
        fontweight="bold",
        y=1.02,
    )
    plt.tight_layout()
    plt.savefig(ruta_grafica, dpi=300, bbox_inches="tight")
    plt.close()

    print("\nGrafica generada exitosamente en:", ruta_grafica)
    print("=" * 68)


if __name__ == "__main__":
    ejecutar_mediciones()
