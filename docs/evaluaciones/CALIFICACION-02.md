# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Camilo Ospina Hernández · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `5b2ff24`

Muy buen trabajo: se nota un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **95 / 100** |
| **Nota (0–5)** | **4.75** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que Divide y Vencerás empieza a ganar entre n = 10 y n = 50, y explica por qué la fuerza bruta gana en listas muy pequeñas (menos trabajo extra por llamadas recursivas).
- Compara con el máximo de un arreglo: la recurrencia `T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que recorrer una vez, así que dividir no ayuda.
- Recomienda Divide y Vencerás y declara la cifra a 1.000.000 de registros como estimación, usando el crecimiento de cada algoritmo y no una regla de tres lineal.

**Lo que puede mejorar:**
- El punto de cruce "entre 25 y 40" no sale de ninguna de sus mediciones (solo midió 10 y 50); dígalo como una suposición o mida tamaños intermedios.
- En la estimación aparece "14.106 s" para la fuerza bruta cuando son unos 14.106 segundos con punto de miles (casi 4 horas); la unidad quedó confusa. Además, no menciona que la estimación puede variar con el computador.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando cada término y la resuelve con el método maestro, verificando que se cumple el caso 2.
- Justifica el `Θ(n²)` de la fuerza bruta con la suma de pasos de los dos ciclos.

**Lo que puede mejorar:**
- Explique más a fondo por qué el caso cruzado cuesta `Θ(n)` (cada barrido recorre una mitad).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos en todos los casos pedidos y coinciden en 30 listas aleatorias. Yo también las comparé con un resultado de referencia en 500 listas y no hubo diferencias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función cambia la lista recibida.
- Tienen indicaciones de tipo y documentación estilo Google.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas, título, ejes rotulados y leyenda, en escala lineal y logarítmica, con 9 tamaños.
- Calcula el factor al duplicar n de 4000 a 8000 (3,98 en fuerza bruta y 2,08 en divide y vencerás) y lo compara con lo esperado. Los valores citados coinciden con la gráfica (cerca de 900 ms y 7 ms en n = 8000).
- Incluye una tabla con los valores medidos y explica que repitió cada medición 5 veces.

**Lo que puede mejorar:**
- La frase "la pendiente de Fuerza Bruta duplica la de Divide y Vencerás" en escala logarítmica es imprecisa; apóyela con valores leídos de la gráfica.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta `lab2-divide-y-vencer/` con todos los archivos pedidos, en el orden indicado, con enlaces al código en cada parte y la gráfica visible.
- Tres commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa y vuelve a generar la gráfica, y ambos algoritmos dan la misma suma en cada tamaño.

## Para el próximo laboratorio
- Mantenga los *type hints*, los *docstrings* con `Args` y `Returns` y las dos líneas en blanco entre funciones.
- Cuando cite un tamaño de cruce, mida tamaños cercanos para respaldarlo.
- Revise las unidades en las estimaciones y aclare que son aproximadas.
- Profundice un poco más en por qué cada término de la recurrencia cuesta lo que cuesta.
