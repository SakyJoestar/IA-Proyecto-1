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

    Archivo: Reader.py
    Intención:
    Este archivo define la clase Reader, la cual se encarga de leer el archivo de entrada
    y cargar el mapa del juego.
"""

class Reader():
    def __init__(self):
        pass

    @staticmethod
    def read_map(file_name: str) -> list:
        """
        Lee el archivo de entrada y devuelve una matriz con la representación del mapa del juego.
        """
        map = []
        with open(file_name, "r") as file:
            for line in file:
                map.append(list(line.split()))
            file.close()
            
        return map