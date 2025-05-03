nomes=[]
auxNomes=4

for i in range(5):
    nomes.append(input(f"Digite o {i+1} nome: "))

print(nomes)
invNomes=[""]*len(nomes)

for j in range(len(nomes)):
    invNomes[j]=nomes[auxNomes]
    auxNomes-=1
    print(invNomes[j])



