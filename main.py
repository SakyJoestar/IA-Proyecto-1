from Models import *

from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ui = UI()
    ui.show()
    sys.exit(app.exec_()) 
