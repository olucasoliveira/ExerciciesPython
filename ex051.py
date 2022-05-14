termo=int(input("DIGITE O PRIMEIRO TERMO:"))
razao=float(input("DIGITE UMA RAZÃO:"))

for c in range(1, 11):
     print("O TERMO {} DESSA PROGRESSÃO CORRESPONDE AO VALOR {} ".format(c, (termo+(c-1)*razao)))
