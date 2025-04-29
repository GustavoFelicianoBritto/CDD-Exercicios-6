arrayVerdura = ["sim","Tomate","cebola","legumes","notebook"]

"""for i in arrayVerdura:
    print(f"{i}", end=" ")
"""
arrayVerdura.append("Feijão")
arrayVerdura.insert(0,"gato")

for j in range(len(arrayVerdura)):
    print(arrayVerdura[j])

verduraA=arrayVerdura.pop(0)
print()
print(verduraA)



