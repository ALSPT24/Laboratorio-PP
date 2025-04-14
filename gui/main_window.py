from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon, QCursor
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Park Out")
        self.setFixedSize(600, 900)
        self.setWindowIcon(QIcon("imagens/icon.png"))

        # background
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("imagens/main.png"))
        self.background.setGeometry(0, 0, 600, 900)
        self.background.setScaledContents(True)

        # botao play
        self.play_button = QPushButton(self)
        self.play_button.setIcon(QIcon("imagens/botao_play.png"))
        self.play_button.setIconSize(QSize(500, 500))
        self.play_button.setGeometry(5, 700, 600, 200)
        self.play_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.play_button.setStyleSheet("border: none;")
        self.play_button.clicked.connect(self.abrir_janela_principal)

    def abrir_janela_principal(self):
        self.novajanela = Novajanela()
        self.novajanela.show()
        self.close()

class Novajanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Park Out")
        self.setFixedSize(600, 900)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("imagens/principal.png"))
        self.background.setGeometry(0, 0, 600, 900)
        self.background.setScaledContents(True)


        