from PyQt6.QtWidgets import QWidget, QLabel,  QPushButton, QVBoxLayout, QMainWindow, QTextEdit, QListWidget
from PyQt6.QtGui import QPixmap, QFont
import requests
from comic import Comic


class ComicsDetailWidget(QMainWindow):
    def __init__(self, comic: Comic):
        super().__init__()
        layout = QVBoxLayout()
        image = requests.get(comic.image)

        self.title = QLabel(comic.comic_title)
        self.title.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.title)

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
        self.description.setPlainText(comic.description)
        self.description.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.description.setEnabled(False)
        layout.addWidget(self.description)

        self.comic_title = QLabel('PERSONAJES QUE APARECEN ')
        self.comic_title.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.comic_title)
        self.comic = QListWidget()
        self.comic.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.comic.addItems(comic.characters)
        layout.addWidget(self.comic)

        self.creators = QLabel('CREADORES DEL COMIC ')
        self.creators.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        layout.addWidget(self.creators)
        self.list_creators = QListWidget()
        self.list_creators.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.list_creators.addItems(comic.creators)
        layout.addWidget(self.list_creators)

        self.info_widget = QWidget()
        self.info_widget.setLayout(layout)
        self.setCentralWidget(self.info_widget)
