# Laboratorio Evaluativo 03: Estructuras de Datos — Tabla Hash vs. Lista Enlazada

- **Estudiante:** Camilo Ospina Hernández
- **Correo Institucional:** camiloospina318319@correo.itm.edu.co
- **Asignatura:** Análisis de algoritmos
- **Semestre:** 2026-2
- **Situación Problema:** Rutas del Caribe — Rediseño del sistema de consulta de envíos y rastreo de guías

---

## Instrucciones de Reproducción

Para ejecutar de manera íntegra y reproducible las pruebas unitarias y los experimentos de medición de rendimiento, ejecute los siguientes comandos desde la raíz del repositorio (`curso-analisis-algoritmos`):

```powershell
# 1. Activar el entorno virtual de Python
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependencias requeridas (si no están instaladas)
pip install -r requirements.txt

# 3. Ejecutar la batería de pruebas unitarias y verificación formal
python lab3-estructuras-datos\pruebas.py

# 4. Ejecutar el protocolo experimental de medición y regenerar las gráficas
python lab3-estructuras-datos\medicion.py
```

> **Nota:** También es posible ejecutar los scripts posicionándose directamente dentro de la carpeta `lab3-estructuras-datos/` mediante `python pruebas.py` y `python medicion.py`.

---

## Parte 1 — Implementación y Verificación de las Estructuras

La implementación de los algoritmos y estructuras de datos se encuentra en [estructuras.py](estructuras.py), y la suite de pruebas automatizadas en [pruebas.py](pruebas.py).

### Descripción de la Verificación y Casos Cubiertos
Para certificar la corrección de `ListaEnlazada` y `TablaHash` (con encadenamiento y resolución de colisiones por método de la división), se implementó un conjunto riguroso de pruebas con `assert` que cubre:

1. **Búsquedas Básicas (Exitosas e Infructuosas):** Se comprobó en ambas estructuras que al insertar pares `(guia, estado)` específicos, la consulta de una guía existente retorna su estado exacto, mientras que la consulta de una guía no presente retorna estrictamente `None`. Asimismo, se constató que las estructuras vacías reportan `tamano == 0` y retornan `None` ante cualquier búsqueda.
2. **Colisión Forzada ($m = 7$):** Con una tabla de tamaño $m = 7$, se verificó que las guías $10$, $24$ y $17$ colisionan exactamente en la casilla $3$, puesto que $10 \bmod 7 = 3$, $24 \bmod 7 = 3$ y $17 \bmod 7 = 3$. Se validó que las tres guías se insertan y recuperan exitosamente, que la lista enlazada de la casilla 3 tiene longitud exacta $3$, que las casillas restantes ($0, 1, 2, 4, 5, 6$) permanecen vacías (`tamano == 0`), y que `factor_carga()` evalúa exactamente $3 / 7$.
3. **Muestreo Aleatorio Masivo (25 Colecciones):** Se evaluaron 25 colecciones aleatorias con tamaños variables entre $30$ y $150$ elementos y módulos primos variados ($m \in [7, 13, 19, 31, 53, 97]$). Se verificó que, para cada elemento existente y para 30 guías inexistentes por colección, `lista.buscar(g) == tabla.buscar(g)` de forma idéntica en el 100 % de los casos, validando consistencia absoluta sin recurrir a bibliotecas prohibidas (`dict`, `set` o `hash()`).

---

## Parte 2 — Medición Experimental y Gráficas

El código de los experimentos de rendimiento y generación de figuras se encuentra en [medicion.py](medicion.py).

### Metodología de Medición
Las mediciones se ejecutaron bajo un estricto protocolo experimental para garantizar rigor y reproducibilidad:
- **Aislamiento del Cronometraje:** Se midió exclusivamente el tiempo invertido en las consultas mediante `time.perf_counter()`, aislando la generación de datos y el poblamiento de las estructuras.
- **Búsquedas Infructuosas:** En cada ensayo se consultaron 200 guías inexistentes de 10 dígitos generadas con semilla determinista mediante `generar_guias_inexistentes()`. Este escenario representa el peor caso operativo, obligando a recorrer cada estructura hasta el final.
- **Mitigación de Ruido:** Cada bloque de 200 consultas se repitió en 5 rondas consecutivas por configuración, calculando el promedio aritmético por búsqueda en microsegundos ($\mu\text{s}$).
- **Verificación en Muestra:** En cada iteración se verificó que una muestra de claves existentes devolviera idéntico estado en ambas estructuras.

### Resultados del Experimento A (Lista frente a Tabla, $\alpha \approx 2$)
Se evaluaron seis valores de $n \in [100, 500, 1000, 5000, 20000, 50000]$, seleccionando en cada caso un módulo primo $m \approx n / 2$ para mantener $\alpha \approx 2$:

