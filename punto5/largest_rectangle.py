"""
Punto 5b - Largest Rectangle (HackerRank)
https://www.hackerrank.com/challenges/largest-rectangle/problem

Pila monotona: O(n) tiempo, O(n) espacio.

Ejecutar pruebas:      python largest_rectangle.py
Ejecutar con entrada:  python largest_rectangle.py < entrada.txt
  (formato: primera linea n, segunda linea las n alturas)
"""
import sys


def largestRectangle(h):
    stack = []  # tuplas (indice_inicio, altura) con alturas crecientes
    max_area = 0
    for i, height in enumerate(list(h) + [0]):  # el 0 final vacia la pila
        start = i
        while stack and stack[-1][1] > height:
            idx, hgt = stack.pop()
            max_area = max(max_area, hgt * (i - idx))
            start = idx
        stack.append((start, height))
    return max_area


def run_tests():
    casos = [
        ([1, 2, 3, 4, 5], 9),   # ejemplo de HackerRank
        ([2, 1, 5, 6, 2, 3], 10),
        ([5], 5),
        ([1, 1, 1, 1], 4),
        ([6, 5, 4, 3, 2, 1], 12),
        ([2, 4], 4),
        ([0, 0, 0], 0),
    ]
    for h, esperado in casos:
        obtenido = largestRectangle(h)
        estado = "OK " if obtenido == esperado else "FALLO"
        print(f"[{estado}] h={h}: esperado={esperado} obtenido={obtenido}")
        assert obtenido == esperado
    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    datos = "" if sys.stdin.isatty() else sys.stdin.read()
    if not datos.strip():
        run_tests()
    else:
        lineas = datos.split("\n")
        n = int(lineas[0])
        h = list(map(int, lineas[1].split()))[:n]
        print(largestRectangle(h))
