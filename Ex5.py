A=[8.0,7.0,8.5,9.0,7.5]
M=[""]*len(A)

num=int(input("Digite o valor para multiplicar: "))

for i in range(len(A)):
    M[i]=A[i]*num

print(f"{A}\n*\n{num}\n=\n{M}")