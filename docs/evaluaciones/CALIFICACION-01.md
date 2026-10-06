# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Camilo Ospina Hernandez · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `8a9d7fd`

Muy buen trabajo: su informe está completo y el código funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **83 / 100** |
| **Nota (0–5)** | **4.15** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre un algoritmo correcto y uno viable, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica con números por qué el servidor del doble de velocidad no basta (la carga crece 3.600 veces y la máquina solo ahorra la mitad).
- Su segundo ejemplo (autobuses y paradas) trae cantidades y una restricción de tiempo concretas.
- Conecta el tiempo de ejecución con la energía gastada cada noche durante años, y señala quién asume el costo en el paciente y en el operador.
**Lo que puede mejorar:**
- Al hablar de la obligación ética del orden de la lista, falta decir con más claridad qué comprobaciones concretas harían confiable el ordenamiento (por ejemplo, verificar el resultado antes de entregarlo).
- Podría mencionar también el costo para la Secretaría o el equipo de desarrollo.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio indicando sobre qué entradas se toma cada uno, justifica usar el peor caso y deja la predicción antes del experimento.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve por método maestro (con la condición verificada) y por árbol de recursión.
- El análisis línea a línea de insertion sort y la tabla de complejidades están completos.
**Lo que puede mejorar:**
- El caso promedio de insertion sort aparece en la tabla, pero no se muestra de dónde sale el `n²/4`.
- En el conteo de ejecuciones de las líneas del ciclo interno hay pequeñas imprecisiones respecto al código real.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. La mezcla de merge sort es propia y recursiva.
- Los generadores dan listas del tamaño pedido, sin repetidos y con semilla.
**Lo que puede mejorar:**
- En el escenario B, el 2 % final son los valores más pequeños, así que nunca tienen que viajar hacia el 98 % ordenado. Por eso insertion sort casi no trabaja (unas 10.600 comparaciones con 6.400 datos). Los registros nuevos debían tener riesgos variados, mezclados con los del resto.
- Las funciones `ejecutar_experimento` no tienen *docstring*, y hay varias líneas demasiado largas en `parte3_casos.py` y `parte4_complejidad.py`.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda; las curvas pedidas están en los mismos ejes.
- Identifica correctamente el escenario C como peor caso, el B como mejor y el A como caso promedio, y relaciona la gráfica de la Parte 4 con las complejidades calculadas.
- El concepto técnico recomienda merge sort, declara las extrapolaciones como estimaciones y discute memoria, estabilidad y mantenimiento.
**Lo que puede mejorar:**
- Algunas cifras del informe no coinciden con sus propias gráficas: dice que insertion sort tarda cerca de 1,5 s con 6.400 datos, pero las gráficas muestran unos 0,65 s. Dice que el escenario B hace unas 200.000 comparaciones y la gráfica muestra casi cero.
- Por eso la estimación para 1.200.000 registros (14,8 horas) está inflada; con el dato de la gráfica saldrían unas 6 horas. La conclusión (no cabe en cuatro horas) sigue valiendo, pero el número debe salir de lo que se mide.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas y los nombres de archivos pedidos, en la rama `main`.
- El informe está por partes, con las gráficas visibles, enlaces al código e instrucciones de reproducción.
- Hay cinco commits descriptivos sobre el laboratorio.
**Lo que puede mejorar:**
- Los cinco commits tienen la misma fecha y hora; conviene hacer commits a medida que avanza el trabajo.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien listas pequeñas, medianas y aleatorias, y los scripts de las Partes 3 y 4 corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Revise que cada número del informe salga de sus gráficas o tablas antes de entregar.
- Cuando genere un escenario "casi ordenado", imprima algunos datos y verifique que lo nuevo quede realmente mezclado.
- Agregue *docstring* a todas las funciones, incluidas las de los scripts, y mantenga las líneas cortas.
- Haga commits pequeños y frecuentes durante el desarrollo.
