nomes=[""]*5
for i in range(len(nomes)):
    nomes[i]= input("insira o nomes:")
    
for i,j  in enumerate(nomes):
    print(f"{i} - {j}")


for k in range(len(nomes)):
    print(f"{nomes[k]}, {k}")


