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

    Archivo: Environment.py
    Intención:
    Este archivo define la clase Environment, la cual se encarga de manejar la interfaz gráfica del juego.
"""

import pygame
import os
import time

ruta_actual = os.path.dirname(__file__)


class Environment:
    def __init__(self, width, height, map_matrix, agent):
        self.map = map_matrix
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.agent = agent

        self.left_margin = width * 0.1
        self.right_margin = width * 0.1
        self.top_margin = height * 0.1
        self.bottom_margin = height * 0.1

        self.rectangle_width = (
            width - self.left_margin - self.right_margin
        ) // self.cols
        self.width = (
            (self.cols * self.rectangle_width) + self.left_margin + self.right_margin
        )

        self.rectangle_height = (
            height - self.top_margin - self.bottom_margin
        ) // self.rows
        self.height = (
            self.rows * self.rectangle_height + self.top_margin + self.bottom_margin
        )

        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 32)

        self.background_color = (165, 201, 202)
        self.wall_color = (107, 132, 139)
        self.free_space_color = (255, 255, 255)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.background_color)
        pygame.display.set_caption("Smart Mandalorian")

        self.fit_icons()

    def fit_icons(self):
        """
        Carga y ajusta el tamaño de los íconos de los agentes según las dimensiones del tablero.
        """
        # Mandalorian
        self.mandalorian_icon = pygame.image.load(
            os.path.join(ruta_actual, "../Static/Mandalorian.png")
        )
        self.mandalorian_icon = pygame.transform.scale(
            self.mandalorian_icon,
            (self.rectangle_width * 0.5, self.rectangle_height * 0.7),
        )
        mandalorian_icon_offset_x = (
            self.rectangle_width - self.mandalorian_icon.get_width()
        ) // 2
        mandalorian_icon_offset_y = (
            self.rectangle_height - self.mandalorian_icon.get_height()
        ) // 2
        self.agent.update_icon(self.mandalorian_icon)
        self.agent.update_current_position(
            self.rectangle_width,
            self.rectangle_height,
            mandalorian_icon_offset_x,
            mandalorian_icon_offset_y,
            self.left_margin,
            self.top_margin,
        )

        # Grogu
        self.grogu_icon = pygame.image.load(
            os.path.join(ruta_actual, "../Static/Grogu.png")
        )
        self.grogu_icon = pygame.transform.scale(
            self.grogu_icon,
            (self.rectangle_width * 0.7, self.rectangle_height * 0.7),
        )
        self.grogu_icon_offset_x = (
            self.rectangle_width - self.grogu_icon.get_width()
        ) // 2
        self.grogu_icon_offset_y = (
            self.rectangle_height - self.grogu_icon.get_height()
        ) // 2

        # Mandalorian y Grogu
        self.mandalorian_grogu_icon = pygame.image.load(
            os.path.join(ruta_actual, "../Static/Mandalorian_with_grogu.jpg")
        )
        self.mandalorian_grogu_icon = pygame.transform.scale(
            self.mandalorian_grogu_icon,
            (self.rectangle_width * 0.6, self.rectangle_height * 0.7),
        )
        mandalorian_grogu_icon_offset_x = (
            self.rectangle_width - self.mandalorian_grogu_icon.get_width()
        ) // 2
        mandalorian_grogu_icon_offset_y = (
            self.rectangle_height - self.mandalorian_grogu_icon.get_height()
        ) // 2

        # Spaceship
        self.spaceship_icon = pygame.image.load(
            os.path.join(ruta_actual, "../Static/Spaceship.png")
        )
        self.spaceship_icon = pygame.transform.scale(
            self.spaceship_icon,
            (self.rectangle_width * 0.7, self.rectangle_height * 0.4),
        )
        self.spaceship_icon_offset_x = (
            self.rectangle_width - self.spaceship_icon.get_width()
        ) // 2
        self.spaceship_icon_offset_y = (
            self.rectangle_height - self.spaceship_icon.get_height()
        ) // 2

        # Enemy
        self.enemy_icon = pygame.image.load(
            os.path.join(ruta_actual, "../Static/Enemy.png")
        )
        self.enemy_icon = pygame.transform.scale(
            self.enemy_icon, (self.rectangle_width * 0.4, self.rectangle_height * 0.7)
        )
        self.enemy_icon_offset_x = (
            self.rectangle_width - self.enemy_icon.get_width()
        ) // 2
        self.enemy_icon_offset_y = (
            self.rectangle_height - self.enemy_icon.get_height()
        ) // 2

    def display_environment(self, path: list):
        """
        Dibuja el tablero y los íconos de los agentes.
        Además arranca la animación, según el camino encontrado por el algoritmo previamente ejecutado.
        """
        self.agent.update_path_to_follow(path)
        index = 0

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            for row in range(self.rows):
                for col in range(self.cols):
                    rectangle = pygame.Rect(
                        col * self.rectangle_width + self.left_margin,
                        row * self.rectangle_height + self.top_margin,
                        self.rectangle_width,
                        self.rectangle_height,
                    )

                    if self.map[row][col] == "1":  # Muro
                        self.window.fill(self.wall_color, rectangle)
                        pygame.draw.rect(self.window, (0, 0, 0), rectangle, 1)

                    else:
                        self.window.fill(self.free_space_color, rectangle)
                        pygame.draw.rect(self.window, (0, 0, 0), rectangle, 1)

                        if self.map[row][col] == "3":  # Nave
                            self.window.blit(
                                self.spaceship_icon,
                                (
                                    col * self.rectangle_width
                                    + self.left_margin
                                    + self.spaceship_icon_offset_x,
                                    row * self.rectangle_height
                                    + self.top_margin
                                    + self.spaceship_icon_offset_y,
                                ),
                            )

                        elif self.map[row][col] == "4":  # Enemigo
                            self.window.blit(
                                self.enemy_icon,
                                (
                                    col * self.rectangle_width
                                    + self.left_margin
                                    + self.enemy_icon_offset_x,
                                    row * self.rectangle_height
                                    + self.top_margin
                                    + self.enemy_icon_offset_y,
                                ),
                            )

                        elif self.map[row][col] == "5":  # Grogu
                            self.window.blit(
                                self.grogu_icon,
                                (
                                    col * self.rectangle_width
                                    + self.left_margin
                                    + self.grogu_icon_offset_x,
                                    row * self.rectangle_height
                                    + self.top_margin
                                    + self.grogu_icon_offset_y,
                                ),
                            )
            
            # Se llegó al final del camino, se termina la animación
            if index == len(path) - 1:
                self.agent.update_icon(self.mandalorian_grogu_icon)
                self.agent.draw(self.window)
                pygame.display.flip()

                while True:
                    event = pygame.event.poll()
                    if event.type == pygame.QUIT:
                        break

            index = self.agent.update_position(self.map, index)
            self.agent.draw(self.window)

            pygame.display.flip()
            time.sleep(0.01)

        pygame.quit()
