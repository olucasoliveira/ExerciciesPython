termo1= int(input("DIGITE O PRIMEIRO TERMO DA PA: "))
razao=int(input('DIGITE A RAZÃO DESSA PA: '))
n = 1
while n <= 10:
    print("O correspondente  {} equivale ao valor {} dessa PA ".format(n, (termo1 +((n-1)*razao ))))
    n+=1

print("FIM")