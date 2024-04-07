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
    Se encarga de cargar el mapa, definir la posición del jugador y el objetivo, verificar si una posición es válida
    y calcular el costo de moverse a una posición en el tablero.
"""

from .Position import Position
from .Action import Action
from .Reader import Reader
from copy import deepcopy


class Puzzle(object):
    def __init__(
        self,
        board=[],
        initial_position=None,
        goal_position=None,
        rows=0,
        cols=0,
    ):
        self.board = board
        self.initial_position = initial_position
        self.goal_position = goal_position
        self.rows = rows
        self.cols = cols

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

    def __str__(self):
        """
        Imprime el tablero en un formato fácil de leer.
        """
        return str(self.board).replace("],", "]\n")

    def clone(self) -> "Puzzle":
        # Para el caso del self.board se debe hacer una copia profunda para que no se modifiquen tableros de otros puzzles,
        # ya que en Python las listas son pasadas por referencia y al crear una copia sencilla de la lista (self.board.copy() o self.board[:])
        # los objetos internos dentro de la lista siguen guardando la misma referencia.
        return Puzzle(
            deepcopy(self.board), 
            self.initial_position,
            self.goal_position,
            self.rows,
            self.cols,
        )

    def load_map(self, file: str) -> None:
        """
        Carga el mapa desde un archivo de texto.
        Adicionalmente setea el mapa y el tamaño del mismo (se asume que el mapa es cuadrado)
        """
        self.board = Reader.read_map(file)
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.define_key_positions(self.board)

    def define_key_positions(self, map: list) -> None:
        """
        Setea la posición inicial y la posición objetivo del mapa.
        """
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "2":
                    self.initial_position = Position(i, j, False)
                    map[i][j] = "0"
                elif map[i][j] == "5":
                    self.goal_position = Position(i, j, False)

    def is_valid_position(self, position) -> bool:
        """
        Verifica si una posición es válida.
        Para ello verifica que la posición no esté fuera del tablero y que no sea un muro.
        """
        is_out_of_board = (
            position.y < 0
            or position.y >= self.rows
            or position.x < 0
            or position.x >= self.cols
        )
        is_wall = (
            self.board[position.y][position.x] == "1" if not is_out_of_board else False
        )

        return not is_out_of_board and not is_wall

    def cost(self, position: Position) -> float:
        """
        Devuelve el costo de moverse a una posición en el puzzle.
        """
        # Si la posición se alcanza estando en la nave, el costo es 0.5 siempre
        if position.is_in_spaceship:
            return 0.5

        # Si no va en la nave y la posición resulta en un enemigo, el costo es 5
        if self.board[position.y][position.x] == "4":
            return 5
        
        # En cualquier otro caso (se llega a una posición vacía, o se pasa por el punto de inicio
        # o se llega a la nave, o se llega al objetivo), el costo es 1
        return 1
    
    def heuristic(self, position: Position) -> float:
        """
        Devuelve el costo heurístico de moverse a una posición en el puzzle.
        La heuristica es la distancia en L entre la posición actual y la posición objetivo entre 2 ya que suponemos que siempre está en la nave, pero si la distancia es mayor a 10 (potencia de la nave) se tomarán las primeras 10 casillas con costo de 0.5 y el resto con costo 1.
        """
        Dl = abs(position.x - self.goal_position.x) + abs(position.y - self.goal_position.y)
        if Dl <= 10:
            return Dl/2
        else:
            dif = Dl - 10
            return 5 + dif