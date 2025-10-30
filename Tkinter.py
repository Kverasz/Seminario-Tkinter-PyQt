import customtkinter as ctk

#aparencia
ctk.set_appearance_mode('dark')

#funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #verificar ususario
    if usuario == 'heuryk' and senha == 'senacpe':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',text_color='red')


#janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')
#campos
#label
label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)
#entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#label
label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)
#entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha')
campo_senha.pack(pady=10)
#button
botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)
#feedback
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

#iniciar app
app.mainloop()