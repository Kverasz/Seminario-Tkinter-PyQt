import tkinter as tk
from tkinter import messagebox
import random

# Lista de monstros e dicas
monstros = [
    ("Vampiro", "Tem dentes afiados e se alimenta de sangue."),
    ("Zumbi", "Caminha lentamente e tem pele esverdeada."),
    ("Lobisomem", "Transforma-se em um lobo nas noites de lua cheia."),
    ("Fantasma", "É invisível, mas pode ser ouvido fazendo barulhos assustadores."),
    ("Múmia", "É uma figura embalada em faixas de pano.")
]

# Função para escolher um monstro aleatório e exibir a pista
def escolher_monstro():
    global monstro_atual, dica_atual
    monstro_atual, dica_atual = random.choice(monstros)
    label_dica.config(text=f"Dica: {dica_atual}")

# Função para verificar a resposta do jogador
def verificar_resposta():
    resposta = entry_resposta.get().strip().lower()
    if resposta == monstro_atual.lower():
        messagebox.showinfo("Correto!", "Você acertou! Muito bem!")
        escolher_monstro()  
        entry_resposta.delete(0, tk.END)  
    else:
        messagebox.showerror("Errado!", "Que pena, você errou! Tente novamente!")
        entry_resposta.delete(0, tk.END)  

# Config da janela principal
root = tk.Tk()
root.title("Winx Seminario")
root.geometry("500x300")
root.config(bg="#222")

# Titulo
label_titulo = tk.Label(root, text="Adivinhe os Monstros! MUAHAHAH", font=("Helvetica", 16), fg="orange", bg="#222")
label_titulo.pack(pady=20)

# Texto das dicas
label_dica = tk.Label(root, text="Clique em 'Dica' para uma começar!", font=("Helvetica", 12), fg="white", bg="#222")
label_dica.pack(pady=10)

# Campo de digitar o monstro
entry_resposta = tk.Entry(root, font=("Helvetica", 14))
entry_resposta.pack(pady=10)

# Botões de interação
button_comecar = tk.Button(root, text="Dica", font=("Helvetica", 12), command=escolher_monstro)
button_comecar.pack(pady=10)

button_verificar = tk.Button(root, text="Verificar Resposta", font=("Helvetica", 12), command=verificar_resposta)
button_verificar.pack(pady=10)

# Rodar a interface
root.mainloop()
