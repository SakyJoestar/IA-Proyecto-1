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

    Archivo: DepthSearch.py
    Intención:
    Este archivo define la función execute_depth_search, la cual representa el algoritmo de búsqueda por profundidad.
    Este algoritmo se encarga de expandir el nodo más profundo en el árbol de búsqueda.
    En principio este no es un algoritmo completo, pero como intencionalmente se evitan los ciclos
    (pasar por posiciones previamente visitadas), entonces se garantiza que el algoritmo es completo.
    En el peor de los casos su complejidad temporal es exponencial, aunque la complejidad en espacio siempre es
    proporcional a la profundidad * el factor de ramificación. Es debido a esta reducción en la complejidad espacial
    que el algoritmo de búsqueda por profundidad es preferido sobre la búsqueda por amplitud.
"""

from Models.Node import Node
from Models.Puzzle import Puzzle
from Models.Position import Position
import timeit


def execute_depth_search(file_path: str):
    """
    Ejecuta el algoritmo de búsqueda por profundidad.
    Se basa en una pila de nodos, donde el primer nodo es el nodo raíz (que contiene el estado inicial del juego).
    Expande el nodo más profundo en el árbol de búsqueda y agrega los nodos hijos al inicio de la pila.
    """
    # Para modelar la pila de nodos se utiliza una lista.
    # El método append de las listas en Python agrega un elemento al final de la lista,
    # pero el método pop retorna y elimina de la lista el último elemento, lo que permite simular
    # el comportamiento de una pila.
    stack_of_nodes = []
    expanded_nodes = 0

    puzzle = Puzzle()
    puzzle.load_map(file_path)
    initial_position = puzzle.initial_position

    # Para asegurar que el algoritmo realmente tenga una complejidad espacial proporcional
    # a la profundidad del árbol * factor de ramificación, se va a llevar registro del número de nodos hijos que tiene cada nodo.
    # Este es el último parámetro del constructor de la clase Node, que es opcional y cuyo registro no se lleva en los otros algoritmos.
    initial_node = Node(puzzle, initial_position, 0, 0, 0, None, None, 0)

    stack_of_nodes.append(initial_node)
    start_time = timeit.default_timer()

    while True:
        if len(stack_of_nodes) == 0:
            print("No solution found")
            break

        node = stack_of_nodes.pop()

        if node.is_goal():
            end_time = timeit.default_timer()
            total_time = end_time - start_time
            path = node.get_path_from_root_to_node()
            return (expanded_nodes, node.depth, total_time, node.cost, path)

        possible_actions = node.get_possible_actions()
        expanded_nodes += 1

        # Si la rama ya no se puede expandir más, entonces se llama al método verify_node_and_ancestors_to_free_memory
        # para que setear a None los nodos de esta rama que ya no tienen hijos que expandir, y por tanto no son necesarios
        # para lo que resta del algoritmo.
        if len(possible_actions) == 0:
            node.verify_node_and_ancestors_to_free_memory()
            continue
        
        for action in possible_actions:
            new_node = node.apply_action(action)
            stack_of_nodes.append(new_node)
            node.number_of_children += 1
