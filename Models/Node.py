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

from .Position import Position
from .Action import Action
from .Puzzle import Puzzle


class Node(object):
    def __init__(
        self,
        puzzle: Puzzle,
        position: Position,
        fuel: int,
        cost: float,
        parent: "Node",
        depth: int,
        action: Action,
    ):
        self.puzzle = puzzle
        self.position = position
        self.fuel = fuel
        self.cost = cost
        self.parent = parent
        self.depth = depth
        self.action = action

    def __str__(self):
        return f"Posición: {self.position}, combustible: {self.fuel}, costo: {self.cost}, profundidad: {self.depth}, acción: {self.action}"

    @staticmethod
    def have_common_previous_position(
        possible_position: Position, node: "Node"
    ) -> bool:
        """
        Verifica si una posición se encuentra en el camino hacía la raíz de un nodo.
        """
        # Si el nodo a evaluar es None entonces no hubo coincidencias.
        if node is None:
            return False

        # Si la posición evaluada es igual a la posición del nodo, entonces se encontró una posición común en el camino.
        if possible_position == node.position:
            return True

        # Se sigue verificando camino arriba con el padre del nodo.
        return Node.have_common_previous_position(possible_position, node.parent)

    def is_valid_move(self, action: Action) -> bool:
        """
        Verifica si un posible movimiento es válido.
        Para ello verifica:
        *Que la posición a la que se quiere mover (según la acción) sea válida en el puzzle (self.puzzle.is_valid_position).
         Para que una posición sea válida, debe estar dentro de los límites del tablero y no debe ser un muro.
        *Que la posición a la que se quiere mover no sea una posición que ya se haya visitado
         en el camino desde la raíz hasta el nodo actual (have_common_previous_position).
        """
        new_position = None

        if action == Action.UP:
            new_position = self.position.position_up()
        elif action == Action.DOWN:
            new_position = self.position.position_down()
        elif action == Action.LEFT:
            new_position = self.position.position_left()
        elif action == Action.RIGHT:
            new_position = self.position.position_right()

        # Verificar si la posición a la que se quiere mover es una posición válida en el puzzle.
        is_valid_position = self.puzzle.is_valid_position(new_position)
        if not is_valid_position:
            return False

        # Si la posición a la que se quiere mover es una posición válida en el puzzle,
        # se procede a verificar si la posición a la que se quiere mover no es una posición que ya se haya visitado

        # Verificar si adelante hay una nave.
        # Si adelante hay una nave, se sobreentiende que self.position.is_in_spaceship = False
        # y por tanto new_position.is_in_spaceship = False
        if self.puzzle.board[new_position.y][new_position.x] == "3":
            new_position.change_spaceship_status()

        # Verificar si en el siguiente movimiento se acaba el combustible de la nave.
        # Si el combustible está por acabarse, se sobreentiende que self.position.is_in_spaceship = True
        # y por tanto new_position.is_in_spaceship = True
        if self.fuel == 1:
            new_position.change_spaceship_status()

        return not Node.have_common_previous_position(new_position, self.parent)

    def get_possible_actions(self) -> list[Action]:
        """
        Devuelve una lista con las acciones posibles que se pueden realizar en el estado actual.
        Para ello utiliza el método self.is_valid_move.
        Este método verifica que la posición a la que se quiere mover (según la acción) sea válida en el puzzle
        y que no sea una posición que ya se haya visitado en el camino desde la raíz hasta el nodo actual.
        """
        possible_actions = []

        for action in [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]:
            if self.is_valid_move(action):
                possible_actions.append(action)

        return possible_actions

    def apply_action(self, action: Action) -> "Node":
        """
        Aplica una acción al estado actual y devuelve un nuevo nodo con el estado resultante.
        """
        new_puzzle = self.puzzle.clone()
        new_position = None
        new_fuel = self.fuel

        if action == Action.UP:
            new_position = self.position.position_up()
        elif action == Action.DOWN:
            new_position = self.position.position_down()
        elif action == Action.LEFT:
            new_position = self.position.position_left()
        elif action == Action.RIGHT:
            new_position = self.position.position_right()

        # Calcula el costo del movimiento antes de haber cambiado cualquier estado sobre el puzzle.
        new_cost = self.cost + new_puzzle.cost(new_position)

        # Verificar si va en la nave, y por lo tanto el combustible disminuye.
        if self.position.is_in_spaceship:
            new_fuel -= 1

            # Verificar si el movimiento resulta en una posición donde se ha acabado el combustible.
            # Si el combustible está por acabarse, se sobreentiende que self.position.is_in_spaceship = True
            # y por tanto new_position.is_in_spaceship = True
            if new_fuel == 0:
                new_position.change_spaceship_status()

        # Verificar si el movimiento resulta en una posición donde hay una nave.
        # Si adelante hay una nave, se sobreentiende que self.position.is_in_spaceship = False
        # y por tanto new_position.is_in_spaceship = False
        if new_puzzle.board[new_position.y][new_position.x] == "3":
            new_position.change_spaceship_status()
            new_fuel = 10
            new_puzzle.board[new_position.y][new_position.x] = "0"

        return Node(
            new_puzzle, new_position, new_fuel, new_cost, self, self.depth + 1, action
        )

    def is_goal(self) -> bool:
        return (
            self.position.x == self.puzzle.goal_position.x
            and self.position.y == self.puzzle.goal_position.y
        )
