list=[]
indexFind=[]
cont=0
pos=0

for i in range(10):
    list.append(int(input(f"Digite o {i+1}º valor: ")))

num = int(input("Digite um número para verificar: "))

for index,i in enumerate(list):
    if num == list[pos]:
        indexFind.append(index)
        cont+=1
    pos+=1

if len(indexFind)>0:
    print(f"Numero {num} encontrado nas posições:", end=" ")
    for j in range(len(indexFind)):
        print(indexFind[j]+1,end=" ")
    print()
    print(f"o número {num} foi encontrado {cont} vezes na lista")
else:
    print("número não foi encontrado na lista")
