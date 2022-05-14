import random

A1 = input("Qual o nome do primeiro aluno ?")
A2 = input("Qual o nome do segundo aluno ?")
A3 = input("Qual o nome do terceiro aluno ?")
A4 = input("Qual o nome do quarto aluno ?")
lista= [A1, A2, A3, A4]
C = random.choice(lista)
print("O sorteado foi o aluno {}".format(C))
