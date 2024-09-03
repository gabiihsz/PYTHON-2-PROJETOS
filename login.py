import tkinter as tk
from tkinter import messagebox, PhotoImage, Frame
import principal

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        root.destroy()
        principal.abrir_pagina_principal()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

class Imagem():
    def __init__(self, master):
        self.wdgt3 = tk.Frame(master)
        self.wdgt3["padx"] = 20
        self.wdgt3["pady"] = 5
        self.wdgt3.pack()

        self.img = PhotoImage(file="imagem/17004.png")
        self.lblimg = tk.Label(self.wdgt3, image=self.img)
        self.lblimg.pack()


root = tk.Tk()
root.title("Tela de Login")


frame = tk.Frame(root)
frame.pack(padx=20, pady=20, expand=True)



label_usuario = tk.Label(frame, text="Usuário:")
label_usuario.pack(pady=(10, 0))
entry_usuario = tk.Entry(frame)
entry_usuario.pack(pady=(5, 10))

label_senha = tk.Label(frame, text="Senha:")
label_senha.pack(pady=(10, 0))

entry_senha = tk.Entry(frame, show="*")
entry_senha.pack(pady=(5, 10))
btn_login = tk.Button(frame, text="Login", command=verificar_login)
btn_login.pack(pady=20)

root.geometry("300x300")
root.mainloop()


