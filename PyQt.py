import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QIcon


class BlocoDeNotas(QMainWindow):
    def __init__(self):  
        super().__init__()

        # Área de texto
        self.texto = QTextEdit()
        self.setCentralWidget(self.texto)

        # Configurações da janela
        self.setWindowTitle("Bloco de Notas - PyQt5")
        self.setGeometry(200, 200, 600, 400)

        # Criação do menu
        self.criar_menu()

    def criar_menu(self):
        menu_bar = self.menuBar()

        # Menu Arquivo
        menu_arquivo = menu_bar.addMenu("Arquivo")

        # Ações
        abrir_acao = QAction("Abrir", self)
        abrir_acao.triggered.connect(self.abrir_arquivo)
        menu_arquivo.addAction(abrir_acao)

        salvar_acao = QAction("Salvar", self)
        salvar_acao.triggered.connect(self.salvar_arquivo)
        menu_arquivo.addAction(salvar_acao)

        sair_acao = QAction("Sair", self)
        sair_acao.triggered.connect(self.close)
        menu_arquivo.addAction(sair_acao)

        # Menu Ajuda
        menu_ajuda = menu_bar.addMenu("Ajuda")
        sobre_acao = QAction("Sobre", self)
        sobre_acao.triggered.connect(self.mostrar_sobre)
        menu_ajuda.addAction(sobre_acao)

    def abrir_arquivo(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Arquivo",
            "",
            "Text Files (.txt);;All Files ()"  
        )
        if caminho:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.texto.setText(arquivo.read())

    def salvar_arquivo(self):
        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo",
            "",
            "Text Files (.txt);;All Files ()"  
        )
        if caminho:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write(self.texto.toPlainText())

    def mostrar_sobre(self):
        QMessageBox.information(
            self,
            "Sobre",
            "Mini Bloco de Notas feito com PyQt5\n😄"
        )


# Execução da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = BlocoDeNotas()
    janela.show()
    sys.exit(app.exec_())