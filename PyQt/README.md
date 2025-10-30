# Bloco de Notas com PyQt5

Projeto desenvolvido para um **seminário com o tema “Interfaces Gráficas”**, demonstrando como criar uma aplicação de interface amigável usando **Python e PyQt5**.

Este projeto implementa um **Mini Bloco de Notas**, com funcionalidades de abrir, editar e salvar arquivos de texto em uma interface simples e intuitiva.

---

## Demonstração

A aplicação permite ao usuário:

* Criar e editar textos;
* Abrir arquivos `.txt`;
* Salvar o conteúdo digitado;
* Ver informações sobre o programa no menu “Ajuda”.

---

## Tecnologias Utilizadas

* **Python 3.10+**
* **PyQt5** — Biblioteca para criação de interfaces gráficas no Python.

---

## Estrutura do Projeto

```
 BlocoDeNotas_PyQt5
├── PyQt.py              # Código principal da aplicação
├── README.md            # Documentação do projeto
```

---

## Como Executar

### Clonar o repositório

```bash
git clone https://github.com/seu-usuario/blocodenotas-pyqt5.git
cd blocodenotas-pyqt5
```

### Instalar dependências

Certifique-se de ter o Python instalado e execute:

```bash
pip install PyQt5
```

### Rodar o programa

```bash
python PyQt.py
```

---

## Explicação Técnica

O projeto foi construído com base na classe `QMainWindow`, que permite criar uma janela principal com menus e widgets.

**Componentes principais:**

* `QTextEdit`: área de texto para edição de conteúdo.
* `QFileDialog`: permite abrir e salvar arquivos.
* `QMessageBox`: exibe janelas de informação (como o menu “Sobre”).
* `QAction`: cria ações nos menus interativos.
* `QMenuBar`: adiciona menus como “Arquivo” e “Ajuda”.

**Menus implementados:**

* **Arquivo**

  * `Abrir`: carrega um arquivo `.txt` para edição.
  * `Salvar`: salva o texto digitado em um arquivo.
  * `Sair`: fecha o programa.
* **Ajuda**

  * `Sobre`: exibe informações sobre o aplicativo.

---

## Autor

Desenvolvido por **Allany Dias**

Projeto apresentado como parte de um **seminário sobre Interfaces Gráficas**.

---

## Licença

Este projeto está sob a licença **MIT** — sinta-se livre para usar, modificar e compartilhar.

---
