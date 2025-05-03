valores=[]
pares=[]
menor=float('inf')
maior=float('-inf')
soma=0
rep=10
maiorCont=0

for i in range(rep):
    valor=int(input(f"Digite o {i+1}º valor: ") or 10)
    valores.append(valor)
    soma+=valor

media= soma/rep

for valorAtual in valores:
    if valorAtual%2==0:
        pares.append(valorAtual)
    if valorAtual < menor:
        menor = valorAtual
    if valorAtual > maior:
        maior = valorAtual
    if valorAtual>media:
        maiorCont+=1

print(f"Números pares inseridos:",end=" ")
for k in range(len(pares)):
    print(pares[k],end=" ")
print()
print(f"O maior valor inserido foi: {maior}\n"
      f"O menor valor inserido foi: {menor}\n"
      f"a média dos números foi: {media} e tivemos {maiorCont} numeros inseridos maiores que a média.")





