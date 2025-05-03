login = [""]*5
senha = [""]*5

for i in range(len(login)):
    login[i]=input("Digite seu nome de usuário: ") or "user"
    senha[i]=input(f"Olá, {login[i]}. Digite sua nova senha: ") or f"{login[i]}"
print()
for j in range(len(login)):
    print(f"Pos:{j+1} - Login:{login[j]} Senha:{senha[j]}")