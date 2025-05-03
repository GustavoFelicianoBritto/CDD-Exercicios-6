nSize= int(input("Digite o tamanho dos vetores: ") or 5)

aList=[""]*nSize
bList=[""]*nSize
soma=[""]*nSize

for i in range(len(aList)):
    aList[i]=int(input(f"Digite o {i+1} valor A: ") or 2)
    bList[i]=int(input(f"Digite o {i+1} valor B: ") or 2)

for j in range(len(aList)):
    soma[j]=aList[j]+bList[j]


print(f"{aList}\n+\n{bList}\n=\n{soma}")
