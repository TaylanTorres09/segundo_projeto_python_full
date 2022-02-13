from controller import CadastroController, LoginController

while True:
    entrada = int(input("Digite 1 para cadastrar, 2 para fazer login e 0 para sair: "))
    if entrada == 0:
        break
    while entrada != 1 and entrada != 2:
        entrada = int(input("Digite 1 para cadastrar e 2 para fazer login: "))
    
    if entrada == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite um e-mail válido: ")
        print("Sua senha deve seguir as seguintes regras:")
        print(''' Os alfabetos devem estar entre [az]; \n Pelo menos um alfabeto deve ser maiúsculo [AZ];
        Pelo menos 1 número ou dígito entre [0-9]; \n Pelo menos 1 caractere de [_ ou @ ou $]; \n'''.strip("\t"))
        senha = input("Digite sua senha: ")
        cadastro = CadastroController(nome, email, senha)
        print(cadastro.cadastro())

    if entrada == 2:
        email = input("Digite um e-mail válido: ")
        senha = input("Digite sua senha: ")
        print(LoginController.login(email, senha))
    

