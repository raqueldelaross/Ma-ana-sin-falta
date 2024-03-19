from PyQt6.QtWidgets import QWidget, QLabel,  QPushButton, QVBoxLayout, QMainWindow, QTextEdit, QListWidget
from PyQt6.QtGui import QPixmap, QFont
import requests
from character import Character


class CharacterDetailWidget(QMainWindow):
    def __init__(self, character: Character):
        super().__init__()
        layout = QVBoxLayout()
        image = requests.get(character.image)

        self.name = QLabel(character.character_name)
        self.name.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.name)

        self.image = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(image.content)
        self.image.setPixmap(pixmap)
        scaled_pixmap = pixmap.scaled(150, 150)
        self.image.setPixmap(scaled_pixmap)

        layout.addWidget(self.image)

        self.des = QLabel('DESCRIPCIÓN')
        self.des.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.des)

        self.description = QTextEdit()
        self.description.setPlainText(character.description)
        self.description.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.description.setEnabled(False)
        layout.addWidget(self.description)

        self.comic_title = QLabel('COMICS EN LOS QUE HA PARTICIPADO')
        self.comic_title.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.comic_title)
        self.comic = QListWidget()
        self.comic.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.comic.addItems(character.comic)
        layout.addWidget(self.comic)

        self.serie_title = QLabel('SERIES EN LOS QUE HA PARTICIPADO')
        self.serie_title.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.serie_title)

        self.serie = QListWidget()
        self.serie.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.serie.addItems(character.serie)
        layout.addWidget(self.serie)

        self.info_widget = QWidget()
        self.info_widget.setLayout(layout)
        self.setCentralWidget(self.info_widget)
