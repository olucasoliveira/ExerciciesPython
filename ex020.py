
import random

A1 = input("Qual o nome do primeiro aluno ?")
A2 = input("Qual o nome do segundo aluno ?")
A3 = input("Qual o nome do terceiro aluno ?")
A4 = input("Qual o nome do quarto aluno ?")
Lista= [A1, A2, A3, A4]
random.shuffle(Lista)
print(Lista)