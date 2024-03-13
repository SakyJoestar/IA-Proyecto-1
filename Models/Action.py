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

    Archivo: Action.py
    Intención:
    Este archivo define la clase Action, la cual guarda las acciones posibles que se pueden realizar en el juego.
    Hereda de la clase Enum para poder definir las acciones como constantes numéricas.
"""

from enum import Enum


class Action(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
