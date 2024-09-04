import tkinter as tk
from tkinter import messagebox
import os
from cidades import cidade


class Application:
    def _init_(self, root):
        self.cidade = cidade()

        self.root = root
        self.root.title("Cadastro de Cidades")

        # Widgets
        self.lblIdcidade = tk.Label(root, text="ID da Cidade:")
        self.lblIdcidade.grid(row=0, column=0)
        self.txtIdcidade = tk.Entry(root)
        self.txtIdcidade.grid(row=0, column=1)

        self.btnBuscar = tk.Button(root, text="Buscar", command=self.buscar_cidade)
        self.btnBuscar.grid(row=0, column=2)

        self.lblNome = tk.Label(root, text="Nome:")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblUf = tk.Label(root, text="UF:")
        self.lblUf.grid(row=2, column=0)
        self.txtUf = tk.Entry(root)
        self.txtUf.grid(row=2, column=1)

        # Botões
        self.btnInserir = tk.Button(root, text="Inserir", command=self.inserir_cidade)
        self.btnInserir.grid(row=3, column=0)

        self.btnAlterar = tk.Button(root, text="Alterar", command=self.alterar_cidade)
        self.btnAlterar.grid(row=3, column=1)

        self.btnExcluir = tk.Button(root, text="Excluir", command=self.excluir_cidade)
        self.btnExcluir.grid(row=3, column=2)

        self.lblMensagem = tk.Label(root, text="")
        self.lblMensagem.grid(row=4, column=0, columnspan=3)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_cidade(self):
        idCidade = self.txtIdcidade.get()
        resultado = self.cidade.buscar(idCidade)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtUf.delete(0, tk.END)
            self.txtUf.insert(tk.END, resultado[2])
            self.lblMensagem.config(text="Busca realizada com sucesso!")
        else:
            self.lblMensagem.config(text="Cidade não encontrada!")

    def inserir_cidade(self):
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        self.cidade.inserir(nome, uf)
        self.lblMensagem.config(text="Cidade inserida com sucesso!")

    def alterar_cidade(self):
        idCidade = self.txtIdcidade.get()
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        self.cidade.alterar(idCidade, nome, uf)
        self.lblMensagem.config(text="Cidade alterada com sucesso!")

    def excluir_cidade(self):
        idCidade = self.txtIdcidade.get()
        self.cidade.excluir(idCidade)
        self.lblMensagem.config(text="Cidade excluída com sucesso!")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')  # Reabre o principal.py ao fechar a janela


# Execução da interface
if _name_ == "_main_":
    root = tk.Tk()
    app = Application(root)
    root.state("zoomed")
    root.mainloop()