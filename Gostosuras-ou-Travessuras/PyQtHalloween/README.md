# Caça-Fantasma — Jogo com Interface Gráfica em PyQt5 

Este projeto foi desenvolvido como parte de um **seminário sobre Interfaces Gráficas**, com o objetivo de demonstrar o uso da biblioteca **PyQt5** na criação de aplicações interativas e visuais em Python.

---

## Sobre o Projeto

O **Caça-Fantasma** é um mini-jogo em que o jogador deve clicar nos fantasmas 👻 que aparecem aleatoriamente na tela para marcar pontos.
O desafio é **acumular o maior número de pontos** antes que o tempo acabe!

---

## Conceitos Demonstrados

* Criação de **janelas gráficas** com `QWidget`
* Uso de **layouts** (`QVBoxLayout`, `QHBoxLayout`)
* **Eventos de clique** com `mousePressEvent`
* Uso de **temporizadores (`QTimer`)** para controle do tempo e geração de fantasmas
* Estilização com **QPalette** e **QStyleSheet**
* **Atualização dinâmica de interface** (pontuação, tempo, dificuldade)

---

## Estrutura do Código

 `class GhostLabel(QLabel)`

Representa cada fantasma na tela (um emoji 👻).

* Possui um tempo de vida (`lifespan_ms`) antes de desaparecer.
* Detecta cliques para incrementar a pontuação.

 `class GameWindow(QWidget)`

Gerencia toda a interface e lógica do jogo.

* Inicializa a janela, pontuação, tempo e botão de início.
* Controla os temporizadores do jogo e o surgimento de fantasmas.
* Atualiza a interface conforme o jogo progride.

---

## Como Executar

### 1. Instale o PyQt5

```bash
pip install PyQt5
```

### 2. Execute o jogo

```bash
python PyQt.py
```

---

## Regras do Jogo

* Clique nos fantasmas para ganhar pontos.
* Cada fantasma desaparece automaticamente após 1 segundo.
* O tempo total de jogo é de **30 segundos**.
* A dificuldade aumenta gradualmente, reduzindo o intervalo de aparição dos fantasmas.
* Quando o tempo chega a zero, o jogo exibe sua pontuação final.

---

## Tecnologias Utilizadas

| Tecnologia              | Função                                         |
| ----------------------- | ---------------------------------------------- |
| **Python 3**            | Linguagem base                                 |
| **PyQt5**               | Biblioteca de interface gráfica                |
| **Qt Widgets / Timers** | Gerenciamento de eventos e componentes visuais |

---

## Captura de Tela 


> <img width="605" height="434" alt="image" src="https://github.com/user-attachments/assets/4edd8a13-b11a-436b-9e44-edf69e2e03b1" />


---

## Autor

**Kennedy Veras**

Desenvolvido para o seminário de **Interfaces Gráficas**.
