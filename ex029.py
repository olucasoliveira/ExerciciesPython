
vel=float(input("Digite a Velocidade do veiculo: "))
p= vel-80
if vel<= 80:
    print("Velocidade permitida")
else:
    print("Você foi multado em R${}".format(p*7))

print("Atenção no transito")