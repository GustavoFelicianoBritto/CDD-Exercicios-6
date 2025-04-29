nomes=["gustavo","victor","sol","andresa","joão"]

nome=input("Digite o nome em questão: ").lower()

for i in range(len(nomes)):
    if nome == nomes[i]:
        print(f"Nome: {nome} encontrado na posição {i}")
    else:
        print("Nome não encontrado")