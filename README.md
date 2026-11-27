# Taller Estructuras de Datos

**Estudiante:** TU NOMBRE  
**Curso / Profesor:** TU CURSO / TU PROFESOR  
**Fecha:** 27/11/2026

Este repositorio contiene la solución del taller: heapsort, árbol binario de búsqueda (ABB), árbol AVL, inserción en un árbol rojinegro y dos problemas de HackerRank.

## Contenido

| Punto | Tema | Dónde está |
|---|---|---|
| 1 | Heapsort | [`diagramas/Ejercicio_1.drawio`](diagramas/Ejercicio_1.drawio) |
| 2 | Árbol binario de búsqueda | [`diagramas/Ejercicio_2.drawio`](diagramas/Ejercicio_2.drawio) |
| 3 | Árbol AVL paso a paso | [`diagramas/Ejercicio_3.drawio`](diagramas/Ejercicio_3.drawio) |
| 4 | Árbol rojinegro (insertar el 3) | [`diagramas/Ejercicio_4.drawio`](diagramas/Ejercicio_4.drawio) |
| 5 | Problemas de HackerRank | [`punto5/`](punto5/) y [`evidencia/`](evidencia/) |

---

## Cómo ver los diagramas (puntos 1 a 4)

Los diagramas están hechos en [draw.io](https://www.drawio.com/). Hay dos formas de revisarlos.

### Opción A: desde Visual Studio Code (todo en el repositorio)

1. Clona el repositorio y ábrelo en VS Code:
   ```bash
   git clone https://github.com/TU_USUARIO/taller-estructuras-datos.git
   code taller-estructuras-datos
   ```
2. Instala la extensión **Draw.io Integration** (autor: Henning Dieterichs, id `hediet.vscode-drawio`). Al abrir la carpeta, VS Code suele mostrar un aviso con la recomendación; acéptalo. También puedes hacerlo a mano: `Ctrl+Shift+X`, buscar "Draw.io Integration" e **Install**. La instalación toma menos de un minuto.
3. Abre los archivos de la carpeta `diagramas/`. Se muestran directamente en el editor de VS Code, sin salir de él.
4. En los diagramas con varias páginas (ejercicios 3 y 4) las páginas aparecen como pestañas en la parte inferior del editor.

### Opción B: desde Google Drive

Los mismos archivos están en esta carpeta compartida de Drive:

**[trabajo análisis de algoritmos](https://drive.google.com/drive/folders/1VKwEtmAyeVjUjdBE5CpBwA3a4bLudkAe?usp=drive_link)**

Para abrir un archivo: clic derecho sobre él, **Abrir con**, **diagrams.net (draw.io)**. Si Drive no ofrece esa opción, se puede descargar el archivo `.drawio` y abrirlo en <https://app.diagrams.net> con *Archivo → Abrir desde → Dispositivo*.

### Cómo moverse dentro de un diagrama

Los diagramas son grandes (sobre todo el 1, que es un lienzo largo), así que conviene saber desplazarse:

- **Flechas del teclado:** es la forma más cómoda de recorrer el diagrama. Antes, haz clic en un espacio vacío del lienzo para que no quede ninguna figura seleccionada; si hay una figura seleccionada, las flechas la mueven de lugar en vez de desplazar la vista. Si se mueve una figura sin querer, se deshace con `Ctrl+Z`.
- **Rueda del ratón:** desplaza el diagrama hacia arriba y abajo (con `Shift` se desplaza hacia los lados).
- **Zoom:** `Ctrl` + rueda del ratón, o los botones de lupa (+ y −) de la barra superior. Con zoom bajo se ve el árbol completo y con zoom alto se leen los factores de equilibrio y los textos.
- **Arrastrar:** mantener presionada la barra espaciadora (o el botón central del ratón) y arrastrar mueve la vista sin tocar las figuras.
- **Cambiar de página** (ejercicios 3 y 4): usar las pestañas de la parte inferior del editor, por ejemplo "Paso 1: insertar 8", "Paso 2: insertar 9", y así hasta "Solución final".

### Qué contiene cada archivo

| Archivo | Páginas | Contenido |
|---|---|---|
| `Ejercicio_1.drawio` | 1 (lienzo largo, desplazarse hacia abajo) | Heap inicial, construcción del heap máximo, las 9 extracciones y el resultado ordenado |
| `Ejercicio_2.drawio` | 1 | ABB final con la secuencia completa |
| `Ejercicio_3.drawio` | 23 | Portada con leyenda, 21 pasos (uno por inserción, con factor de equilibrio y rotación) y solución final |
| `Ejercicio_4.drawio` | 5 | Árbol inicial, inserción del 3, rotación derecha en 6, rotación izquierda en 1 y recoloreo final |

---

## Punto 1 - Heapsort

**Enunciado:** aplicar heapsort y mostrar cómo cambia el árbol con la secuencia `8, 9, 11, 15, 19, 20, 21, 7, 3, 2`.

### Conceptos

- **Heap máximo:** árbol binario completo en el que cada padre es mayor o igual que sus hijos. Se guarda en un arreglo: los hijos del índice `i` están en `2i+1` y `2i+2`.
- **Heapify (sift-down):** si un nodo es menor que alguno de sus hijos, se intercambia con el hijo mayor y se repite hacia abajo hasta restaurar la propiedad.
- **Heapsort** tiene dos fases: (1) construir el heap máximo aplicando heapify desde el último nodo interno hasta la raíz, y (2) repetir: intercambiar la raíz con el último elemento del heap, sacarlo de la zona activa y aplicar heapify a la raíz.

### Fase 1: construcción del heap máximo

Se recorren los nodos internos de abajo hacia arriba (índices 4, 3, 2, 1, 0):

| Nodo | Acción | Arreglo |
|---|---|---|
| 19 y 15 | Ya cumplen la propiedad, no hay intercambio | `[8, 9, 11, 15, 19, 20, 21, 7, 3, 2]` |
| 11 | Se intercambia con su hijo mayor, 21 | `[8, 9, 21, 15, 19, 20, 11, 7, 3, 2]` |
| 9 | Se intercambia con su hijo mayor, 19 | `[8, 19, 21, 15, 9, 20, 11, 7, 3, 2]` |
| 8 (raíz) | Baja intercambiando con 21 y luego con 20 | `[21, 19, 20, 15, 9, 8, 11, 7, 3, 2]` |

### Fase 2: extracciones

| Iter. | Intercambio | Heapify | Heap activo | Ordenados |
|---|---|---|---|---|
| 1 | 21 ↔ 2 | 2↔20, 2↔11 | `[20, 19, 11, 15, 9, 8, 2, 7, 3]` | `[21]` |
| 2 | 20 ↔ 3 | 3↔19, 3↔15, 3↔7 | `[19, 15, 11, 7, 9, 8, 2, 3]` | `[20, 21]` |
| 3 | 19 ↔ 3 | 3↔15, 3↔9 | `[15, 9, 11, 7, 3, 8, 2]` | `[19, 20, 21]` |
| 4 | 15 ↔ 2 | 2↔11, 2↔8 | `[11, 9, 8, 7, 3, 2]` | `[15, 19, 20, 21]` |
| 5 | 11 ↔ 2 | 2↔9, 2↔7 | `[9, 7, 8, 2, 3]` | `[11, 15, 19, 20, 21]` |
| 6 | 9 ↔ 3 | 3↔8 | `[8, 7, 3, 2]` | `[9, 11, 15, 19, 20, 21]` |
| 7 | 8 ↔ 2 | 2↔7 | `[7, 2, 3]` | `[8, 9, 11, 15, 19, 20, 21]` |
| 8 | 7 ↔ 3 | no hace falta (3 > 2) | `[3, 2]` | `[7, 8, 9, 11, 15, 19, 20, 21]` |
| 9 | 3 ↔ 2 | no hace falta | `[2]` | `[3, 7, 8, 9, 11, 15, 19, 20, 21]` |

**Resultado:** `[2, 3, 7, 8, 9, 11, 15, 19, 20, 21]`

### Justificación

Se usa un heap **máximo** porque la raíz siempre es el mayor, y cada extracción deja ese mayor en su posición final al fondo del arreglo; así el resultado queda ordenado de menor a mayor. Construir el heap cuesta O(n) y las n extracciones cuestan O(log n) cada una, por lo que el total es **O(n log n)** en todos los casos. Ordena en el mismo arreglo (espacio extra O(1)) y no es estable.

---

## Punto 2 - Árbol binario de búsqueda

**Enunciado:** generar el árbol binario de búsqueda para `8, 9, 11, 15, 19, 20, 21, 7, 3, 2, 1, 5, 6, 4, 13, 14, 10, 12, 17, 16, 18`.

### Concepto

Un **ABB** cumple que, para cada nodo, todos los valores de su subárbol izquierdo son menores y los del derecho son mayores. Cada valor se inserta en el orden dado: se compara con la raíz y se baja a izquierda o derecha hasta encontrar un hueco. **No** hay rebalanceo, así que la forma del árbol depende totalmente del orden de entrada.

### Resultado

```
8
├── izq: 7
│   └── izq: 3
│       ├── izq: 2
│       │   └── izq: 1
│       └── der: 5
│           ├── izq: 4
│           └── der: 6
└── der: 9
    └── der: 11
        ├── izq: 10
        └── der: 15
            ├── izq: 13
            │   ├── izq: 12
            │   └── der: 14
            └── der: 19
                ├── izq: 17
                │   ├── izq: 16
                │   └── der: 18
                └── der: 20
                    └── der: 21
```

### Justificación

Los primeros valores (8, 9, 11, 15, 19, 20, 21) llegan en orden creciente, por lo que forman una cadena hacia la derecha. Después, el 7, el 3 y el 2 forman una cadena hacia la izquierda. El árbol queda desbalanceado: **altura 7** con 21 nodos, cuando el mínimo posible sería 5. En el peor caso, buscar un valor cuesta O(n) en vez de O(log n). Ese es el problema que resuelve el AVL del punto siguiente.

---

## Punto 3 - Árbol AVL

**Enunciado:** generar el árbol AVL para la misma secuencia del punto 2.

### Conceptos

- **Árbol AVL:** ABB autobalanceado. Para todo nodo, el **factor de equilibrio** `FE = altura(izq) − altura(der)` debe estar en {−1, 0, +1}.
- Si tras insertar algún nodo queda con |FE| = 2, se corrige con rotaciones sobre el primer nodo desbalanceado que se encuentra subiendo desde el nodo nuevo:

| Caso | Condición | Rotación |
|---|---|---|
| II (izq-izq) | FE = +2 y el hijo izquierdo tiene FE ≥ 0 | Simple a la derecha |
| DD (der-der) | FE = −2 y el hijo derecho tiene FE ≤ 0 | Simple a la izquierda |
| ID (izq-der) | FE = +2 y el hijo izquierdo tiene FE < 0 | Doble: izquierda en el hijo, derecha en el nodo |
| DI (der-izq) | FE = −2 y el hijo derecho tiene FE > 0 | Doble: derecha en el hijo, izquierda en el nodo |

### Inserciones que requirieron rotación

De las 21 inserciones, 14 produjeron desbalance (11 rotaciones simples y 3 dobles). Las otras 7 (8, 9, 15, 7, 13, 12 y 17) no necesitaron rotar.

| Paso | Inserta | Nodo desbalanceado | Caso | Rotación |
|---|---|---|---|---|
| 3 | 11 | 8 | DD | Simple izquierda |
| 5 | 19 | 11 | DD | Simple izquierda |
| 6 | 20 | 9 | DD | Simple izquierda |
| 7 | 21 | 19 | DD | Simple izquierda |
| 9 | 3 | 8 | II | Simple derecha |
| 10 | 2 | 9 | II | Simple derecha |
| 11 | 1 | 3 | II | Simple derecha |
| 12 | 5 | 15 | II | Simple derecha |
| 13 | 6 | 3 | DD | Simple izquierda |
| 14 | 4 | 2 | DI | Doble derecha-izquierda |
| 16 | 14 | 11 | DD | Simple izquierda |
| 17 | 10 | 9 | DI | Doble derecha-izquierda |
| 20 | 16 | 19 | II | Simple derecha |
| 21 | 18 | 20 | ID | Doble izquierda-derecha |

Cada una de estas inserciones tiene su propia página en `Ejercicio_3.drawio`, con el árbol antes y después de rotar y los FE de cada nodo.

### Resultado final

Raíz 7, altura 5, 21 nodos, todos con |FE| ≤ 1:

```
7
├── izq: 3
│   ├── izq: 2
│   │   └── izq: 1
│   └── der: 5
│       ├── izq: 4
│       └── der: 6
└── der: 15
    ├── izq: 11
    │   ├── izq: 9
    │   │   ├── izq: 8
    │   │   └── der: 10
    │   └── der: 13
    │       ├── izq: 12
    │       └── der: 14
    └── der: 19
        ├── izq: 17
        │   ├── izq: 16
        │   └── der: 18
        └── der: 20
            └── der: 21
```

### Justificación y comparación con el ABB

Con la misma secuencia, el ABB tiene altura 7 y el AVL altura 5, que es la mínima posible para 21 nodos. Las rotaciones cuestan O(1) y mantienen la propiedad de ABB (el recorrido en orden sigue dando 1…21). A cambio de ese trabajo extra en cada inserción, búsqueda, inserción y borrado quedan garantizados en **O(log n)** incluso en el peor caso.

---

## Punto 4 - Árbol rojinegro

**Enunciado:** dado el árbol rojinegro del taller (raíz 13), ¿cómo quedaría al adicionar el 3?

### Conceptos

Un árbol rojinegro es un ABB que cumple cinco propiedades: (1) cada nodo es rojo o negro; (2) la raíz es negra; (3) las hojas `NIL` son negras; (4) un nodo rojo no tiene hijos rojos; (5) todos los caminos desde un nodo hasta sus hojas tienen la misma cantidad de nodos negros. Se inserta como en un ABB, el nodo nuevo se pinta de **rojo** y se corrigen las violaciones según el color del **tío** (hermano del padre):

- Tío rojo: se recolorean padre, tío y abuelo, y se sigue revisando hacia arriba.
- Tío negro (o `NIL`) en forma de **triángulo** (padre e hijo en lados opuestos): rotación sobre el padre, que lo convierte en caso línea.
- Tío negro en forma de **línea**: rotación sobre el abuelo y recoloreo (padre negro, abuelo rojo).

### Procedimiento (4 pasos, uno por página del diagrama)

1. **Insertar 3 como en un ABB:** 3 < 13 (izquierda), 3 < 8 (izquierda), 3 > 1 (derecha), 3 < 6 (izquierda). Queda como hijo izquierdo del 6, en rojo.
2. **Detectar la violación:** el padre (6) es rojo y el nuevo nodo (3) también, así que hay rojo-rojo. El abuelo es el 1 (negro) y el tío, el hijo izquierdo del 1, es `NIL` (negro). Como 6 es hijo derecho de 1 y 3 es hijo izquierdo de 6, es un **triángulo**: se necesita doble rotación.
3. **Rotación a la derecha sobre el 6:** sube el 3 y el 6 queda como su hijo derecho (ahora 1 → 3 → 6 es una línea).
4. **Rotación a la izquierda sobre el 1 y recoloreo:** el 3 queda como raíz del subárbol con el 1 a la izquierda y el 6 a la derecha. El 3 pasa a **negro** y el 1 pasa a **rojo**; el 6 sigue rojo.

### Resultado

El subárbol que antes colgaba del 8 por la izquierda con raíz 1 ahora tiene raíz **3 (negro)**, con hijos **1 (rojo)** y **6 (rojo)**. El resto del árbol no cambia (13 negro, 8 rojo, 11 negro, 17 rojo, 15 negro, 25 negro, 22 rojo, 27 rojo).

### Justificación

- No hay nodos rojos consecutivos: el 8 (rojo) ahora tiene como hijo al 3 (negro).
- La raíz sigue negra.
- Los caminos hacia las hojas mantienen **2 nodos negros** (por ejemplo 13 → 8 → 3 contra el 13 → 8 → 1 original), así que se conserva la altura negra.
- Se resolvió con 2 rotaciones y 2 cambios de color, sin propagar el arreglo hacia arriba.

---

## Punto 5 - Problemas de HackerRank

| Problema | Código | Enlace | Evidencia |
|---|---|---|---|
| Detect a Cycle in a Linked List | [`punto5/detect_cycle.py`](punto5/detect_cycle.py) | [HackerRank](https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem) | ![](evidencia/detect_cycle.png) |
| Largest Rectangle | [`punto5/largest_rectangle.py`](punto5/largest_rectangle.py) | [HackerRank](https://www.hackerrank.com/challenges/largest-rectangle/problem) | ![](evidencia/largest_rectangle.png) |

### Detect a Cycle in a Linked List

**Problema:** dada la cabeza de una lista enlazada, determinar si tiene un ciclo (algún nodo se visita más de una vez). Retorna 1 si lo hay y 0 si no. Una lista vacía (`head` nulo) no tiene ciclo.

**Enfoque, algoritmo de Floyd (tortuga y liebre):** dos punteros recorren la lista, uno avanza 1 nodo por paso y el otro 2. Si hay ciclo, el rápido termina alcanzando al lento dentro del ciclo; si no lo hay, el rápido llega a `None`.

**Por qué se eligió:** la alternativa obvia es guardar los nodos visitados en un conjunto, que también es O(n) en tiempo pero usa O(n) de memoria. Floyd usa solo **O(1)** de memoria y no modifica la lista.

**Complejidad:** tiempo O(n), espacio O(1).

### Largest Rectangle

**Problema:** dadas las alturas de `n` edificios adyacentes, hallar el área del mayor rectángulo que se puede formar con edificios consecutivos (altura = la del más bajo, ancho = cantidad de edificios). Ejemplo: `[1, 2, 3, 4, 5]` da 9 (altura 3 por 3 edificios).

**Enfoque, pila monótona:** se recorren las alturas manteniendo una pila de alturas crecientes con el índice donde empezó cada una. Cuando llega una altura menor, se van sacando de la pila las alturas mayores; al sacar cada una se calcula el área del rectángulo que esa altura puede cubrir hacia la izquierda y se guarda el máximo. Se agrega una altura 0 al final para vaciar la pila.

**Por qué se eligió:** la fuerza bruta prueba todos los pares de extremos (o expande desde cada edificio) y cuesta O(n²), demasiado lento para las entradas grandes de HackerRank. Con la pila, cada edificio entra y sale una sola vez.

**Complejidad:** tiempo O(n), espacio O(n).

### Cómo ejecutar

Requiere **Python 3.8 o superior**, sin librerías externas. Cada archivo trae sus propias pruebas.

```bash
cd punto5

python detect_cycle.py          # corre las pruebas
python largest_rectangle.py     # corre las pruebas

# Largest Rectangle con entrada propia (imprime 9):
printf "5\n1 2 3 4 5\n" | python largest_rectangle.py
```

En Windows se usa `python` o `py` en lugar de `python3`.

---

## Estructura del repositorio

```
taller-estructuras-datos/
├── README.md
├── .vscode/extensions.json   recomienda la extensión Draw.io Integration
├── diagramas/                puntos 1 a 4 (archivos .drawio)
├── punto5/                   código de HackerRank
└── evidencia/                pantallazos de HackerRank
```
