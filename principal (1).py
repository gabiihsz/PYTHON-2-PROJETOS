import tkinter as tk
from tkinter import messagebox

def mostrar_usuarios():
    messagebox.showinfo("Usuários","Botão de Usuários clicado")

def mostrar_cidades():
    messagebox.showinfo("Cidades","Botão de Cidades clicado")

def mostrar_clientes():
    messagebox.showinfo("Clientes","Botão de Clientes clicado")

def fechar_janela():
    root.destroy()

root = tk.Tk()
root.title("Interface de Botões")

titulo = tk.Label(root, text="INFORME OS DADOS", font=("Arial", 16))
titulo.pack(pady=20)

botao_usuarios = tk.Button(root, text="Usuários", command=mostrar_usuarios)
botao_usuarios.pack(pady=18)

botao_cidades = tk.Button(root, text="Cidades", command=mostrar_cidades)
botao_cidades.pack(pady=18)

botao_clientes = tk.Button(root, text="Clientes", command=mostrar_clientes)
botao_clientes.pack(pady=18)

botao_fechar = tk.Button(root, text="Fechar", command=fechar_janela)
botao_fechar.pack(pady=18)


root.mainloop()