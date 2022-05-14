n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
n3=int(input("Digite o ultimo numero"))
lista=[n1, n2, n3]
x=sorted(lista)
print("Esse numero é o menor {}".format(x[0]))
print("Esse numero é o maior {}".format(x[2]))


