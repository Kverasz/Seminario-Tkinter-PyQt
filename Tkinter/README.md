# Sistema de Login com CustomTkinter

Projeto desenvolvido para o **seminário sobre Interfaces Gráficas**, com o objetivo de demonstrar a criação de uma aplicação simples e funcional utilizando **Python e CustomTkinter** — uma versão moderna e personalizável do Tkinter.

Este projeto implementa uma **interface de login** estilizada no modo escuro, com validação de credenciais e feedback visual ao usuário.

---

## Demonstração

A aplicação apresenta:

* Campos para **usuário** e **senha**;
* Botão de **Login** com verificação simples;
* Mensagens de feedback (“Login feito com sucesso!” ou “Login incorreto”);
* Interface escura e moderna usando o tema **CustomTkinter Dark Mode**.

---

## Tecnologias Utilizadas

* **Python 3.10+**
* **CustomTkinter** — Biblioteca moderna para construção de interfaces gráficas com aparência aprimorada.

---

## Estrutura do Projeto

```
SistemaLogin_CustomTkinter
├── Tkinter.py           # Código principal da aplicação
├── README.md            # Documentação do projeto
```

---

## Como Executar

### Clonar o repositório

```bash
git clone https://github.com/seu-usuario/sistema-login-tkinter.git
cd sistema-login-tkinter
```

### Instalar dependências

Certifique-se de ter o Python instalado e execute:

```bash
pip install customtkinter
```

### Rodar o programa

```bash
python Tkinter.py
```

---

## Explicação Técnica

A aplicação foi desenvolvida utilizando **CustomTkinter (ctk)**, uma biblioteca baseada no Tkinter tradicional, mas com suporte a **design moderno**, **modo escuro** e componentes personalizados.

**Componentes principais:**

* `CTkLabel`: rótulos de texto para identificar os campos.
* `CTkEntry`: campos de entrada para o usuário e a senha.
* `CTkButton`: botão para confirmar o login.
* `CTk`: janela principal da aplicação.

**Lógica de funcionamento:**

1. O usuário digita suas credenciais.
2. Ao clicar no botão **Login**, a função `validar_login()` é chamada.
3. Se o usuário for `"heuryk"` e a senha `"senacpe"`, aparece a mensagem de sucesso.
4. Caso contrário, é exibida uma mensagem de erro.

---

## Autor

Desenvolvido por **Mariana Oliveira**

Projeto apresentado como parte de um **seminário sobre Interfaces Gráficas**.

---

## Licença

Este projeto está sob a licença **MIT** — livre para uso, modificação e distribuição.
