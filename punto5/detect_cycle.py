"""
Punto 5a - Detect a Cycle in a Linked List (HackerRank)
https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

Algoritmo de Floyd (tortuga y liebre): O(n) tiempo, O(1) espacio.
Ejecutar:  python detect_cycle.py
"""


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    """Retorna 1 si la lista tiene ciclo, 0 si no."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return 1
    return 0


def build_list(values, cycle_to=None):
    """Crea una lista con `values`. Si cycle_to es un indice, la cola apunta a ese nodo."""
    if not values:
        return None
    nodes = [SinglyLinkedListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if cycle_to is not None:
        nodes[-1].next = nodes[cycle_to]
    return nodes[0]


def run_tests():
    casos = [
        ("lista vacia", build_list([]), 0),
        ("un nodo sin ciclo", build_list([1]), 0),
        ("sin ciclo (ejemplo 1)", build_list([1, 2, 3]), 0),
        ("ciclo 3 -> 1 (ejemplo 2)", build_list([1, 2, 3], cycle_to=0), 1),
        ("un nodo apuntando a si mismo", build_list([1], cycle_to=0), 1),
        ("ciclo en el medio", build_list([1, 2, 3, 4, 5], cycle_to=2), 1),
    ]
    for nombre, head, esperado in casos:
        obtenido = has_cycle(head)
        estado = "OK " if obtenido == esperado else "FALLO"
        print(f"[{estado}] {nombre}: esperado={esperado} obtenido={obtenido}")
        assert obtenido == esperado
    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    run_tests()
