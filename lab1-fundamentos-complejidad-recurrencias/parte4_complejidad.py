# -*- coding: utf-8 -*-
"""Experimento de la Parte 4: Comparativa Insertion Sort vs Merge Sort."""

import time
import os
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento() -> None:
    tamanos: list[int] = [100, 200, 400, 800, 1600, 3200, 6400]
    repeticiones: int = 3

    tiempos_insertion: list[float] = []
    tiempos_merge: list[float] = []

    print("Ejecutando experimento Parte 4 (Insertion vs Merge Sort en Escenario A)...")

    for n in tamanos:
        datos = generar_aleatorio(n)

        # Insertion Sort
        t_acum_ins = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            insertion_sort(datos)
            t_acum_ins += (time.perf_counter() - t_ini)
        tiempos_insertion.append((t_acum_ins / repeticiones) * 1000)  # en ms

        # Merge Sort
        t_acum_mrg = 0.0
        for _ in range(repeticiones):
            t_ini = time.perf_counter()
            merge_sort(datos)
            t_acum_mrg += (time.perf_counter() - t_ini)
        tiempos_merge.append((t_acum_mrg / repeticiones) * 1000)  # en ms

        print(f"  n={n} completado.")

    os.makedirs("lab1-fundamentos-complejidad-recurrencias/graficas", exist_ok=True)

    # Grafica Parte 4: Tiempo comparativo
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_insertion, marker="o", label="Insertion Sort (O(n^2))", color="#d62728", linewidth=2)
    plt.plot(tamanos, tiempos_merge, marker="s", label="Merge Sort (O(n log n))", color="#1f77b4", linewidth=2)
    plt.title("Comparativa de Desempeno: Insertion Sort vs. Merge Sort (Escenario A)", fontsize=12, fontweight="bold")
    plt.xlabel("Tamano de la entrada (n elementos)", fontsize=10)
    plt.ylabel("Tiempo de ejecucion (milisegundos [ms])", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.savefig("lab1-fundamentos-complejidad-recurrencias/graficas/parte4_tiempo.png", dpi=300)
    plt.close()

    print("Grafica de Parte 4 generada exitosamente en graficas/.")


if __name__ == "__main__":
    ejecutar_experimento()
