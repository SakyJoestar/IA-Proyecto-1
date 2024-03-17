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

    Archivo: Position.py
    Intención:
    Este archivo define la clase Position, la cual representa una posición en el tablero.
    Una posición consta de dos coordenadas x, y (que representan la fila y la columna, respectivamente)
    y de un booleano que indica si el agente va en la nave o no.
"""


class Position:
    def __init__(self, y: int, x: int, is_in_spaceship: bool = False):
        self.y = y
        self.x = x
        self.is_in_spaceship = is_in_spaceship

    def __eq__(self, other: "Position"):
        return (
            self.y == other.y
            and self.x == other.x
            and self.is_in_spaceship == other.is_in_spaceship
        )

    def __hash__(self):
        return hash((self.y, self.x, self.is_in_spaceship))

    def __str__(self):
        return f"(fila: {self.y}, columna: {self.x}, está en la nave: {self.is_in_spaceship})"
    
    @staticmethod
    def print_list_of_positions(positions: list):
        for position in positions:
            print(position)

    def position_up(self):
        return Position(self.y - 1, self.x, self.is_in_spaceship)
    
    def position_down(self):
        return Position(self.y + 1, self.x, self.is_in_spaceship)
    
    def position_left(self):
        return Position(self.y, self.x - 1, self.is_in_spaceship)
    
    def position_right(self):
        return Position(self.y, self.x + 1, self.is_in_spaceship)
    
    def change_spaceship_status(self):
        self.is_in_spaceship = not self.is_in_spaceship
