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
    Este archivo define la clase CostSearch, la cual representa el algoritmo de búsqueda por costo.
    Este algoritmo se encarga de expandir el nodo con el menor costo acumulado.
    Es un algoritmo completo y además encuentra la solución con el menor costo.
    En el caso promedio, su complejidad temporal ############################ Completar
    Sin embargo, en su peor caso (cuando el costo de las acciones es el mismo) su complejidad en tiempo y espacio es exponencial.
"""

from Node import Node
from Puzzle import Puzzle


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


def node_of_min_cost(queue_of_nodes):
    """
    Dada una cola de nodos, devuelve el índice del nodo con el menor costo acumulado.
    """
    min_cost = queue_of_nodes[0].cost
    min_index = 0

    for i in range(1, len(queue_of_nodes)):
        if queue_of_nodes[i].cost < min_cost:
            min_cost = queue_of_nodes[i].cost
            min_index = i

    return min_index


def execute_cost_search():
    """
    Ejecuta el algoritmo de búsqueda por costo.
    Se basa en una cola de nodos, donde el primer nodo es el nodo raíz (que contiene el estado inicial del juego).
    Expande el nodo con el menor costo acumulado (cola de prioridad) y agrega los nodos hijos al final de la cola.
    """
    queue_of_nodes = []
    index = 0

    puzzle = Puzzle(is_cost_search=True)
    puzzle.load_map("Prueba1.txt")
    initial_node = Node(puzzle, None, None, 0, 0)

    queue_of_nodes.append(initial_node)

    while True:
        if index >= len(queue_of_nodes):
            print("No solution found")
            break

        index = node_of_min_cost(queue_of_nodes)
        node = queue_of_nodes[index]
        possible_actions = node.get_possible_actions()

        if node.is_goal():
            print("Goal found")
            print(node.puzzle.current_position)
            print("Cost: ", node.cost)
            print("Depht: ", node.depth)
            print("Path: ", path_goal(node))
            break

        for action in possible_actions:
            newNode = node.apply_action(action)
            queue_of_nodes.append(newNode)

        del queue_of_nodes[index]


execute_cost_search()
