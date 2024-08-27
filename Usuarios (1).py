from tkinter import *

class Usuarios:
    db = {
        '1': {'nome': 'Gabi', 'telefone': '123456786', 'email': 'gabi@example.com', 'usuario': 'joao123',
              'senha': 'senha123'},
        '2': {'nome': 'Esther', 'telefone': '987654328', 'email': 'esther@example.com', 'usuario': 'maria123',
              'senha': 'senha456'}
    }

    def __init__(self):
        self.idusuario = None
        self.nome = None
        self.telefone = None
        self.email = None
        self.usuario = None
        self.senha = None

    def insertUser(self):
        if self.idusuario in Usuarios.db:
            return "Usuário já existe."
        Usuarios.db[self.idusuario] = {
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'usuario': self.usuario,
            'senha': self.senha
        }
        return "Usuário inserido com sucesso."

    def updateUser(self):
        if self.idusuario not in Usuarios.db:
            return "Usuário não encontrado."
        Usuarios.db[self.idusuario] = {
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'usuario': self.usuario,
            'senha': self.senha
        }
        return "Usuário atualizado com sucesso."

    def deleteUser(self):
        if self.idusuario not in Usuarios.db:
            return "Usuário não encontrado."
        del Usuarios.db[self.idusuario]
        return "Usuário excluído com sucesso."

    def selectUser(self, idusuario):
        if idusuario not in Usuarios.db:
            return "Usuário não encontrado."
        user = Usuarios.db[idusuario]
        self.idusuario = idusuario
        self.nome = user['nome']
        self.telefone = user['telefone']
        self.email = user['email']
        self.usuario = user['usuario']
        self.senha = user['senha']
        return "Usuário encontrado."


class Usuarios:
    def _init_(self, master=None):
        self.fonte = ("Verdana", "8")
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        self.container1 = Frame(self.master, pady=10)
        self.container1.pack()
        self.container2 = Frame(self.master, padx=20, pady=5)
        self.container2.pack()
        self.container3 = Frame(self.master, padx=20, pady=5)
        self.container3.pack()
        self.container4 = Frame(self.master, padx=20, pady=5)
        self.container4.pack()
        self.container5 = Frame(self.master, padx=20, pady=5)
        self.container5.pack()
        self.container6 = Frame(self.master, padx=20, pady=5)
        self.container6.pack()
        self.container7 = Frame(self.master, padx=20, pady=5)
        self.container7.pack()
        self.container8 = Frame(self.master, padx=20, pady=10)
        self.container8.pack()
        self.container9 = Frame(self.master, pady=15)
        self.container9.pack()


        self.create_label_entry(self.container1, "Informe os dados :", font=("Calibri", "9", "bold"))

        self.lblidusuario, self.txtidusuario = self.create_label_entry(self.container2, "idUsuario:", width=10)
        self.btnBuscar = self.create_button(self.container2, "Buscar", self.buscarUsuario)

        self.lblnome, self.txtnome = self.create_label_entry(self.container3, "Nome:", width=25)
        self.lbltelefone, self.txttelefone = self.create_label_entry(self.container4, "Telefone:", width=25)
        self.lblemail, self.txtemail = self.create_label_entry(self.container5, "E-mail:", width=25)
        self.lblusuario, self.txtusuario = self.create_label_entry(self.container6, "Usuário:", width=25)
        self.lblsenha, self.txtsenha = self.create_label_entry(self.container7, "Senha:", width=25, show="*")
        self.bntInsert = self.create_button(self.container8, "Inserir", self.inserirUsuario)
        self.bntAlterar = self.create_button(self.container8, "Alterar", self.alterarUsuario)
        self.bntExcluir = self.create_button(self.container8, "Excluir", self.excluirUsuario)
        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

    def create_label_entry(self, parent, label_text, width=None, show=None, font=None):
        label = Label(parent, text=label_text, font=font or self.fonte, width=width)
        label.pack(side=LEFT)
        entry = Entry(parent, width=width, font=self.fonte)
        if show:
            entry.config(show=show)
        entry.pack(side=LEFT)
        return label, entry

    def create_button(self, parent, text, command):
        button = Button(parent, text=text, font=self.fonte, width=12, command=command)
        button.pack(side=LEFT)
        return button

    def inserirUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.insertUser()
        self.clear_entries()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.updateUser()
        self.clear_entries()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.clear_entries()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        msg = user.selectUser(idusuario)
        self.lblmsg["text"] = msg
        if msg == "Usuário encontrado.":
            self.fill_entries(user)
        else:
            self.clear_entries()

    def clear_entries(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def fill_entries(self, user):
        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)


root = Tk()
Usuarios(root)
root.mainloop()



