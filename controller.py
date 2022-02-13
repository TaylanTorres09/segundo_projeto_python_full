import re
import bcrypt
from model import Client
from dao import RetornaSession

engine, session = RetornaSession.retornaSession()

class CadastroController:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def checar_dados_cadastro(self):
        # Checar nome
        if len(self.nome) <= 4:
            return "Nome deve conter no mínimo 5 characteres"

        # Checar e-mail
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(not re.search(regex,self.email)):
            return "E-mail inválido"

        # senha
        flag = 0
        while True:   
            if (len(self.senha)<8): 
                flag = -1
                break
            elif not re.search("[a-z]", self.senha): 
                flag = -1
                break
            elif not re.search("[A-Z]", self.senha): 
                flag = -1
                break
            elif not re.search("[0-9]", self.senha): 
                flag = -1
                break
            elif not re.search("[_@$]", self.senha): 
                flag = -1
                break
            elif re.search("\s", self.senha): 
                flag = -1
                break
            else: 
                flag = 0
                break
        
        if flag ==-1: 
            return "Senha inválida" 

    def cadastro(self):
        checar = self.checar_dados_cadastro()
        if checar == "Senha inválida" or checar == "E-mail inválido" or checar == "Nome deve conter no mínimo 5 characteres":
            return checar
        listar = session.query(Client).filter(Client.email == self.email).all()
        if len(listar) > 0:
            return f"Pessoa com o email {self.email} já existe"
        else:
            try:
                encript = bcrypt.hashpw(self.senha.encode('utf8'), bcrypt.gensalt(10))
                x = Client(nome=self.nome, email=self.email, senha=encript)
                session.add(x)
                session.commit()
                return "Cadastro feito com sucesso"
            except Exception as e:
                return e

class LoginController:
    @classmethod
    def login(cls, email, senha):
        login_user = session.query(Client).filter(Client.email == email).all()
        if len(login_user) > 0:
            if bcrypt.checkpw(senha.encode('utf8'), login_user[0].senha.encode('utf8')):
                return "Bem vindo ao nosso sistema."
            else:
                return "Digite a senha correta"
        return "Digite o e-mail correto"
