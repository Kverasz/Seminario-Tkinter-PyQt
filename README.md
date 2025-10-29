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

A apresentação contém um exemplo prático de uma aplicação GUI desenvolvida em Tkinter, que é um jogo simples de "Adivinhe os Monstros".

O código-fonte demonstra a implementação dos seguintes conceitos básicos:

1.  **Importação:** `import tkinter as tk` e `from tkinter import messagebox`.
2.  **Configuração da Janela Raiz:** Criação (`root = tk.Tk()`), título, tamanho (`root.geometry`) e cor de fundo (`root.config`).
3.  **Widgets:** Uso de `Label` (títulos e dicas), `Entry` (campo de resposta) e `Button` (botões de ação).
4.  **Associação de Eventos:** O botão é associado a funções Python (o `command=`) para realizar ações, como `escolher_monstro` e `verificar_resposta`.
5.  **Loop Principal:** `root.mainloop()` para manter a janela aberta e responsiva a eventos.

---

## 6. Perspectivas Futuras

Ambas as bibliotecas continuam relevantes no ecossistema Python.

* **Tkinter:** Seguirá como principal ferramenta para o **ensino** dos fundamentos de GUI e para a criação de **soluções internas/simples**.
* **PyQt:** Manterá seu valor em **aplicações profissionais e complexas**.

Para o futuro, ambas podem ser usadas em cenários avançados de desenvolvimento, como:

* Integração com **Inteligência Artificial (IA)**.
* Visualização de **dados em tempo real** (usando os poderosos recursos gráficos do PyQt).
* Criação de aplicativos híbridos que conectam o *desktop* à *web*.

---

## 7. Referências:

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
