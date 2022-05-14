termo1= int(input("DIGITE O VALOR PRIMEIRO TERMO DA PA: "))
razao=int(input('DIGITE A RAZÃO DESSA PA: '))
n = 1
total= 0
mais = 10
while mais != 0:
    total += mais
    while n <= total:
        print(" {} -> ".format( (termo1 +((n-1)*razao ))), end="")
        n+=1
    print("PAUSA")
    mais = int(input("Quer somar mais quantos termos?" ))
print("Obrigado por usar nosso sistema")






