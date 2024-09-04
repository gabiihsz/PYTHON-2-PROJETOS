import sys
import tkinter as tk
from tkinter import messagebox, Menu
import os

# Funções para abrir diferentes páginas
def abrir_app():
    try:
        janela.destroy()  # Fecha a janela atual
        os.system('python appusu.py')  # Abre o arquivo appusu.py
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir appusu.py: {str(e)}")

def abrir_cidade():
    try:
        janela.destroy()  # Fecha a janela atual
        os.system('python appcid.py')  # Abre o arquivo appcid.py
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir appcid.py: {str(e)}")

def abrir_cliente():
    try:
        janela.destroy()  # Fecha a janela atual
        os.system('python appcli.py')  # Abre o arquivo appcli.py
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir appcli.py: {str(e)}")

# Função para sair da aplicação
def sair():
    sys.exit()

# Função para mostrar a ajuda
def mostrar_ajuda():
    messagebox.showinfo("Ajuda", "Selecione a opção desejada no menu para abrir a página correspondente ou saia da aplicação.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Rotas")

# Criação da barra de menu
menubar = Menu(janela)
janela.config(menu=menubar)

# Menu "Arquivo"
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=filemenu)
filemenu.add_command(label="Usuários", command=abrir_app)
filemenu.add_command(label="Cidades", command=abrir_cidade)
filemenu.add_command(label="Clientes", command=abrir_cliente)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=sair)

# Menu "Ajuda"
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Mostrar Ajuda", command=mostrar_ajuda)

# Título
titulo = tk.Label(janela, text="Rotas", font=("Arial", 24, "bold"))
titulo.pack(pady=20)



# Executar a janela
if _name_ == "_main_":
    janela.state("zoomed")
    janela.mainloop()