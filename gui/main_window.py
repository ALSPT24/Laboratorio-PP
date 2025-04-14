from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Park Out")
        self.setFixedSize(600, 800)
        self.setWindowIcon(QIcon("imagens/icon.png"))

        # Carrega e exibe a imagem
        self.image_label = QLabel(self)
        pixmap = QPixmap("imagens/principal.png")  # Caminho da tua imagem
        self.image_label.setPixmap(pixmap)
        self.image_label.resize(pixmap.width(), pixmap.height())
