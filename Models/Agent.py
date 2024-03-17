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

    Archivo: Agent.py
    Intención:
    Este archivo define la clase Agent, la cual representa el objeto que se mueve en el entorno de juego. 
    Se encarga de realizar las acciones que le indique el algoritmo de búsqueda seleccionado por el usuario.
    No se encarga de ejecutar la lógica del juego, sino exclusivamente de ejecutar las acciones de movimiento.
    La lógica del agente está dada por los algoritmos de búsqueda definidos en el paquete ../Algorithms.
"""


class Agent:
    @staticmethod
    def find_agent(map):
        for row in range(len(map)):
            for col in range(len(map[0])):
                if map[row][col] == "2":
                    return (row, col)
        return None

    def __init__(self, y, x):
        # Las posiciones x, y guardan la posición en términos de los indices del tablero de juego.
        self.y = y  # Filas
        self.x = x  # Columnas

        # Las posiciones estáticas, dinámicas y objetivo guardan la posición en términos de píxeles de la ventana
        self.static_y = y
        self.static_x = x

        self.dinamic_y = y
        self.dinamic_x = x

        self.goal_y = y
        self.goal_x = x

        # Tamaño de cada rectangulo en la cuadrícula, para efectos de ajustar la posición del agente en la ventana
        self.rectangle_width = 0
        self.rectangle_height = 0

        self.path_to_follow = []

    def update_path_to_follow(self, path):
        self.path_to_follow = path

    def update_icons(self, mandalorian_icon, spaceship_icon):
        self.mandalorian_icon = mandalorian_icon
        self.spaceship_icon = spaceship_icon
        self.current_icon = mandalorian_icon

    def update_current_icon(self, icon):
        self.current_icon = icon

    def update_current_position(
        self,
        rectangle_width,
        rectangle_height,
        offset_x,
        offset_y,
        left_margin,
        top_margin,
    ):
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height

        # Ajustar la posición actual del agente en términos de los píxeles de la ventana
        self.static_x = self.static_x * self.rectangle_width + left_margin + offset_x
        self.static_y = self.static_y * self.rectangle_height + top_margin + offset_y

        self.dinamic_x = self.dinamic_x * self.rectangle_width + left_margin + offset_x
        self.dinamic_y = self.dinamic_y * self.rectangle_height + top_margin + offset_y

    def identify_action(self, map, index):
        """
        Identifica el movimiento a realizar por el agente según el camino previamente asignado y
        el estado actual de la animación (definido por index).
        """
        (diff_y, diff_x) = (
            self.path_to_follow[index + 1].y - self.path_to_follow[index].y,
            self.path_to_follow[index + 1].x - self.path_to_follow[index].x,
        )

        if diff_y == 1 and diff_x == 0:
            return "DOWN"
        elif diff_y == -1 and diff_x == 0:
            return "UP"
        elif diff_y == 0 and diff_x == 1:
            return "RIGHT"
        elif diff_y == 0 and diff_x == -1:
            return "LEFT"

    def move(self, action):
        """
        Mueve el agente según la acción indicada.
        """
        if action == "DOWN":
            self.goal_x = self.static_x
            self.goal_y = self.static_y + self.rectangle_height
            self.dinamic_y += self.speed_y

        elif action == "UP":
            self.goal_x = self.static_x
            self.goal_y = self.static_y - self.rectangle_height
            self.dinamic_y -= self.speed_y

        elif action == "RIGHT":
            self.goal_x = self.static_x + self.rectangle_width
            self.dinamic_x += self.speed_x
            self.goal_y = self.static_y

        elif action == "LEFT":
            self.goal_x = self.static_x - self.rectangle_width
            self.dinamic_x -= self.speed_x
            self.goal_y = self.static_y

    def update_position(self, map, index):
        """
        Mueve el agente según el camino previamente asignado y
        el estado actual de la animación (definido por index).
        """
        self.speed_x = 1
        self.speed_y = 1
        found_spaceship = False
        found_enemy = False

        action = self.identify_action(map, index)

        self.move(action)

        if self.path_to_follow[index].is_in_spaceship:
            self.current_icon = self.spaceship_icon
        else:
            self.current_icon = self.mandalorian_icon

        if self.dinamic_x == self.goal_x and self.dinamic_y == self.goal_y:
            self.static_x = self.goal_x
            self.static_y = self.goal_y

            if action == "DOWN":
                self.y += 1

            elif action == "UP":
                self.y -= 1

            elif action == "RIGHT":
                self.x += 1

            elif action == "LEFT":
                self.x -= 1

            index += 1

            if index == len(self.path_to_follow) - 1:
                map[self.y][self.x] = "0"

            if map[self.y][self.x] == "3":
                found_spaceship = True

            if (
                map[self.y][self.x] == "4"
                and not self.path_to_follow[index].is_in_spaceship
                and not self.path_to_follow[index - 1].is_in_spaceship
            ):
                found_enemy = True

        return (index, found_spaceship, found_enemy)

    def draw(self, window):
        """
        Dibuja el agente en la ventana.
        """
        window.blit(self.current_icon, (self.dinamic_x, self.dinamic_y))
