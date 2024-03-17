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
from Models import Position
import time


def path_goal(node):
    """
    Dado un nodo, devuelve el camino que lleva a ese nodo hasta el nodo raíz.
    """
    path = []
    while node != None:
        path.append(node.position)
        node = node.parent
    path.reverse()
    return path


def execute_breadth_search(file_path):
    """
    Ejecuta el algoritmo de búsqueda por amplitud.
    Se basa en una cola de nodos, donde el primer nodo es el nodo raíz (que contiene el estado inicial del juego).
    Expande el primer nodo y agrega los nodos hijos al final de la cola.
    """
    queue_of_nodes = []
    index = 0
    expanded_nodes = 0

    puzzle = Puzzle()
    puzzle.load_map(file_path)
    initial_position = puzzle.initial_position
    initial_node = Node(puzzle, initial_position, 0, 0, None, 0, None)

    queue_of_nodes.append(initial_node)
    start_time = time.time()
    
    while True:
        if index >= len(queue_of_nodes):
            print("No solution found")
            break
        
        node = queue_of_nodes[index]
        possible_actions = node.get_possible_actions()
        index += 1

        if node.is_goal():
            end_time = time.time()
            total_time = end_time - start_time
            path = path_goal(node)

            print("Goal found: ", node.position)
            print("Expanded nodes: ", expanded_nodes)
            print("Depht: ", node.depth)
            print("Time of execution (sec): ", total_time)
            print("Cost: ", node.cost)
            print("Path: ")
            Position.print_list_of_positions(path)

            return (expanded_nodes, node.depth, total_time, node.cost, path)

        for action in possible_actions:
            new_node = node.apply_action(action)
            queue_of_nodes.append(new_node)
            expanded_nodes += 1