| $n$ (Guías) | $m$ (Casillas) | $\alpha$ Real | Tiempo Lista ($\mu\text{s}$) | Tiempo Tabla ($\mu\text{s}$) | Ventaja de la Tabla |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 100 | 53 | 1.887 | 3.18 | 0.170 | 18.8x |
| 500 | 251 | 1.992 | 14.48 | 0.216 | 67.2x |
| 1.000 | 503 | 1.988 | 29.44 | 0.279 | 105.4x |
| 5.000 | 2503 | 1.998 | 148.35 | 0.412 | 359.9x |
| 20.000 | 10007 | 1.999 | 766.86 | 0.510 | 1.503.9x |
| 50.000 | 25013 | 1.999 | 4.239.46 | 0.304 | 13.950.2x |

![Comparativa de Desempeño: Lista vs. Tabla](graficas/lista_vs_tabla.png)

### Resultados del Experimento B (Efecto del Factor de Carga $\alpha$, $n = 20.000$ Fijo)
Con $n = 20.000$ fijo, se varió $m$ para evaluar 7 factores de carga entre $0.25$ y $10.00$:

| $\alpha$ Objetivo | $m$ (Primo) | $\alpha$ Real | Tiempo Tabla ($\mu\text{s}$) |
| :---: | :---: | :---: | :---: |
| 0.25 | 80021 | 0.250 | 0.182 |
| 0.50 | 40009 | 0.500 | 0.163 |
| 1.00 | 20011 | 0.999 | 0.177 |
| 2.00 | 10007 | 1.999 | 0.175 |
| 4.00 | 5003 | 3.998 | 0.293 |
| 8.00 | 2503 | 7.990 | 0.378 |
| 10.00 | 2003 | 9.985 | 0.433 |

![Efecto del Factor de Carga en Tabla Hash](graficas/tiempo_vs_alfa.png)

---

## Parte 3 — Análisis Teórico y Discusión

### 1. Costo Teórico
En una lista enlazada simple sin orden, una búsqueda infructuosa no puede anticiparse y recorre los $n$ nodos hasta `None`. Cada nodo exige comparar la clave y avanzar el puntero ($\Theta(1)$), costando estrictamente $\Theta(n)$.

En la tabla hash con encadenamiento, consultar la clave $k$ requiere evaluar $h(k) = k \bmod m$ e indexar su casilla ($\Theta(1)$). Ante una clave inexistente, se recorre toda la lista de dicha casilla. Bajo la **Hipótesis de Dispersión Uniforme Simple (SUHA)**, cada clave se distribuye de manera uniforme e independiente entre las $m$ casillas ($P = 1/m$). La longitud esperada de cada lista es el factor de carga $\alpha = n / m$. Sumando el hash, el acceso y la inspección de $\alpha$ nodos, el costo promedio es $\Theta(1 + \alpha)$.

Si todas las claves cayeran en la misma casilla, se formaría una única lista de longitud $n$ y $m-1$ casillas vacías. La búsqueda infructuosa examinaría los $n$ nodos, degradando la tabla a $\Theta(n)$ y perdiendo su ventaja.

### 2. Lo Medido contra lo Esperado
En la gráfica lineal, la lista enlazada crece de forma pronunciada, mientras la tabla hash permanece plana. Al comparar dos tamaños consecutivos:
- De $n_1 = 500$ ($14.48\,\mu\text{s}$) a $n_2 = 1.000$ ($29.44\,\mu\text{s}$), $n$ se multiplica por $2.00\times$ y el tiempo por $2.03\times$.
- De $n_1 = 1.000$ ($29.44\,\mu\text{s}$) a $n_2 = 5.000$ ($148.35\,\mu\text{s}$), $n$ crece $5.00\times$ y el tiempo por $5.04\times$.
Esto coincide de forma exacta con la complejidad teórica $\Theta(n)$.

Para la tabla hash, con $m \approx n/2$ mantuvimos $\alpha \approx 2$ constante. Los tiempos oscilaron entre $0.170\,\mu\text{s}$ y $0.510\,\mu\text{s}$. Entre $n = 500$ ($0.216\,\mu\text{s}$) y $n = 50.000$ ($0.304\,\mu\text{s}$), aunque $n$ creció $100\times$, el tiempo varió solo $1.41\times$, confirmando la cota $\Theta(1)$.

En la segunda gráfica ($n = 20.000$), al crecer $\alpha$ de $0.50$ a $10.00$, el tiempo asciende de $0.163\,\mu\text{s}$ a $0.433\,\mu\text{s}$. Crece linealmente con $\alpha$, confirmando que el costo escala con la longitud de la cadena, validando $\Theta(1 + \alpha)$.

