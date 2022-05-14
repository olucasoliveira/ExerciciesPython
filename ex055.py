
lista = []
for c in range(0, 5):
    peso = input("Qual é seu peso ?")
    lista.append(peso)

esse = sorted(lista)


print("Esse é o maior: {}".format(esse[4]))
print("Esse é o menor peso: {}".format(esse[0]))
