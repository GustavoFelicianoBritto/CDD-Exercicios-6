notas=[""]*5
soma=0
maiormedia=0

for i in range(len(notas)):
    notas[i]=float(input(f"Digite a {i+1} nota: ").replace(',','.'))
    soma += notas[i]

media = soma/ len(notas)

for i in range(len(notas)):
    if notas[i]>media:
        maiormedia+=1

print(f"A média da turma foi: {media:.1f}, e tivemos {maiormedia} alunos com nota superior a média")




