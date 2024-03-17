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
import sys

ruta_actual = os.path.dirname(__file__)


class Environment:
    def __init__(self, width, height, map_matrix, agent):
        pygame.init()

        self.map = map_matrix
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.agent = agent

        self.left_margin = width * 0.1
        self.right_margin = width * 0.1
        self.top_margin = height * 0.1
        self.bottom_margin = height * 0.25

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
        self.font_title_1 = pygame.font.Font(pygame.font.get_default_font(), 32)
        self.font_title_2 = pygame.font.Font(pygame.font.get_default_font(), 28)
        self.font_subtitle = pygame.font.Font(pygame.font.get_default_font(), 14)
        self.font_body = pygame.font.Font(pygame.font.get_default_font(), 12)

        self.background_color = (165, 201, 202)
        self.wall_color = (107, 132, 139)
        self.free_space_color = (255, 255, 255)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.background_color)
        pygame.display.set_caption("Smart Mandalorian")

        self.fit_icons()

        pygame.mixer.init()
        self.upload_music()

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

        self.agent.update_icons(self.mandalorian_icon, self.spaceship_icon)
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
        self.mandalorian_grogu_icon_offset_x = (
            self.rectangle_width - self.mandalorian_grogu_icon.get_width()
        ) // 2
        self.mandalorian_grogu_icon_offset_y = (
            self.rectangle_height - self.mandalorian_grogu_icon.get_height()
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

    def upload_music(self):
        """
        Carga la música de fondo del juego.
        """
        self.main_theme = pygame.mixer.Sound(
            os.path.join(ruta_actual, "../Static/Sounds/main_theme.mp3")
        )

        self.win_sound = pygame.mixer.Sound(
            os.path.join(ruta_actual, "../Static/Sounds/win.mp3")
        )

        self.spaceship_sound = pygame.mixer.Sound(
            os.path.join(ruta_actual, "../Static/Sounds/spaceship.mp3")
        )
        self.spaceship_sound_length = int(self.spaceship_sound.get_length())

        self.enemy_sound = pygame.mixer.Sound(
            os.path.join(ruta_actual, "../Static/Sounds/lightsaber.wav")
        )
        self.enemy_sound_length = int(self.enemy_sound.get_length())

    def end_game(self):
        """
        Finaliza el juego y cierra la ventana de juego.
        """
        pygame.quit()
        sys.exit()

    def draw_board(self):
        """
        Ejecuta la animación del juego, según el camino encontrado por el algoritmo previamente ejecutado.
        """
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

                    elif self.map[row][col] == "6":  # Victoria: Mandalorian y Grogu
                        self.window.blit(
                            self.mandalorian_grogu_icon,
                            (
                                col * self.rectangle_width
                                + self.left_margin
                                + self.mandalorian_grogu_icon_offset_x,
                                row * self.rectangle_height
                                + self.top_margin
                                + self.mandalorian_grogu_icon_offset_y,
                            ),
                        )

    def print_stats(self, nodes_expanded, tree_depth, time_elapsed, cost):
        """
        Despliega las estadísticas del algoritmo en la ventana de juego.
        """
        self.title = self.font_title_1.render("Smart Mandalorian", True, (0, 0, 0))

        self.stats_title = self.font_title_2.render(
            "Estadísticas del algoritmo", True, (0, 0, 0)
        )

        self.nodes_expanded = self.font_subtitle.render(
            "Nodos expandidos: ", True, (0, 0, 0)
        )
        self.nodes_expanded_value = self.font_body.render(
            str(nodes_expanded), True, (0, 0, 0)
        )

        self.tree_depth = self.font_subtitle.render(
            "Profundidad del árbol: ", True, (0, 0, 0)
        )
        self.tree_depth_value = self.font_body.render(str(tree_depth), True, (0, 0, 0))

        self.time_elapsed = self.font_subtitle.render(
            "Tiempo de ejecución (s): ", True, (0, 0, 0)
        )
        self.time_elapsed_value = self.font_body.render(
            str(time_elapsed), True, (0, 0, 0)
        )

        self.cost = self.font_subtitle.render("Costo de la solución: ", True, (0, 0, 0))
        self.cost_value = self.font_body.render(str(cost), True, (0, 0, 0))

        self.window.blit(
            self.title,
            (
                self.width * 0.5 - self.title.get_width() // 2,
                self.top_margin * 0.3,
            ),
        )

        self.window.blit(
            self.stats_title,
            (
                self.width * 0.5 - self.stats_title.get_width() // 2,
                self.height - self.bottom_margin * 0.95,
            ),
        )

        self.window.blit(
            self.nodes_expanded,
            (
                self.width * 0.5 - self.nodes_expanded.get_width() // 2,
                self.height - self.bottom_margin * 0.7,
            ),
        )

        self.window.blit(
            self.nodes_expanded_value,
            (
                self.width * 0.5 + self.nodes_expanded.get_width() // 2,
                self.height - self.bottom_margin * 0.7,
            ),
        )

        self.window.blit(
            self.tree_depth,
            (
                self.width * 0.5 - self.tree_depth.get_width() // 2,
                self.height - self.bottom_margin * 0.5,
            ),
        )

        self.window.blit(
            self.tree_depth_value,
            (
                self.width * 0.5 + self.tree_depth.get_width() // 2,
                self.height - self.bottom_margin * 0.5,
            ),
        )

        self.window.blit(
            self.time_elapsed,
            (
                self.width * 0.5 - self.time_elapsed.get_width() // 2,
                self.height - self.bottom_margin * 0.3,
            ),
        )

        self.window.blit(
            self.time_elapsed_value,
            (
                self.width * 0.5 + self.time_elapsed.get_width() // 2,
                self.height - self.bottom_margin * 0.3,
            ),
        )

        self.window.blit(
            self.cost,
            (
                self.width * 0.5 - self.cost.get_width() // 2,
                self.height - self.bottom_margin * 0.1,
            ),
        )

        self.window.blit(
            self.cost_value,
            (
                self.width * 0.5 + self.cost.get_width() // 2,
                self.height - self.bottom_margin * 0.1,
            ),
        )

    def display_environment(self, expanded_nodes, tree_depth, time_elapsed, cost, path):
        """
        Controlador general de la ventana de juego.
        Despliega la interfaz inicial y después ejecuta la animación del juego, según el camino encontrado por el algoritmo previamente seleccionado y ejecutado.
        """
        self.agent.update_path_to_follow(path)
        index = 0
        found_spaceship = False
        found_enemy = False

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                self.end_game()

            # Dibuja el tablero y las estadísticas del algoritmo
            self.draw_board()
            self.print_stats(expanded_nodes, tree_depth, time_elapsed, cost)

            # Verifica si el agente ha llegado a la meta
            if index == len(path) - 1:
                self.agent.update_current_icon(self.mandalorian_grogu_icon)
                self.agent.draw(self.window)
                pygame.display.flip()
                self.win_sound.play()

                # Espera a que el usuario cierre la ventana
                while True:
                    event = pygame.event.poll()
                    if event.type == pygame.QUIT:
                        self.end_game()

            # Actualiza la posición del agente en el tablero
            (index, found_spaceship, found_enemy) = self.agent.update_position(
                self.map, index
            )
            self.agent.draw(self.window)

            # Verifica si el agente ha encontrado la nave
            if found_spaceship:
                self.spaceship_sound.play()
                pygame.time.wait(self.spaceship_sound_length * 1000)
                self.map[self.agent.y][self.agent.x] = "0"

            # Verifica si el agente ha encontrado al enemigo
            if found_enemy:
                self.enemy_sound.play()
                pygame.time.wait(self.enemy_sound_length * 1000)

            # Actualiza el contenido de la ventana
            pygame.display.flip()
            pygame.time.wait(4)
