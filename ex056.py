f = 0
maioridadehomem= 0
nomevelho= ""
totmulheres= 0

for dados in range(1, 5):
    print("========== {}° PESSOA ========".format(dados))
    nome=str(input("Nome: ")).strip()
    idade= int(input("Idade: "))
    sexo= str(input("Sexo [H/M]: ")).strip()
    f  += idade

    if dados == 1 and sexo == "Hh":
        maioridadehomem = idade
        nomevelho= nome
    if idade > maioridadehomem and sexo in "Hh":
        maioridadehomem = idade
        nomevelho= nome
    if idade < 20 and sexo in "Mm":
        totmulheres+= 1





print("================RESULTADOS================")
print("A Media de idade do grupo é {}".format(f/4))
print("A idade do mais velho é {}, e seu nome é {}".format(maioridadehomem, nomevelho))
print("{} mulheres tem menos de 20 anos ".format(totmulheres))