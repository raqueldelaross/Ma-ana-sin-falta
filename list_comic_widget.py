from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from comic_widget import ComicsWidget
from comic import Comic


class ListComicWidget(QWidget):
    def __init__(self, comic: list[Comic]):
        super().__init__()
        self.grid_items = []
        grid_layout = QGridLayout()
        for i, comic in enumerate(comic):
            widget = ComicsWidget(comic)
            # Calculamos la posición del QLabel en el QGridLayout
            fila = i // 5
            columna = i % 5
            # Agregamos el QLabel al QGridLayout
            grid_layout.addWidget(widget, fila, columna)
            self.grid_items.append(widget)

        self.setLayout(grid_layout)
