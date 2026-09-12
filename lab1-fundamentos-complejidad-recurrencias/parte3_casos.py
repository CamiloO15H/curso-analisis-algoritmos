# -*- coding: utf-8 -*-
"""Experimento de la Parte 3: Analisis de casos en Insertion Sort."""

import time
import os
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento() -> None:
    tamanos: list[int] = [100, 200, 400, 800, 1600, 3200, 6400]
    repeticiones: int = 3

    tiempos_a: list[float] = []
    tiempos_b: list[float] = []
    tiempos_c: list[float] = []

    comps_a: list[int] = []
    comps_b: list[int] = []
    comps_c: list[int] = []

    print("Ejecutando experimento Parte 3 (Insertion Sort en Escenarios A, B y C)...")

    for n in tamanos:
        # Escenario A
        datos_a = generar_aleatorio(n)
        t_acum = 0.0
        c_val = 0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            _, c_val = insertion_sort(datos_a)
            t_acum += (time.perf_counter() - t_ini)
        tiempos_a.append(t_acum / repeticiones)
        comps_a.append(c_val)

        # Escenario B
        datos_b = generar_casi_ordenado(n)
        t_acum = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            _, c_val = insertion_sort(datos_b)
            t_acum += (time.perf_counter() - t_ini)
        tiempos_b.append(t_acum / repeticiones)
        comps_b.append(c_val)

        # Escenario C
        datos_c = generar_inverso(n)
        t_acum = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            _, c_val = insertion_sort(datos_c)
            t_acum += (time.perf_counter() - t_ini)
        tiempos_c.append(t_acum / repeticiones)
        comps_c.append(c_val)
        print(f"  n={n} completado.")

    os.makedirs("lab1-fundamentos-complejidad-recurrencias/graficas", exist_ok=True)

    # Grafica 1: Comparaciones vs Tamano
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, comps_a, marker="o", label="Escenario A (Aleatorio - Caso Promedio)", color="#1f77b4")
    plt.plot(tamanos, comps_b, marker="s", label="Escenario B (Casi Ordenado - Mejor Caso)", color="#2ca02c")
    plt.plot(tamanos, comps_c, marker="^", label="Escenario C (Inverso - Peor Caso)", color="#d62728")
    plt.title("Insertion Sort: Comparaciones vs. Tamano de Entrada", fontsize=12, fontweight="bold")
    plt.xlabel("Tamano de la entrada (n elementos)", fontsize=10)
    plt.ylabel("Numero de comparaciones realizadas", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig("lab1-fundamentos-complejidad-recurrencias/graficas/parte3_comparaciones.png", dpi=300)
    plt.close()

    # Grafica 2: Tiempo vs Tamano
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, [t * 1000 for t in tiempos_a], marker="o", label="Escenario A (Aleatorio)", color="#1f77b4")
    plt.plot(tamanos, [t * 1000 for t in tiempos_b], marker="s", label="Escenario B (Casi Ordenado)", color="#2ca02c")
    plt.plot(tamanos, [t * 1000 for t in tiempos_c], marker="^", label="Escenario C (Inverso)", color="#d62728")
    plt.title("Insertion Sort: Tiempo de Ejecucion vs. Tamano de Entrada", fontsize=12, fontweight="bold")
    plt.xlabel("Tamano de la entrada (n elementos)", fontsize=10)
    plt.ylabel("Tiempo promedio de ejecucion (milisegundos [ms])", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig("lab1-fundamentos-complejidad-recurrencias/graficas/parte3_tiempo.png", dpi=300)
    plt.close()

    print("Graficas de Parte 3 generadas exitosamente en graficas/.")


if __name__ == "__main__":
    ejecutar_experimento()
