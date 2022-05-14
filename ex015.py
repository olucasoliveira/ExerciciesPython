D = int(input("Por quantos dias o carro foi utilizado?"))
KM = float(input("Qual a kilometragem rodada durante o percurso ?"))
P = D*60 + KM*0.15
print("O preço da vigem no qual durou {} dias e foram percorridos {} KM é de RS{:.2f}".format(D, KM, P))
