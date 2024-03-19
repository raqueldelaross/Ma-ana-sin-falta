from PyQt6.QtWidgets import QWidget, QLabel,  QPushButton, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap, QFont
import requests
import sys
from character import Character
from character_detail_window import CharacterDetailWidget

app = QApplication(sys.argv)


class CharacterWidget(QWidget):
    def __init__(self, character: Character):
        super().__init__()
        self.character_detail = character
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

        self.button = QPushButton('DETALLES')
        self.button.setFont(QFont('Bahnschrift Light SemiCondensed', 12))
        self.button.setStyleSheet('Background-color: #FF030C')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.view_detail)

        self.setLayout(layout)

    def view_detail(self):
        self.detail = CharacterDetailWidget(self.character_detail)
        self.detail.show()
        app.exec()
