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

    Archivo: greedySearch.py
    Intención:
    Este archivo define la función execute_greedy_search, la cual representa el algoritmo de búsqueda voraz.
    Este algoritmo se encarga de expandir el nodo con el menor valor dado por la heurística.
    En principio este no es un algoritmo completo, pero como intencionalmente se evitan los ciclos
    (pasar por posiciones previamente visitadas), entonces se garantiza que el algoritmo es completo.
    A diferencia del algoritmo de búsqueda por profundidad, la solución de este algoritmo no depende del orden de aplicación
    de los operadores, sino que depende exclusivamente de la función heurística utilizada.
    No obtiene una solución óptima, y su complejidad en tiempo y espacio es exponencial.

    
"""

from Models.Node import Node
from Models.Puzzle import Puzzle
import Models.Position as Position
import timeit


def node_of_min_heuristic(queue_of_nodes: list[Node]):
    """
    Dada una cola de nodos, devuelve el índice del nodo con la menor heurística.
    """
    min_heuristic = queue_of_nodes[0].heuristic
    min_index = 0

    for i in range(1, len(queue_of_nodes)):
        if queue_of_nodes[i].heuristic < min_heuristic:
            min_heuristic = queue_of_nodes[i].heuristic
            min_index = i

    return min_index


def execute_greedy_search(file_path: str):
    """
    Ejecuta el algoritmo de búsqueda greedy.
    Se basa en una cola de nodos, donde el primer nodo es el nodo raíz (que contiene el estado inicial del juego).
    Expande el nodo con la menor heurística (cola de prioridad) y agrega los nodos hijos al final de la cola.
    """
    queue_of_nodes = []
    index = 0
    expanded_nodes = 0

    puzzle = Puzzle()
    puzzle.load_map(file_path)
    initial_position = puzzle.initial_position
    initial_node = Node(puzzle, initial_position, 0, 0, 0, None, None)

    queue_of_nodes.append(initial_node)
    start_time = timeit.default_timer()

    while True:
        if index >= len(queue_of_nodes):
            print("No solution found")
            break

        index = node_of_min_heuristic(queue_of_nodes)
        node = queue_of_nodes[index]

        if node.is_goal():
            end_time = timeit.default_timer()
            total_time = end_time - start_time
            path = node.get_path_from_root_to_node()

            print("Goal found: ", node.position)
            print("Expanded nodes: ", expanded_nodes)
            print("Depht: ", node.depth)
            print("Time of execution (sec): ", total_time)
            print("Cost: ", node.cost)
            print("Path: ")
            Position.print_list_of_positions(path)

            return (expanded_nodes, node.depth, total_time, node.cost, path)

        possible_actions = node.get_possible_actions()
        expanded_nodes += 1

        for action in possible_actions:
            new_node = node.apply_action(action)
            queue_of_nodes.append(new_node)

        del queue_of_nodes[index]
