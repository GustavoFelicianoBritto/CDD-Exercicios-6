notas=[""]*5
soma=0
contador=0
for i in range(len(notas)):
    notas[i]=float(input(f"Digite a {i+1} nota: ").replace(',','.'))

for j in range(len(notas)):
    soma += notas[i]

media = soma/ len(notas)
for k in range(len(notas)):
    if notas[i]>media:
        contador+=1

print(f"A média da turma foi: {media:.1f}, e tivemos {contador} alunos com nota superior a média")




