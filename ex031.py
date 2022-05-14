km=int(input("Qual a distancia em KM: "))
c1=km*0.5
c2=km*0.45
if km < 200:
    print("O valor da sua viagem sera de R${}, com a taxa de R$0,50/KM".format(c1))
else:
    print("O valor da sua viagem sera de R${}, com a taxa de R$0,45/KM".format(c2))