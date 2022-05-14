import random
from time import sleep

computador = random.randint(0, 5)

usuario=int(input("Qual numero eu pensei ? "))

print("----"*9)

print("PROCESSANDO...")

sleep(3)
if usuario == computador:
    print("Parabens voce acertou!")

else:
    print("Você errou, tente novamente")



