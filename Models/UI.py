import os
from Algorithms import *
from Models import *

from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QRadioButton,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QDesktopWidget,
)
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

current_path = os.path.dirname(__file__)
icon = os.path.join(current_path, "../Static/Grogu.png")
font_title_path = os.path.join(current_path, "../Static/Fonts/Starjedi.ttf")
font_title_2_path = os.path.join(current_path, "../Static/Fonts/Roboto-Bold.ttf")
font_subtitle_path = os.path.join(current_path, "../Static/Fonts/Roboto-Regular.ttf")
font_body_path = os.path.join(current_path, "../Static/Fonts/Roboto-Thin.ttf")
main_theme = os.path.join(current_path, "../Static/Sounds/main_theme.mp3")


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_dir = None

        self.setWindowTitle("Smart Mandalorian")
        self.setWindowIcon(QIcon(icon))
        self.setGeometry(100, 100, 600, 400)

        screen = QDesktopWidget().screenGeometry()
        self.move(
            (screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2
        )

        font_title = self.load_font(font_title_path, 32)
        font_subtitle = self.load_font(font_subtitle_path, 14)
        font_body = self.load_font(font_body_path, 12)
        font_start = self.load_font(font_title_path, 12)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: #A5C9CA;")

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Smart Mandalorian")
        self.title_label.setFont(font_title)
        self.layout.addWidget(self.title_label)

        self.algorithm_label = QLabel("Select an Algorithm:")
        self.algorithm_label.setFont(font_subtitle)
        self.layout.addWidget(self.algorithm_label)

        self.algorithm_buttons = []
        self.algorithms = ["Amplitud", "Costo", "Profundidad", "Avaro", "A*"]
        for algo in self.algorithms:
            radio_button = QRadioButton(algo)
            radio_button.setFont(font_body)
            self.algorithm_buttons.append(radio_button)
            self.layout.addWidget(radio_button)

        self.algorithm_buttons[0].setChecked(True)

        self.layout.setAlignment(Qt.AlignCenter)

        self.file_label = QLabel("Select a File:")
        self.file_label.setFont(font_subtitle)
        self.layout.addWidget(self.file_label)

        self.file_selector_button = QPushButton("Select File")
        self.file_selector_button.setFont(font_body)
        self.file_selector_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_selector_button)

        self.start_button = QPushButton("Start")
        self.start_button.setFont(font_start)
        self.start_button.clicked.connect(self.start_game)
        self.start_button.setEnabled(False)
        self.layout.addWidget(self.start_button)

        self.central_widget.setLayout(self.layout)

        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(main_theme)))
        self.player.play()


    def load_font(self, font_path: str, font_size: int):
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, font_size, QFont.Normal)
            return font
        return None

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select File", "", "All Files (*)"
        )
        if (
            file_path
            and file_path.endswith(".txt")
            and any(algo.isChecked() for algo in self.algorithm_buttons)
        ):
            self.start_button.setEnabled(True)
            self.file_dir = file_path
            filename = os.path.basename(file_path)
            self.file_label.setText(f"Selected File: {filename}")

    def select_algorithm(self):
        selected_algorithm = None
        for i, radio_button in enumerate(self.algorithm_buttons):
            if radio_button.isChecked():
                selected_algorithm = self.algorithms[i]

        if selected_algorithm == "Amplitud":
            return execute_breadth_search(self.file_dir)
        elif selected_algorithm == "Costo":
            return execute_cost_search(self.file_dir)
        elif selected_algorithm == "Profundidad":
            return execute_depth_search(self.file_dir)
        elif selected_algorithm == "Avaro":
            return execute_greedy_search(self.file_dir)
        elif selected_algorithm == "A*":
            return execute_astar_search(self.file_dir)

    def start_game(self):

        print("Starting game...")
        self.player.stop()
        self.close()

        expanded_nodes, depth, total_time, cost, path = self.select_algorithm()

        map = Reader.read_map(self.file_dir)

        (y, x) = Agent.find_agent(map)
        agent = Agent(y, x)

        env = Environment(650, 750, map, agent)
        env.display_environment(expanded_nodes, depth, round(total_time, 6), cost, path)
