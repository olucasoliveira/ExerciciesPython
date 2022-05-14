frase= str(input("Digite uma string: ")).upper().strip()


print("Na frase existem {} letras A".format(frase.count("A")))
print("A primeira aparece na posição {}".format(frase.find("A")+1))
print("A ultima aparece na posição {}".format(frase.rfind("A")))