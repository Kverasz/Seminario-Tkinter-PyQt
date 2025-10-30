# Análise Comparativa de Interfaces Gráficas (GUI) em Python: Tkinter vs. PyQt

![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
<img src="https://miro.medium.com/v2/0*uzNNniKqLDmyx2pX" width="50">

## 1. Introdução às Interfaces Gráficas de Usuário (GUI)

Uma **Interface Gráfica do Usuário (GUI)** consiste em elementos visuais que facilitam a interação do usuário com um software. Em Python, existem diversas bibliotecas para desenvolver GUIs Desktop, sendo **Tkinter** e **PyQt** duas das mais proeminentes.

Este documento apresenta uma análise comparativa dessas duas bibliotecas, destacando suas características, vantagens, desvantagens e casos de uso ideais.

## 2. Tkinter

### 2.1. O que é?

* **Biblioteca nativa do Python** para a criação de GUIs.
* É a **biblioteca padrão** do Python, e já vem instalada com a maioria das distribuições da linguagem. É uma interface para o kit de ferramentas **Tcl/Tk**.

### 2.2. Conceitos Centrais

* **Janela Raiz (`root`):** O contêiner principal que abriga todos os elementos.
* **Widgets:** Componentes visuais como botões (`Button`), rótulos (`Label`) e caixas de texto.
* **Gerenciadores de Layout:** Métodos como `.pack()` e `.grid()` são utilizados para organizar a posição dos widgets na janela.

### 2.3. Vantagens e Desvantagens (Prós e Contras)

| Vantagens (Prós) | Desvantagens (Contras) |
| :--- | :--- |
| **Simples:** Curva de aprendizado mais fácil e rápida. É a porta de entrada para iniciantes. | **Aparência Datada:** O visual não é moderno, apresentando um estilo básico que lembra programas antigos (ex: Windows XP/Vista). |
| **Leve e Rápido:** Não requer instalação nem dependências externas. Ótimo para *scripts* rápidos e ferramentas internas. | **Limitado:** Possui poucos *widgets* avançados (sem recursos para tabelas complexas, gráficos, etc.). |
| **Gratuito e Livre:** Possui uma licença permissiva e pode ser utilizado para uso comercial sem custos. | **Performance:** Seu desempenho pode ser baixo em comparação com outras bibliotecas (embora seja aceitável para aplicações simples). |

### 2.4. Uso Ideal

* Iniciantes e desenvolvedores que buscam aprender os fundamentos de GUI.
* Projetos acadêmicos, ferramentas internas simples (ex: calculadoras) e *scripts* de automação rápidos.

---

## 3. PyQt

### 3.1. O que é?

* É o **Binding** (ponte/conexão) da poderosa biblioteca **Qt** para Python.
* **Qt** é um *framework* robusto e multiplataforma escrito em linguagem **C++**.
* **Requer instalação** via gerenciador de pacotes (ex: `pip install PyQt6`).

### 3.2. Conceitos Centrais

* **Sinais e Slots:** Utiliza um sistema avançado para gerenciamento de eventos. Um *Sinal* (ex: o clique de um botão) é conectado a um *Slot*, que é uma função de resposta (ação).

### 3.3. Vantagens e Desvantagens (Prós e Contras)

| Vantagens (Prós) | Desvantagens (Contras) |
| :--- | :--- |
| **Aparência Moderna:** Oferece um visual nativo, profissional e altamente personalizável. | **Complexo:** Apresenta uma curva de aprendizado mais alta devido à sua maior complexidade e ao uso de conceitos como Sinais e Slots. |
| **Poderoso e Completo:** Oferece um catálogo imenso de *widgets* avançados. Inclui módulos para rede, banco de dados, e outras funcionalidades. | **Licença Restritiva:** O modelo de licenciamento padrão (GPL) exige que sua aplicação tenha o código-fonte aberto se for distribuída gratuitamente. Caso contrário, é necessária a compra de uma licença comercial. |
| **Ferramenta Visual (`Qt Designer`):** Permite a criação da interface visual via "arrastar e soltar". | **Requer Instalação:** Não é nativo e precisa ser instalado separadamente. |
| **Multiplataforma:** Pode ser executado em Windows, Linux, Android, iOS e outros sistemas. | |

> **Informação Complementar:** Uma alternativa ao PyQt, com funcionalidades muito semelhantes, é o **PySide**, que é licenciado sob **LGPL** e é frequentemente preferido para o desenvolvimento de software comercial gratuito, pois sua licença é menos restritiva do que a GPL do PyQt.

### 3.4. Uso Ideal

* Desenvolvimento de aplicações desktop robustas, complexas, profissionais e modernas.
* Sistemas de controle industrial, *dashboards* gerenciais e programas científicos.

---

## 4. Comparativo Resumido

| Característica | **Tkinter** | **PyQt** |
| :--- | :--- | :--- |
| **Instalação** | Já vem com o Python | Requer instalação (`pip`) |
| **Aparência** | Básica, datada | Moderna, nativa |
| **Complexidade** | Baixa (Fácil de aprender) | Alta (Profissional) |
| **Widgets** | Limitados | Extensos e avançados |
| **Ferramenta Visual** | Não | Sim (Qt Designer) |
| **Licença** | Permissiva (Livre) | GPL (Restritiva) ou Comercial |

---

## 5. Exemplo de Aplicação Prática (Tkinter)

A seguir, é apresentado um exemplo prático de uma aplicação GUI (Interface Gráfica de Usuário) desenvolvida com CustomTkinter, uma versão moderna e estilizada do Tkinter.
O exemplo demonstra a criação de um sistema simples de login com validação de usuário e senha.

O código-fonte demonstra a implementação dos seguintes conceitos básicos:

1.  **Importação:** `import customtkinter as ctk`.
2.  **Aparência e Janela Principal:** Modo escuro (`ctk.set_appearance_mode('dark')`), janela principal (`app = ctk.CTk()`), define titulo (`app.title()`) e o tamanho (`app.geometry())`).
3.  **Widgets:** Uso de `CTkLabel` (exibe textos fixos como “Usuário” e “Senha”), `CTkEntry` (campos de entrada para digitação), `CTkButton` (botão de ação “Login”) e outro `CTkLabel` (exibe mensagens de resultado [sucesso ou erro]).
4.  **Associação de Eventos:** O botão Login está vinculado à função (`validar_login`) por meio do parâmetro (`command`). Essa função captura os valores digitados e verifica se o usuário e senha estão corretos, atualizando a mensagem de feedback na tela.
5.  **Loop Principal:** A chamada `app.mainloop()` mantém a janela aberta e responsiva aos eventos (cliques e digitação), garantindo a execução contínua da aplicação.

---

## 6. Exemplo de Aplicação Prática (PyQt5)

A seguir, é apresentado um exemplo prático de uma aplicação GUI (Interface Gráfica de Usuário) desenvolvida com PyQt5, que implementa um Bloco de Notas simples, permitindo abrir, editar e salvar arquivos de texto.

O código-fonte demonstra a implementação dos seguintes conceitos básicos:

1.  **Importação:** `import sys`, `from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)`, `from PyQt5.QtGui import QIcon`.
2.  **Criação da Janela Principal:** A classe `BlocoDeNotas` herda de `QMainWindow`, a janela principal típica de aplicações desktop.
`class BlocoDeNotas(QMainWindow):`

```
     def __init__(self):
        super().__init__()

        self.texto = QTextEdit()
        self.setCentralWidget(self.texto)

        self.setWindowTitle("Bloco de Notas - PyQt5")
        self.setGeometry(200, 200, 600, 400)

        self.criar_menu()

```

* Define o título, tamanho e posição da janela.
* O `QTextEdit` é usado como área central de texto.
* O método `criar_menu()` monta a barra de menus.

4.  **Widgets:** O método `criar_menu()` adiciona menus e ações à aplicação:

```

menu_bar = self.menuBar()
menu_arquivo = menu_bar.addMenu("Arquivo")

abrir_acao = QAction("Abrir", self)
abrir_acao.triggered.connect(self.abrir_arquivo)
menu_arquivo.addAction(abrir_acao)

```

* Cada item do menu é uma instância de `QAction`, que se conecta a uma função Python (ex: `abrir_arquivo`, `salvar_arquivo`, `close`).
4.  **Associação de Eventos:** As ações são vinculadas a métodos específicos que executam operações:
* Abrir arquivo: usa `QFileDialog.getOpenFileName()` para selecionar e carregar o conteúdo.
* Salvar arquivo: usa `QFileDialog.getSaveFileName()` para gravar o texto atual.
* Sobre: exibe uma caixa de diálogo `QMessageBox.information()` com informações do app.

```

def mostrar_sobre(self):
    QMessageBox.information(
        self,
        "Sobre",
        "Mini Bloco de Notas feito com PyQt5\n😄"
    `)

