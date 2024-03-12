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

    Archivo: Node.py
    Intención:
    Este archivo define la clase Node, la cual define un nodo en el árbol de búsqueda.
"""

from Action import Action
from Puzzle import Puzzle


class Node(object):
    def __init__(
        self, puzzle: Puzzle, action: Action, parent: "Node", depth: int, cost: float
    ):
        self.puzzle = puzzle
        self.action = action
        self.parent = parent
        self.depth = depth
        self.cost = cost

    def get_possible_actions(self) -> list[Action]:
        """
        Devuelve una lista con las acciones posibles que se pueden realizar en el estado actual.
        Para ello consulta la posición del nodo padre y verifica la posibilidad de moverse en cada una de las direcciones.
        """
        possible_actions = []
        parentPosition = (
            self.parent.puzzle.current_position if self.parent else (-1, -1)
        )
        if self.puzzle.is_valid_move(Action.UP, parentPosition):
            possible_actions.append(Action.UP)
        if self.puzzle.is_valid_move(Action.DOWN, parentPosition):
            possible_actions.append(Action.DOWN)
        if self.puzzle.is_valid_move(Action.LEFT, parentPosition):
            possible_actions.append(Action.LEFT)
        if self.puzzle.is_valid_move(Action.RIGHT, parentPosition):
            possible_actions.append(Action.RIGHT)

        return possible_actions

    def apply_action(self, action: Action) -> "Node":
        """
        Aplica una acción al estado actual y devuelve un nuevo nodo con el estado resultante.
        """
        newPuzzle = self.puzzle.clone()
        cost = newPuzzle.move(action)
        return Node(newPuzzle, action, self, self.depth + 1, self.cost + cost)

    def is_goal(self) -> bool:
        return self.puzzle.is_goal()
