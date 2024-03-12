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

    Archivo: Puzzle.py
    Intención:
    Este archivo define la clase Puzzle, la cual representa el estado del juego.
    Se encarga de cargar el mapa, definir la posición del jugador y el objetivo, y verificar si una posición es válida.
"""

from Action import Action


class Puzzle(object):
    def __init__(
        self,
        board=[],
        current_position=None,
        goal_position=None,
        size=0,
        zero=0,
        power=0,
        is_cost_search: bool = False,
        is_breadth_search: bool = False,
    ):
        self.board = board
        self.current_position = current_position
        self.goal_position = goal_position
        self.size = size
        self.zero = zero
        self.power = power
        self.is_cost_search = is_cost_search
        self.is_breadth_search = is_breadth_search

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        """
        Imprime el tablero en un formato fácil de leer.
        """
        return str(self.board).replace("],", "]\n")

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

    def load_map(self, file: str) -> None:
        """
        Carga el mapa desde un archivo de texto.
        Adicionalmente setea el mapa y el tamaño del mismo (se asume que el mapa es cuadrado)
        """
        with open(file, "r") as file:
            aux_map = file.read().splitlines()

        map_string = ["".join(fila.split()) for fila in aux_map]
        map = [list(fila) for fila in map_string]
        self.board = map
        self.size = len(map)
        self.define_position(map)

    def define_position(self, map: list) -> None:
        """
        Setea la posición inicial y la posición objetivo del mapa.
        """
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "2":
                    self.current_position = (i, j)
                    map[i][j] = "0"
                elif map[i][j] == "5":
                    self.goal_position = (i, j)

    def is_valid_position(self, row, col, parent_position) -> bool:
        """
        Verifica si una posición es válida.
        Para ello verifica que la posición no sea la misma que la del padre, que no esté fuera del tablero y que no sea un muro.
        """
        is_its_previous_parent = (row, col) == parent_position and self.power == 0
        is_out_of_board = row < 0 or row >= self.size or col < 0 or col >= self.size
        is_wall = self.board[row][col] == "1" if not is_out_of_board else False

        return not is_its_previous_parent and not is_out_of_board and not is_wall

    def is_valid_move(self, action: Action, parent_position: tuple[int, int]) -> bool:
        """
        Verifica si un movimiento es válido.
        Para ello verifica si la posición a la que se quiere mover (según la acción) es válida (usando is_valid_position).
        """
        y, x = self.current_position

        move_up = (y - 1, x)
        move_down = (y + 1, x)
        move_left = (y, x - 1)
        move_right = (y, x + 1)

        if action == Action.UP:
            return self.is_valid_position(move_up[0], move_up[1], parent_position)
        elif action == Action.DOWN:
            return self.is_valid_position(move_down[0], move_down[1], parent_position)
        elif action == Action.LEFT:
            return self.is_valid_position(move_left[0], move_left[1], parent_position)
        elif action == Action.RIGHT:
            return self.is_valid_position(move_right[0], move_right[1], parent_position)
        else:
            return False

    def move(self, action: Action) -> float:
        """
        Setea la nueva posición del jugador según la acción realizada y retorna el costo asociado a ese movimiento.
        """
        y, x = self.current_position

        if action == Action.UP:
            new_row, new_col = y - 1, x
        elif action == Action.DOWN:
            new_row, new_col = y + 1, x
        elif action == Action.LEFT:
            new_row, new_col = y, x - 1
        elif action == Action.RIGHT:
            new_row, new_col = y, x + 1

        cost = self.cost(new_row, new_col) if self.is_cost_search else 0
        self.current_position = (new_row, new_col)

        return cost

    def clone(self) -> "Puzzle":
        return Puzzle(
            self.board[:],
            self.current_position,
            self.goal_position,
            self.size,
            self.zero,
            self.power,
            self.is_cost_search,
            self.is_breadth_search
        )

    def is_goal(self) -> bool:
        return self.current_position == self.goal_position

    def cost(self, row: int, col: int) -> float:
        cost = 0
        if self.power > 0:
            cost = 0.5
            self.power -= 1
            return cost

        if self.board[row][col] == "0":
            cost = 1
        if self.board[row][col] == "4":
            cost = 5
        if self.board[row][col] == "3":
            cost = 1
            self.activate_power()
        return cost

    def activate_power(self) -> None:
        self.power = 10
