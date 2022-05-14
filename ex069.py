x= h= m=0
while True:
    idade= int(input("QUAL A SUA IDADE ?  "))
    sexo= str(input("QUAL SEU SEXO ? [F/M]: "))
    if sexo != "MmFf":
        sexo = str(input("QUAL SEU SEXO ? [F/M]: "))
    ask= str(input("QUER CONTINUAR ? [S/N]: "))
    if ask in "Ss":
        if idade > 18:
            x+=1
        if sexo in "Mm":
            h+=1
        if sexo in "fF" and idade < 20:
            m+=1
    else:
        break
print(f"""=================================
                    RESULTADOS
         ==================================
         {x} PESSOAS TEM MAIS DE 18 ANOS
         {h} HOMENS FORAM CADASTRADOS
         {m} MULHERES TEM MENOS DE 20 ANOS""")