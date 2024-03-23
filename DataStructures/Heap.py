"""
    Inteligencia Artificial - 750022C 01
    Proyecto I - Smart Mandalorian

    Autores: 
    John Freddy Belalcázar Rojas - 2182464
    Samuel Galindo Cuevas - 2177491
    Nicolás Herrera Marulanda - 2182551
    Christian David Vargas Gutiérrez - 2179172

    Profesor:
    Oscar Bedoya PhD

    Archivo: Heap.py
    Intención:
    Este archivo define la clase Heap, la cual modela una estructura de datos de tipo heap.
    Se utiliza para la implementación de la cola de prioridad en los algoritmos de búsqueda que
    expanden nodos con base en su costo.
    La razón por la cual un montículo es una mejor estructura de datos para una cola de prioridad
    es debido a su eficiencia en la inserción y eliminación de elementos (O(log n)), y en la obtención
    del elemento con menor costo (O(1)).

    Define la lógica básica para un heap, pero deja la implementación de las comparaciones entre nodos
    a las subclases que hereden de esta clase. Esto permite que se pueda implementar un heap que utilice
    diferentes criterios de comparación entre nodos, como por ejemplo, un heap que ordene los nodos por
    su costo acumulado, por su heurística, por la suma de ambos, etc.
"""


class Heap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def less_than(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def less_than_or_equal(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def greater_than(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def greater_than_or_equal(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def equal(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def not_equal(self, node1, node2):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def heapify_up(self, index):
        """
        Va subiendo el nodo en la posición index hasta que se cumpla la propiedad de heap.
        """
        parent = (index - 1) // 2
        while index != 0 and self.less_than(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        """
        Va bajando el nodo en la posición index hasta que se cumpla la propiedad de heap.
        """
        left = 2 * index + 1
        right = 2 * index + 2

        while (
            left < len(self.heap)
            and self.greater_than(self.heap[index], self.heap[left])
        ) or (
            right < len(self.heap)
            and self.greater_than(self.heap[index], self.heap[right])
        ):
            smallest = 0

            if (right >= len(self.heap)) or (
                self.less_than(self.heap[left], self.heap[right])
            ):
                smallest = left
            else:
                smallest = right

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest
            left = 2 * index + 1
            right = 2 * index + 2

    def insert(self, node):
        """
        Inserta un nodo en el heap y lo acomoda en la posición correcta.
        """
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Elimina el nodo con menor costo del heap y lo retorna.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)
        return root
