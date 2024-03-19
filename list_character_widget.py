from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from character_widget import CharacterWidget
from character import Character


class ListCharacterWidget(QWidget):
    def __init__(self, characters: list[Character]):
        super().__init__()
        self.grid_items = []
        grid_layout = QGridLayout()
        for i, character in enumerate(characters):
            widget = CharacterWidget(character)
            # Calculamos la posición del QLabel en el QGridLayout
            fila = i // 5
            columna = i % 5
            # Agregamos el QLabel al QGridLayout
            grid_layout.addWidget(widget, fila, columna)
            self.grid_items.append(widget)

        self.setLayout(grid_layout)
