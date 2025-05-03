login = ["user0","user1","user2","user3","user4",]
senha = ["senha0","senha1","senha2","senha3","senha4",]

tempLogin= input("Digite seu nome de usuário: ")

if tempLogin in login:
    for index, dataColect in enumerate(login):
        if tempLogin==dataColect:
            tempSenha= input(f"Olá {tempLogin}, Digite sua senha: ")
            if tempSenha==senha[index]:
                print(f"Bem vindo, {login[index]}. Login efetuado com sucesso")
            else:
                print("Senha inválida")
else:
    print("Usuário não encontrado")

