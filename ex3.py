nomes=["gustavo","victor","sol","andresa","joão"]
msg=""
nome=input("Digite o nome em questão: ").lower()

for i in range(len(nomes)):
    if nome == nomes[i]:
        msg=f"Nome {nome} encontrado na posição {i}"
        break
    else:
        msg="Nome não encontrado"

print(msg)
