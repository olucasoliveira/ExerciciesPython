numero= int(input("DIGITE UM NUMERO: "))
a=1
b=numero
lista=[numero]
menu=str(input('QUER CONTINUAR ?[S/N]'))
while menu in "Ss":
    numero = int(input("DIGITE UM NUMERO: "))
    a+= 1
    b+=numero
    lista.append(numero)
    menu = str(input('QUER CONTINUAR ?[S/N]'))

print("Você encerrou o programa")
print("A media entre todos os numerros digitados é {}".format(b/a))
print("A maior numero digitado foi {}, e o menor foi {}".format(max(lista), min(lista)))
