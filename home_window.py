# Importar librerías
import sys
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QLabel)
from PyQt6.QtGui import (QIcon, QPixmap, QFont)
from comics_window import ComicsWindow
from characters_window import CharactersWindow

app = QApplication(sys.argv)


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.test_characters = CharactersWindow()
        self.test_comics = ComicsWindow()

        self.layout = QVBoxLayout()
        # self.buttons_layout = QHBoxLayout

        # Crear la ventana de inicio
        self.setWindowTitle('INICIO')
        self.setWindowIcon(QIcon('logo.jpg'))

        # Poner una imagen de fondo
        self.image1 = QPixmap('wallpaper1.jpg')
        self.image_label1 = QLabel()
        self.image_label1.setPixmap(self.image1)

        self.image2 = QPixmap('wallpaper2.jpg')
        self.image_label2 = QLabel()
        self.image_label2.setPixmap(self.image2)

        # Crear botones
        self.comics_section = QPushButton('VER CÓMICS', self)
        self.comics_section.setFont(QFont('Bahnschrift Condensed', 15))  # Cambiar tipografía y tamaño de la letra
        self.comics_section.setStyleSheet('Background-color: #FF030C')  # Color de fondo
        self.comics_section.setGeometry(9, 0, 300, 30)  # Dimensiones del botón
        self.comics_section.clicked.connect(self.goto_comics_section)  # Acción al click

        self.characters_section = QPushButton('VER PERSONAJES', self)
        self.characters_section.setFont(QFont('Bahnschrift Condensed', 15))  # Cambiar tipografía y tamaño de la letra
        self.characters_section.setStyleSheet('Background-color: #FF030C')  # Color de fondo
        self.characters_section.setGeometry(309, 0, 300, 30)  # Dimensiones del botón
        self.characters_section.clicked.connect(self.goto_characters_section)  # Acción al click

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.comics_section)
        self.buttons_layout.addWidget(self.characters_section)

        self.layout.addWidget(self.image_label1)
        self.layout.addLayout(self.buttons_layout)
        self.layout.addWidget(self.image_label2)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def goto_comics_section(self):
        self.test_comics.load_ui()

    def goto_characters_section(self):
        self.test_characters.load_ui()
