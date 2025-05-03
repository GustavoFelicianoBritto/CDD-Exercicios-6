firstList= [""] * 5
secondList= [""] * 5
cont=4

for i in range(len(firstList)):
    firstList[i]=int(input("Digite o valor: "))

for j in firstList:
    secondList[cont]=j
    cont-=1

print(secondList)