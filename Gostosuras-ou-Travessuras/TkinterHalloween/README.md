# Adivinhe o Monstro — Jogo com Interface Gráfica em Tkinter

Este projeto foi desenvolvido como parte de um **seminário sobre Interfaces Gráficas**, com o objetivo de demonstrar o uso da biblioteca **Tkinter**, que é a biblioteca padrão do Python para criação de GUIs (interfaces gráficas).

---

## Sobre o Projeto

O **Adivinhe o Monstro** é um jogo educativo e divertido em que o usuário deve **adivinhar qual monstro** está sendo descrito com base em uma **dica exibida na tela**.
O objetivo é testar o raciocínio e o conhecimento do jogador sobre criaturas lendárias e de terror. 👻

---

## Conceitos Demonstrados

* Criação de **janelas gráficas** com `Tk()`
* Uso de **widgets básicos** (`Label`, `Button`, `Entry`)
* Manipulação de **eventos de clique**
* Utilização de **caixas de mensagem (`messagebox`)** para feedback ao jogador
* Aplicação de **cores, tamanhos e fontes** para estilização
* Uso de **funções e variáveis globais** para controle do jogo

---

## Estrutura do Código

`monstros`

Lista de tuplas contendo o **nome do monstro** e uma **dica associada**.

`def escolher_monstro()`

Seleciona aleatoriamente um monstro da lista e exibe sua dica na interface.

`def verificar_resposta()`

Compara a resposta digitada pelo jogador com o nome do monstro atual.

* Se estiver correta, exibe uma mensagem de sucesso.
* Se estiver errada, exibe uma mensagem de erro e permite tentar novamente.

---

## Como Executar

### 1. Certifique-se de ter o Python instalado.

Tkinter já vem incluso por padrão.

### 2. Execute o jogo:

```bash
python Tkinter.py
```

---

## Regras do Jogo

* Clique em **“Dica”** para receber uma descrição de um monstro.
* Digite o nome do monstro no campo de texto e clique em **“Verificar Resposta”**.
* O jogo mostrará se você acertou ou errou!
* Cada acerto gera uma nova dica automaticamente.

---

## Tecnologias Utilizadas

| Tecnologia     | Função                                   |
| -------------- | ---------------------------------------- |
| **Python 3**   | Linguagem de programação                 |
| **Tkinter**    | Biblioteca padrão para interface gráfica |
| **messagebox** | Exibição de mensagens interativas        |

---

## Interface

A interface é simples, intuitiva e tematizada com **tons escuros e cores vibrantes** para combinar com a estética de terror e Halloween.

---

## Autor

**Kennedy Veras**

Desenvolvido para o seminário de **Interfaces Gráficas**.
