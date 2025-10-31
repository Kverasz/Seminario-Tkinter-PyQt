import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor

# emoji
class GhostLabel(QLabel):
    def __init__(self, text, lifespan_ms, parent=None):
        super().__init__(text, parent)
        self.lifespan_ms = lifespan_ms
        self.setFont(QFont("Segoe UI Emoji", 36))
        self.setStyleSheet("color: white; background: transparent;")
        self.adjustSize()


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎃 Caça-Fantasma — Winx Seminario 👻")
        self.setFixedSize(600, 400)

        # fundo preto 
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(10, 10, 10))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # variáveis do jogo
        self.score = 0
        self.time_left = 30
        self.active_ghosts = []

        # elementos da interface
        self.score_label = QLabel(f"Pontos: {self.score}")
        self.time_label = QLabel(f"Tempo: {self.time_left}s")
        self.start_button = QPushButton("Iniciar")

        # estilo dos textos e botão
        for lbl in (self.score_label, self.time_label):
            lbl.setStyleSheet("color: orange; font-size: 18px; font-weight: bold;")
        self.start_button.setStyleSheet(
            "background-color: purple; color: white; font-weight: bold; padding: 8px 16px; border-radius: 10px;"
        )

        # layout superior
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.score_label)
        top_layout.addStretch()
        top_layout.addWidget(self.time_label)

        # layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(main_layout)

        # conexão do botão
        self.start_button.clicked.connect(self.start_game)

        # timers
        self.game_timer = QTimer(self)
        self.game_timer.setInterval(1000)
        self.game_timer.timeout.connect(self.update_time)

        self.spawn_timer = QTimer(self)
        self.spawn_timer.timeout.connect(self.spawn_ghost)
    # inicio
    def start_game(self):
        self.clear_ghosts()
        self.score = 0
        self.time_left = 30
        self.score_label.setText(f"Pontos: {self.score}")
        self.time_label.setText(f"Tempo: {self.time_left}s")

        self.game_timer.start()
        self.spawn_timer.start(800)
        self.start_button.setEnabled(False)
    # tempo
    def update_time(self):
        self.time_left -= 1
        self.time_label.setText(f"Tempo: {self.time_left}s")

        # aumenta dificuldade
        if self.time_left % 5 == 0 and self.spawn_timer.interval() > 300:
            self.spawn_timer.setInterval(max(300, self.spawn_timer.interval() - 100))
        #  fim
        if self.time_left <= 0:
            self.end_game()
    # fantasma
    def spawn_ghost(self):
        ghost = GhostLabel("👻", lifespan_ms=1000, parent=self)
        ghost_width, ghost_height = ghost.width(), ghost.height()

        # posição aleatória no fundo 
        x = random.randint(20, self.width() - ghost_width - 20)
        y = random.randint(80, self.height() - ghost_height - 20)
        ghost.move(x, y)
        ghost.show()

        # comportamento ao clicar
        def on_click(event):
            self.score += 1
            self.score_label.setText(f"Pontos: {self.score}")
            ghost.deleteLater()
            if ghost in self.active_ghosts:
                self.active_ghosts.remove(ghost)

        ghost.mousePressEvent = on_click
        self.active_ghosts.append(ghost)

        # desaparece sozinho
        QTimer.singleShot(ghost.lifespan_ms, lambda: self.remove_ghost(ghost))

    def remove_ghost(self, ghost):
        if ghost in self.active_ghosts:
            ghost.deleteLater()
            self.active_ghosts.remove(ghost)

    def clear_ghosts(self):
        for g in list(self.active_ghosts):
            g.deleteLater()
        self.active_ghosts.clear()

    def end_game(self):
        self.game_timer.stop()
        self.spawn_timer.stop()
        self.clear_ghosts()
        self.start_button.setEnabled(True)
        self.time_label.setText("Tempo: 0s — Fim!")
        self.score_label.setText(f"Pontos finais: {self.score}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec_())
