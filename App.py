import tkinter as tk
from tkinter import messagebox
from Usuarios import Usuarios

class Application:
    def __init__(self, root):
        self.usuario = Usuarios()
        self.root = root
        self.root.title("Cadastro de Usuários")

        # Widgets
        self.lblIdUsuario = tk.Label(root, text="idUsuario:")
        self.lblIdUsuario.grid(row=0, column=0)
        self.txtIdUsuario = tk.Entry(root)
        self.txtIdUsuario.grid(row=0, column=1)

        self.btnBuscar = tk.Button(root, text="Buscar", command=self.buscar_usuario)
        self.btnBuscar.grid(row=0, column=2)

        self.lblNome = tk.Label(root, text="Nome:")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblTelefone = tk.Label(root, text="Telefone:")
        self.lblTelefone.grid(row=2, column=0)
        self.txtTelefone = tk.Entry(root)
        self.txtTelefone.grid(row=2, column=1)

        self.lblEmail = tk.Label(root, text="E-mail:")
        self.lblEmail.grid(row=3, column=0)
        self.txtEmail = tk.Entry(root)
        self.txtEmail.grid(row=3, column=1)

        self.lblUsuario = tk.Label(root, text="Usuário:")
        self.lblUsuario.grid(row=4, column=0)
        self.txtUsuario = tk.Entry(root)
        self.txtUsuario.grid(row=4, column=1)

        self.lblSenha = tk.Label(root, text="Senha:")
        self.lblSenha.grid(row=5, column=0)
        self.txtSenha = tk.Entry(root, show="*")
        self.txtSenha.grid(row=5, column=1)

        # Botões
        self.btnInserir = tk.Button(root, text="Inserir", command=self.inserir_usuario)
        self.btnInserir.grid(row=6, column=0)

        self.btnAlterar = tk.Button(root, text="Alterar", command=self.alterar_usuario)
        self.btnAlterar.grid(row=6, column=1)

        self.btnExcluir = tk.Button(root, text="Excluir", command=self.excluir_usuario)
        self.btnExcluir.grid(row=6, column=2)

        self.lblMensagem = tk.Label(root, text="")
        self.lblMensagem.grid(row=7, column=0, columnspan=3)

    def buscar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        resultado = self.usuario.buscar(idUsuario)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEmail.delete(0, tk.END)
            self.txtEmail.insert(tk.END, resultado[3])
            self.txtUsuario.delete(0, tk.END)
            self.txtUsuario.insert(tk.END, resultado[4])
            self.txtSenha.delete(0, tk.END)
            self.txtSenha.insert(tk.END, resultado[5])
            self.lblMensagem.config(text="Busca realizada com sucesso!")
        else:
            self.lblMensagem.config(text="Usuário não encontrado!")

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.inserir(nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário inserido com sucesso!")

    def alterar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário alterado com sucesso!")

    def excluir_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        self.usuario.excluir(idUsuario)
        self.lblMensagem.config(text="Usuário excluído com sucesso!")

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()