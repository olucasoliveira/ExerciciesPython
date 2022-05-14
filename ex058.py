import random
import time
print("======================JOGUINHO======================")

print("GERANDO UM NUMERO ALEATORIO ENTRE 1 E 10...")
time.sleep(3)

numero = random.randint(0, 10)
print(numero, "gerado")

tente= int(input("DIGITE UM NUMERO: "))
f= 1
while tente != numero:
    print("QUE PENA VOCÊ NÃO ACERTOU")
    tente= int(input("DIGITE UM NUMERO NOVAMENTE: "))
    f+=1
print("\033[0;34;40m PARABENS VOCÊ DIGITOU {} E O COMPUTADOR GEROU O {}".format(tente, numero))
print("Voce tentou {} vezes".format(f))