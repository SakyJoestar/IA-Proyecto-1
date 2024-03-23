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

    Archivo: CostHeap.py
    Intención:
    Este archivo define la clase CostHeap, la cual hereda de la clase Heap
    e implementa los métodos de comparación basados en el costo acumulado de cada nodo.
"""

from .Heap import Heap


class CostHeap(Heap):
    def less_than(self, node1, node2):
        return node1.cost < node2.cost

    def less_than_or_equal(self, node1, node2):
        return node1.cost <= node2.cost

    def greater_than(self, node1, node2):
        return node1.cost > node2.cost

    def greater_than_or_equal(self, node1, node2):
        return node1.cost >= node2.cost

    def equal(self, node1, node2):
        return node1.cost == node2.cost

    def not_equal(self, node1, node2):
        return node1.cost != node2.cost