### 3. Explicación de las Colisiones
Una colisión ocurre cuando dos claves distintas $k_1 \neq k_2$ generan el mismo hash ($h(k_1) = h(k_2)$), compitiendo por la misma casilla. Ocurre aun con $m > n$ por la **Paradoja del Cumpleaños**: la cantidad de pares $\binom{n}{2}$ crece cuadráticamente, superando el 50 % de probabilidad con pocos elementos. Si $n > m$, es inevitable por el Principio del Palomar.

Resolución:
- **Encadenamiento:** Cada casilla guarda una lista enlazada con los elementos colisionados.
  - *Ventaja:* Admite $\alpha > 1$ sin saturarse; eliminación directa y simple.
  - *Costo:* Sobrecosto de memoria por punteros y menor localidad en caché.
- **Direccionamiento Abierto:** Los elementos residen en el arreglo, buscando casillas libres por sondeo.
  - *Ventaja:* No usa punteros (ahorra memoria) y ofrece mejor localidad de caché.
  - *Costo:* Requiere $\alpha < 1$; sufre agrupamiento (*clustering*); la eliminación exige marcas (*tombstones*).

*Ejemplo:* Con $m = 7$ y $h(k) = k \bmod 7$, las guías 10, 24 y 17 dan residuo 3 ($10 \bmod 7 = 24 \bmod 7 = 17 \bmod 7 = 3$). Colisionan en la casilla 3 formando la lista `17 -> 24 -> 10 -> None`.

### 4. Tabla Hash o Árbol de Búsqueda Binario
Para el monitoreo por rango ("guías entre $X$ y $Y$"), la tabla hash **no sirve**: su función hash dispersa pseudoaleatoriamente las claves destruyendo su orden. Responder a $[X, Y]$ exigiría escanear toda la tabla ($\Theta(m + n)$) o consultar cada clave individualmente, resultando inviable.

Un **Árbol de Búsqueda Binario (ABB)** preserva la propiedad de orden ($izq < nodo < der$). Permite ubicar $X$ en tiempo $O(h)$ y recolectar los $k$ elementos del rango mediante recorrido en orden podado en tiempo $O(h + k)$.

Si 400.000 guías llegan ordenadas a un ABB sin balanceo, cada clave entra como hijo derecho. El árbol degenera en una lista de altura $h = 399.999$, requiriendo hasta $400.000$ comparaciones infructuosas ($\Theta(n)$) y $\approx 200.000$ promedio. En contraste, un árbol equilibrado (AVL o Rojo-Negro) garantiza $h = \lceil \log_2(400.001) \rceil = 19$ niveles, resolviendo cualquier búsqueda en máximo 19 comparaciones: más de 21.000 veces menos trabajo.

### 5. Concepto Técnico para la Jefa de Operaciones
Recomiendo una **solución híbrida con doble indexación en memoria**:
1. **Call Center (consulta puntual):** **Tabla Hash** con $\alpha \le 1.0$ (o `dict` de Python), garantizando búsquedas en $\Theta(1)$ promedio ($\approx 0.3\,\mu\text{s}$).
2. **Operaciones (monitoreo por rango $[X, Y]$):** **Árbol Autoequilibrado** (Rojo-Negro/AVL) o **Árbol B+**, permitiendo consultas de lotes en $O(\log n + k)$.
Ambas estructuras deben compartir punteros a los mismos objetos de envío para no duplicar datos.

*Estimación para 5.000.000 de envíos activos:*
> *Declaración:* Estas cifras son una **estimación analítica aproximada** basada en la complejidad asintótica y los tiempos empíricos medidos, sujeta a hardware y caché.

- **Lista Enlazada:** Al costar $\Theta(n)$, escala linealmente. Con $n = 50.000$ tardó $4.239\,\mu\text{s}$ ($\approx 4.24\text{ ms}$). Para $5.000.000$ de envíos ($100\times$ más datos):
  $$T_{lista}(5 \times 10^6) \approx 4.24\text{ ms} \times 100 \approx \mathbf{424\text{ ms}} \quad (\mathbf{0.42\text{ s por consulta}})$$
  En hora pico, consultas erróneas concurrentes saturarían la CPU con demoras de varios segundos por llamada.
- **Tabla Hash:** Con $\alpha \approx 2$ ($m \approx 2.500.003$), es $\Theta(1 + \alpha) = \Theta(1)$:
  $$T_{tabla}(5 \times 10^6) \approx \mathbf{0.3\text{ a }0.5\,\mu\text{s}} \quad (\mathbf{0.0000005\text{ s por consulta}})$$
  La tabla responderá más de **800.000 veces más rápido**, asegurando inmediatez total.
