import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import Novajanela


def main():
    app = QApplication(sys.argv)  # Inicializa a app Qt
    window =Novajanela()         # Cria a janela principal
    window.show()                 # Mostra a interface
    sys.exit(app.exec())          # Corre o loop do Qt

if __name__ == "__main__":
    main()
