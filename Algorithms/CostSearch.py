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

    Archivo: CostSearch.py
    Intención:
    Este archivo define la función execute_cost_search, la cual representa el algoritmo de búsqueda por costo.
    Este algoritmo se encarga de expandir el nodo con el menor costo acumulado.
    Es un algoritmo completo y además encuentra la solución con el menor costo.
    Su costo temporal y espacial está definido en términos de la cantidad de nodos que se deben expandir, 
    que en este caso corresponden al número de nodos con costo menor al de la solución óptima. 
    Sin embargo, en su peor caso (cuando el costo de las acciones es el mismo) su complejidad en tiempo y espacio es exponencial
    (termina comportándose como una búsqueda por amplitud).
"""

from Models.Node import Node
from Models.Puzzle import Puzzle
import Models.Position as Position
from DataStructures import CostHeap
import timeit


def execute_cost_search(file_path):
    """
    Ejecuta el algoritmo de búsqueda por costo.
    Se basa en un montículo mín, para siempre contar con el nodo con menor costo en la raíz.
    Al insertar un nodo en el paso de expansión, el heap se encarga de mantener sus propiedades,
    lo que hace que consultar el nodo con menor costo sea una operación muy eficiente.
    """
    queue_of_nodes = CostHeap()
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
