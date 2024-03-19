import time
import hashlib
import requests
import sys
from character import Character
from PyQt6.QtGui import (QIcon, QFont)
from list_character_widget import ListCharacterWidget
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QWidget,
                             QMessageBox, QLineEdit, QApplication)
from character_detail_window import CharacterDetailWidget

from api import get_character, get_characters

app = QApplication(sys.argv)

def get_list(offset):
    characters_list: list[Character] = []
    items, total = get_characters(offset)
    for item in items:
        comics = []
        series = []
        name = item['name']
        image = item['thumbnail']['path'] + '.' + item['thumbnail']['extension']
        description = item['description']
        comic = item['comics']['items']
        for i in comic:
            comics.append(i['name'])
        serie = item['series']['items']
        for i in serie:
            series.append(i['name'])
        character = Character(
            name,
            image,
            description,
            comics,
            series
        )
        characters_list.append(character)
    return characters_list


class CharactersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.character_detail = Character
        self.create_widget()

    def create_widget(self):
        # Layouts que se utilizarán
        self.layout1 = QVBoxLayout()  # para los datos del encabezado
        self.layout2 = QHBoxLayout()  # para los botones de navegación
        self.headers_layout = QHBoxLayout()

        # Configuración de ventana
        self.setWindowTitle("PERSONAJES DE MARVEL")
        self.setWindowIcon(QIcon('logo.jpg'))

        self.orden_combo = QComboBox(self)
        self.orden_combo.setFont(QFont('Bahnschrift Light SemiCondensed', 10))
        self.orden_combo.addItem("POR ORDEN DE NOMBRE ASCENDENTE")
        self.orden_combo.addItem("POR ORDEN DE NOMBRE DESCENDENTE")
        self.orden_combo.addItem("POR ORDEN DE CREADOR ASCENDENTE")
        self.orden_combo.addItem("POR ORDEN DE CREADOR DESCENDENTE  ")

        # Crear el buscador
        self.textbox = QLineEdit(self)

        self.search_button = QPushButton('BUSCAR')
        self.search_button.setFont(QFont('Bahnschrift Light SemiCondensed', 12))
        self.search_button.setStyleSheet('Background-color: #FF030C')  # Color de fondo
        self.search_button.clicked.connect(self.get_search_caracter)

        self.previus_button = QPushButton('ANTERIOR')
        self.previus_button.setFont(QFont('Bahnschrift Light SemiCondensed', 12))
        self.previus_button.setStyleSheet('Background-color: #FF030C')  # Color de fondo
        self.previus_button.clicked.connect(self.prev_page)

        self.headers_layout.addWidget(self.orden_combo)
        self.headers_layout.addWidget(self.textbox)
        self.headers_layout.addWidget(self.search_button)

        self.layout1.addLayout(self.headers_layout)

        self.next_button = QPushButton('SIGUIENTE')
        self.next_button.setFont(QFont('Bahnschrift Light SemiCondensed', 12))
        self.next_button.setStyleSheet('Background-color: #FF030C')  # Color de fondo
        self.next_button.clicked.connect(self.next_page)

        self.layout2.addWidget(self.previus_button)
        self.layout2.addWidget(self.next_button)

        button_info = QWidget()
        button_info.setLayout(self.layout2)

        self.layout1.addWidget(button_info)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout1)

        self.setCentralWidget(self.main_widget)

    def load_ui(self):
        characters = get_list(self.contador)
        list_widget = ListCharacterWidget(characters)
        self.layout1.addWidget(list_widget)
        self.show()

    def next_page(self):
        self.contador += 10
        self.update_grid()

    def prev_page(self):
        if self.contador > 0:
            self.contador -= 10
            self.update_grid()
        else:
            mesage_box = QMessageBox()
            mesage_box.setIcon(QMessageBox.Icon.Warning)
            mesage_box.setWindowTitle('Advertencia')
            mesage_box.setText('No existen personajes anteriores a los mostrados')
            mesage_box.show()
            mesage_box.exec()

    def update_grid(self):
        characters = get_list(self.contador)
        list_widget = ListCharacterWidget(characters)
        for widget in list_widget.grid_items:
            widget.setParent(None)
            widget.deleteLater()
        list_widget.grid_items.clear()
        list_widget = ListCharacterWidget(characters)
        self.create_widget()
        self.layout1.addWidget(list_widget)

    def get_search_caracter(self):
        name = self.textbox.text()
        results = get_character(name)

        if len(results) == 0:
            mesage_box = QMessageBox()
            mesage_box.setIcon(QMessageBox.Icon.Warning)
            mesage_box.setWindowTitle('Advertencia')
            mesage_box.setText('No existen personajes anteriores a los mostrados')
            mesage_box.show()
            mesage_box.exec()
        else:
            character = results[0]
            name = character['name']
            description = character['description']
            imagen = character['thumbnail']['path'] + '.' + character['thumbnail']['extension']
            comics = [comic['name'] for comic in character['comics']['items']]
            series = [serie['name'] for serie in character['series']['items']]

            cara = Character(name, imagen, description, comics, series)

            self.data_search = CharacterDetailWidget(cara)
            self.data_search.show()
            app.exec()
