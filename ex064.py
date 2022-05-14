print("Digite 999 para encerrar o programa")
x= 1
numero=int(input("DIGITE UM NUMERO:"))
f= numero
while numero != 999:
    numero=int(input("DIGITE UM NUMERO: "))
    f += numero
    x += 1

print("Em {} tentativas ".format(x))
print("A soma das tentativas é {}".format(f-999))