```

5.  **Loop Principal:** A execução da aplicação é iniciada com:

```

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = BlocoDeNotas()
    janela.show()
    sys.exit(app.exec_())

```

Essa estrutura:

* Cria a instância da aplicação (`QApplication`);
* Exibe a janela (`show()`);
* Mantém o programa ativo até o usuário fechá-lo (`app.exec_()`).

---

## 7. Perspectivas Futuras

Ambas as bibliotecas continuam relevantes no ecossistema Python.

* **Tkinter:** Seguirá como principal ferramenta para o **ensino** dos fundamentos de GUI e para a criação de **soluções internas/simples**.
* **PyQt:** Manterá seu valor em **aplicações profissionais e complexas**.

Para o futuro, ambas podem ser usadas em cenários avançados de desenvolvimento, como:

* Integração com **Inteligência Artificial (IA)**.
* Visualização de **dados em tempo real** (usando os poderosos recursos gráficos do PyQt).
* Criação de aplicativos híbridos que conectam o *desktop* à *web*.

---

## 8. Referências:

- NASCIMENTO, ANDERSON. O que é GUI? Canaltech. 01 set. 2014. Disponível em: https://canaltech.com.br/produtos/O-que-e-GUI/. Acesso em: 21 out. 2025. Canaltech

- POZO RAMOS, LEODANIS. Python and PyQt: Building a GUI Desktop Calculator. Real Python. Disponível em: https://realpython.com/python-pyqt-gui-calculator/. Acesso em: 21 out. 2025. realpython.com

- CGS, CARLOS. O que é e como Utilizar a Biblioteca Tkinter em Python. DIO. 15 maio 2024. Disponível em: https://www.dio.me/articles/o-que-e-e-como-utilizar-a-biblioteca-tkinter-em-python. Acesso em: 22 out. 2025. DIO

- What Are the Benefits of Using Python for GUI Development? ParallelStaff. Disponível em: https://parallelstaff.com/benefits-of-using-python-for-gui-development/. Acesso em: 22 out. 2025.

- STILEST. PyQt vs Tkinter: Comparing User Interface Libraries in Python. Medium, 22 nov. 2023. Disponível em: https://medium.com/@wepypixel/pyqt-vs-tkinter-comparing-user-interface-libraries-in-python-273a2cc84c7b. Acesso em: 23 out. 2025.


---

## Grupo:
- Kennedy Veras
- Mariana Oliveira
- Lorena Torres
- Allany Dias
- Mayara Marina
