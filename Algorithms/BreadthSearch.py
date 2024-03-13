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

    Archivo: BreadthSearch.py
    Intención:
    Este archivo define la clase BreadthSearch, la cual representa el algoritmo de búsqueda por amplitud.
    Este algoritmo se encarga de recorrer el árbol de búsqueda de manera horizontal, es decir, expande todos los nodos del nivel actual antes de pasar al siguiente nivel.
    Es un algoritmo completo y encuentra la solución óptima si el costo de las acciones es uniforme, 
    sin embargo, su complejidad en tiempo y espacio es exponencial.
"""

from Models import Node
from Models import Puzzle


def path_goal(node):
    """
    Dado un nodo, devuelve el camino que lleva a ese nodo hasta el nodo raíz.
    """
    path = []
    while node.parent != None:
        path.append(node.puzzle.current_position)
        node = node.parent
    path.reverse()
    return path


def execute_breadth_search():
    """
    Ejecuta el algoritmo de búsqueda por amplitud.
    Se basa en una cola de nodos, donde el primer nodo es el nodo raíz (que contiene el estado inicial del juego).
    Expande el primer nodo y agrega los nodos hijos al final de la cola.
    """
    queue_of_nodes = []
    index = 0

    puzzle = Puzzle()
    puzzle.load_map("Prueba1.txt")
    initial_node = Node(puzzle, None, None, 0, 0)

    queue_of_nodes.append(initial_node)

    while True:
        if index >= len(queue_of_nodes):
            print("No solution found")
            break

        node = queue_of_nodes[index]
        possible_actions = node.get_possible_actions()
        index += 1

        if node.is_goal():
            print("Goal found")
            print(node.puzzle.current_position)
            print("Cost: ", node.cost)
            print("Depht: ", node.depth)
            print("Path: ", path_goal(node))
            break

        for action in possible_actions:
            new_node = node.apply_action(action)
            queue_of_nodes.append(new_node)

