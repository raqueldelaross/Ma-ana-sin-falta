# Importar librerías
import sys
import time
import hashlib
import requests
from comic import Comic
from list_comic_widget import ListComicWidget
from PyQt6.QtGui import (QIcon, QFont)
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QWidget,
                             QMessageBox, QLineEdit, QApplication)
from comics_detail_window import ComicsDetailWidget

# Claves de acceso y enlace a la api
public_key = '019d806bc3274b523fa0e428d9c8b19b'
private_key = 'a4ed29bd3586633d05e1df3295863eaad7c5cb4a'
endpoint = 'https://gateway.marvel.com/v1/public/comics'

app = QApplication(sys.argv)


def get_comics(offset):
    ts = str(time.time())
    hash_value = hashlib.md5((ts + private_key + public_key).encode('utf-8')).hexdigest()
    params = {
        'ts': ts,
        'apikey': public_key,
        'hash': hash_value,
        'limit': 10,
        'offset': offset,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data['data']['results'], data['data']['total']


def get_list(offset):
    comics_list: list[Comic] = []
    items, total = get_comics(offset)
    for item in items:
        creators = []
        characters = []
        title = item['title']
        image = item['thumbnail']['path'] + '.' + item['thumbnail']['extension']
        description = item['description']
        creator = item['creators']['items']
        character = item['characters']['items']
        for i in creator:
            creators.append(i['name'])
        for i in character:
            characters.append(i['name'])
        comic = Comic(
            title,
            image,
            description,
            creators,
            characters
        )
        comics_list.append(comic)
    return comics_list


class ComicsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.comic_detail = Comic
        self.create_widget()

    def create_widget(self):
        # Layouts que se utilizarán
        self.layout1 = QVBoxLayout()  # para los datos del encabezado
        self.layout2 = QHBoxLayout()  # para los botones de navegación
        self.headers_layout = QHBoxLayout()

        # Configuración de ventana
        self.setWindowTitle("CÓMICS DE MARVEL")
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
        self.search_button.clicked.connect(self.get_search_comic)

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
        comics = get_list(self.contador)
        list_widget = ListComicWidget(comics)
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
            mesage_box.setText('No existen comics anteriores a los mostrados')
            mesage_box.show()
            mesage_box.exec()

    def update_grid(self):
        comics = get_list(self.contador)
        list_widget = ListComicWidget(comics)
        for widget in list_widget.grid_items:
            widget.setParent(None)
            widget.deleteLater()
        list_widget.grid_items.clear()
        list_widget = ListComicWidget(comics)
        self.create_widget()
        self.layout1.addWidget(list_widget)

    def get_search_comic(self):
        name = self.textbox.text()
        results = get_comics(name)

        if len(results) == 0:
            mesage_box = QMessageBox()
            mesage_box.setIcon(QMessageBox.Icon.Warning)
            mesage_box.setWindowTitle('Advertencia')
            mesage_box.setText('No existen comics anteriores a los mostrados')
            mesage_box.show()
            mesage_box.exec()
        else:
            comics = results[0]
            name = comics['title']
            description = comics['description']
            imagen = comics['thumbnail']['path'] + '.' + comics['thumbnail']['extension']
            creators = [comic['name'] for comic in comics['creators']['items']]
            characters = [serie['name'] for serie in comics['characters']['items']]

            cara = Comic(name, imagen, description, creators, characters)

            self.data_search = ComicsDetailWidget(cara)
            self.data_search.show()
            app.exec()
