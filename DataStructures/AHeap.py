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

    Archivo: AHeap.py
    Intención:
    Este archivo define la clase AHeap, la cual hereda de la clase Heap
    e implementa los métodos de comparación basados en la suma del costo acumulado y la heurística de cada nodo.
"""

from .Heap import Heap


class AHeap(Heap):
    def less_than(self, node1, node2):
        return node1.cost + node1.heuristic < node2.cost + node2.heuristic

    def less_than_or_equal(self, node1, node2):
        return node1.cost + node1.heuristic <= node2.cost + node2.heuristic

    def greater_than(self, node1, node2):
        return node1.cost + node1.heuristic > node2.cost + node2.heuristic

    def greater_than_or_equal(self, node1, node2):
        return node1.cost + node1.heuristic >= node2.cost + node2.heuristic

    def equal(self, node1, node2):
        return node1.cost + node1.heuristic == node2.cost + node2.heuristic

    def not_equal(self, node1, node2):
        return node1.cost + node1.heuristic != node2.cost + node2.heuristic
