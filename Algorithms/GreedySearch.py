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
    No obtiene una solución óptima y su complejidad en tiempo y espacio es exponencial.  
"""

from Models.Node import Node
from Models.Puzzle import Puzzle
import Models.Position as Position
from DataStructures import HeuristicHeap
import timeit


def execute_greedy_search(file_path: str):
    """
    Ejecuta el algoritmo de búsqueda greedy.
    Se basa en un montículo mín, para siempre contar con el nodo con menor valor de la heurística en la raíz.
    Al insertar un nodo en el paso de expansión, el heap se encarga de mantener sus propiedades,
    lo que hace que consultar el nodo con menor valor de la heurística sea una operación muy eficiente.
    """
    queue_of_nodes = HeuristicHeap()
    expanded_nodes = 0

    puzzle = Puzzle()
    puzzle.load_map(file_path)
    initial_position = puzzle.initial_position
    initial_node = Node(puzzle, initial_position, 0, 0, 0, None, None)

    queue_of_nodes.insert(initial_node)
    start_time = timeit.default_timer()

    while True:
        if queue_of_nodes.is_empty():
            print("No solution found")
            break

        node = queue_of_nodes.pop()

        if node.is_goal():
            end_time = timeit.default_timer()
            total_time = end_time - start_time
            path = node.get_path_from_root_to_node()
            return (expanded_nodes, node.depth, total_time, node.cost, path)

        possible_actions = node.get_possible_actions()
        expanded_nodes += 1

        for action in possible_actions:
            new_node = node.apply_action(action)
            queue_of_nodes.insert(new_node)
