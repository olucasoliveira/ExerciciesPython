from math import factorial
numero= int(input("Digite um número para calcular o fatorial: "))
x = numero
while x >= 1:
    print(x, end="")
    print(" x " if x > 1  else " = ", end="")

    x += -1
print("{}".format(factorial(numero)))