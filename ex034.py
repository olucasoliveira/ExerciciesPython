sal=int(input("Digite seu salario: "))
c1=sal*1.1
c2=sal*1.15
if sal >= 1250:
    print("Seu salario novo: {}".format(c1))
else:
    print("Seu salario novo é: {}".format(c2))
