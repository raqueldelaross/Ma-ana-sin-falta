# importar librerías
import sys
from home_window import HomeWindow
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)  # Crear la aplicación
home_window = HomeWindow()  # Crear variable de la ventana inicial


# Cargar ventana principal
def load_window():
    home_window.show()


# Inicio de la aplicación
def main():
    home_window.hide()
    load_window()

    app.exec()


main()  # Iniciar la aplicación
