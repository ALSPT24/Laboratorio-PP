import os
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QPoint

# Pastas dos carros e as cores associadas (mesma ordem)
IMAGE_FOLDERS = [
    ("imagens/autocarros/autocarrosamarelos", "amarelo"),
    ("imagens/autocarros/autocarrosazuis", "azul"),
    ("imagens/autocarros/autocarrosverdes", "verde"),
    ("imagens/autocarros/autocarrosvermelhos", "vermelho"),
]

# Pastas das pessoas e cores
PEOPLE_FOLDERS = [
    ("imagens/pessoas/amarelo", "amarelo"),
    ("imagens/pessoas/azul", "azul"),
    ("imagens/pessoas/verde", "verde"),
    ("imagens/pessoas/vermelho", "vermelho"),
]


class CarroWidget(QLabel):
    def __init__(self, imagem_path, cor, mover_callback, capacidade, parent=None):
        super().__init__(parent)
        self.capacidade = capacidade
        self.ocupacao_atual = 0
        self.imagem_path = imagem_path
        self.cor_carro = cor.lower().strip()
        self.mover_callback = mover_callback
        self.direcao = random.choice(["up", "down", "left", "right"])  # Direção fixa

        self.setFixedSize(70, 70)
        self.setStyleSheet("background: transparent; border: none;")

        # Imagem do carro
        pixmap = QPixmap(imagem_path)
        if not pixmap.isNull():
            self.setPixmap(pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.setText("Erro imagem")

        # Label de ocupação sobreposta
        self.ocupacao_label = QLabel(f"{self.ocupacao_atual}/{self.capacidade}", self)
        self.ocupacao_label.setStyleSheet("color: black; font-size: 10px; background-color: rgba(255,255,255,150);")
        self.ocupacao_label.move(2, 50)
        self.ocupacao_label.resize(60, 15)
        self.ocupacao_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ocupacao_label.hide()

    def mousePressEvent(self, event):
        self.mover_callback(self)

    def atualizar_ocupacao(self):
        self.ocupacao_label.setText(f"{self.ocupacao_atual}/{self.capacidade}")


class PessoaWidget(QLabel):
    def __init__(self, imagem_path, cor, parent=None):
        super().__init__(parent)
        self.imagem_path = imagem_path
        self.cor = cor.lower().strip()
        self.setFixedSize(100, 100)
        self.setStyleSheet("background: transparent; border: none;")

        pixmap = QPixmap(imagem_path)
        if not pixmap.isNull():
            self.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.setText("Erro imagem")


class Novajanela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Park Out")
        self.setWindowIcon(QIcon("imagens/icon.png"))
        self.setFixedSize(600, 800)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.numero_aleatorio = random.randint(80, 120)
        print(f"Número inicial aleatório: {self.numero_aleatorio}")

        bg_path = "imagens/principal.png"
        if os.path.exists(bg_path):
            self.central_widget.setStyleSheet(f"QWidget {{ background-image: url({bg_path}); background-repeat: no-repeat; background-position: center; background-size: cover; }}")
        else:
            self.central_widget.setStyleSheet("QWidget { background-color: #cccccc; }")

        self.vagas_disponiveis = [(50, 150), (140, 150), (230, 150), (320, 150), (400, 150), (490, 150)]
        self.ocupadas = {}

        self.num_rows = 5
        self.num_cols = 5
        self.total_slots = self.num_rows * self.num_cols

        self.images_by_folder = [self.load_images_from_folder(folder) for folder, _ in IMAGE_FOLDERS]
        colors = [cor for _, cor in IMAGE_FOLDERS]
        self.image_paths_com_cores = self.prepare_balanced_images_with_colors(self.images_by_folder, colors, self.total_slots)

        self.create_carros_grid()
        self.people_images_colored = self.load_people_with_colors()

        self.fila_reserva = []
        while len(self.fila_reserva) < self.numero_aleatorio:
            faltam = self.numero_aleatorio - len(self.fila_reserva)
            if faltam >= len(self.people_images_colored):
                self.fila_reserva.extend(self.people_images_colored)
            else:
                self.fila_reserva.extend(random.sample(self.people_images_colored, faltam))

        self.fila_visivel = []
        self.max_pessoas_fila = 7

        self.numero_label = QLabel(f"{self.numero_aleatorio}", self.central_widget)
        self.numero_label.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
        self.numero_label.adjustSize()
        self.numero_label.move(50, 50)

        #Botao Restart
        self.restart_button = QPushButton("Restart", self.central_widget)
        self.restart_button.setStyleSheet("font-size: 16px; padding: 6px;")
        self.restart_button.move(500, 350)
        self.restart_button.clicked.connect(self.reiniciar_jogo)
        self.restart_button.show()

        self.create_fila_linear()

        self.timer = QTimer()
        self.timer.timeout.connect(self.tentar_entrar_pessoa)
        self.timer.start(1000)

    def reiniciar_jogo(self):
        # Parar timer
        self.timer.stop()

        # Remover carros
        for carro in self.carros_widgets:
            carro.hide()
            carro.deleteLater()
        self.carros_widgets.clear()
        self.ocupadas.clear()

        # Remover fila
        for pessoa in self.fila_visivel:
            pessoa.hide()
            pessoa.deleteLater()
        self.fila_visivel.clear()
        self.fila_reserva.clear()

        # Regerar número aleatório
        self.numero_aleatorio = random.randint(80, 120)
        self.numero_label.setText(str(self.numero_aleatorio))
        self.numero_label.adjustSize()

        # Recarregar imagens e recriar tudo
        self.image_paths_com_cores = self.prepare_balanced_images_with_colors(
            self.images_by_folder,
            [cor for _, cor in IMAGE_FOLDERS],
            self.total_slots
        )
        self.create_carros_grid()

        self.people_images_colored = self.load_people_with_colors()
        while len(self.fila_reserva) < self.numero_aleatorio:
            faltam = self.numero_aleatorio - len(self.fila_reserva)
            if faltam >= len(self.people_images_colored):
                self.fila_reserva.extend(self.people_images_colored)
            else:
                self.fila_reserva.extend(random.sample(self.people_images_colored, faltam))

        self.create_fila_linear()
        self.timer.start(1000)

    def load_images_from_folder(self, folder_path):
        all_image_paths = []
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    filepath = os.path.join(folder_path, filename)
                    all_image_paths.append(filepath)
        return all_image_paths

    def prepare_balanced_images_with_colors(self, images_by_folder, colors, total_slots):
        balanced = []
        n_folders = len(images_by_folder)
        slots_per_folder = total_slots // n_folders
        extra = total_slots % n_folders

        for i, (images, cor) in enumerate(zip(images_by_folder, colors)):
            if images:
                count = slots_per_folder + (1 if i < extra else 0)
                chosen = []
                while len(chosen) < count:
                    chosen.extend(random.sample(images, min(count - len(chosen), len(images))))
                balanced.extend([(img, cor) for img in chosen])
        random.shuffle(balanced)
        return balanced

    def load_people_with_colors(self):
        pessoas = []
        for folder, cor in PEOPLE_FOLDERS:
            imagens = self.load_images_from_folder(folder)
            for img in imagens:
                pessoas.append((img, cor))
        if not pessoas:
            pessoas.append(("imagens/default_person.png", "amarelo"))
        return pessoas

    def create_carros_grid(self):
        start_x = 150
        start_y = 400
        spacing_x = 70
        spacing_y = 70

        self.carros_widgets = []
        capacidades_possiveis = [4, 6, 8, 12]

        for index in range(min(len(self.image_paths_com_cores), self.total_slots)):
            imagem_path, cor = self.image_paths_com_cores[index]
            capacidade = random.choice(capacidades_possiveis)
            carro = CarroWidget(imagem_path, cor, self.mover_carro_para_vaga, capacidade, parent=self.central_widget)
            row = index // self.num_cols
            col = index % self.num_cols
            carro.move(start_x + col * spacing_x, start_y + row * spacing_y)
            carro.show()
            self.carros_widgets.append(carro)

    def create_fila_linear(self):
        for pessoa in self.fila_visivel:
            pessoa.hide()
            pessoa.deleteLater()
        self.fila_visivel.clear()

        self.fila_start_x = 150
        self.fila_start_y = 25
        self.fila_spacing_x = 60

        for i in range(min(self.max_pessoas_fila, len(self.fila_reserva))):
            imagem_path, cor = self.fila_reserva.pop(0)
            pessoa = PessoaWidget(imagem_path, cor, parent=self.central_widget)
            pessoa.move(self.fila_start_x + i * self.fila_spacing_x, self.fila_start_y)
            pessoa.show()
            self.fila_visivel.append(pessoa)

    def mover_carro_para_vaga(self, carro_widget):
        vaga_livre = next((vaga for vaga in self.vagas_disponiveis if vaga not in self.ocupadas), None)
        if vaga_livre is None:
            print("Sem vagas livres para o carro.")
            return

        vaga_antiga = next((coord for coord, carro in self.ocupadas.items() if carro == carro_widget), None)
        if vaga_antiga is not None:
            del self.ocupadas[vaga_antiga]

        animation = QPropertyAnimation(carro_widget, b"pos", self)
        animation.setDuration(500)
        animation.setStartValue(carro_widget.pos())
        animation.setEndValue(QPoint(*vaga_livre))
        animation.start()
        carro_widget.animation = animation  # Referência evita que o GC cancele
        carro_widget.ocupacao_label.show()
        self.ocupadas[vaga_livre] = carro_widget

    def tentar_entrar_pessoa(self):
        if not self.fila_visivel:
            return

        primeira_pessoa = self.fila_visivel[0]
        cor_pessoa = primeira_pessoa.cor

        carro_encontrado = next((carro for carro in self.ocupadas.values()
                                 if carro.cor_carro == cor_pessoa and carro.ocupacao_atual < carro.capacidade), None)

        if carro_encontrado is None:
            return

        self.fila_visivel.pop(0)
        primeira_pessoa.hide()
        primeira_pessoa.deleteLater()

        carro_encontrado.ocupacao_atual += 1
        carro_encontrado.atualizar_ocupacao()

        self.numero_aleatorio = max(0, self.numero_aleatorio - 1)
        self.numero_label.setText(str(self.numero_aleatorio))
        self.numero_label.adjustSize()

        while len(self.fila_visivel) < self.max_pessoas_fila and self.fila_reserva:
            imagem_path, cor = self.fila_reserva.pop(0)
            nova_pessoa = PessoaWidget(imagem_path, cor, parent=self.central_widget)
            nova_pessoa.move(self.fila_start_x + len(self.fila_visivel) * self.fila_spacing_x, self.fila_start_y)
            nova_pessoa.show()
            self.fila_visivel.append(nova_pessoa)

        for i, pessoa in enumerate(self.fila_visivel):
            pessoa.move(self.fila_start_x + i * self.fila_spacing_x, self.fila_start_y)

        if carro_encontrado.ocupacao_atual >= carro_encontrado.capacidade:
            vaga_remover = next((coord for coord, carro in self.ocupadas.items() if carro == carro_encontrado), None)
            if vaga_remover is not None:
                del self.ocupadas[vaga_remover]

            carro_encontrado.hide()
            carro_encontrado.ocupacao_label.hide()
            carro_encontrado.deleteLater()
            if carro_encontrado in self.carros_widgets:
                self.carros_widgets.remove(carro_encontrado)

        if self.numero_aleatorio == 0:
            print("Todas as pessoas entraram no carro!")

