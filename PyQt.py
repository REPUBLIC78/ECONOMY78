from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon

import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Название программы')
    window.setWindowIcon(QIcon(''))
    window.setGeometry(300, 250, 350, 200)

    button = QPushButton("Click!")
    button.setFixedSize(128, 32)
    window.setCentralWidget(button)

    window.show()
    sys.exit(app.exec())


application()