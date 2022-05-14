import time

print("VAMOS CALCULAR SEU IMC ?")

altura=str(input("Me diga sua altura:")).replace(",", ".")
peso= float(input("Me diga seu peso:"))

print("\033[0;36;40mCALCULANDO...\033[m")

time.sleep(1)

imc= peso/(float(altura)**2)

if imc < 18.0:
    print("ABAIXO DO PESO")

elif imc > 18.5 and imc <= 25:
    print("VOCE ESTA NO SEU PESO IDEAL  ")

elif imc > 25 and imc <= 30 :
    print("SOBREPESO")

elif imc > 30 and imc <=40 :
    print("OBESIDADE")

else:
    print("OBESIDADE MORBIDA ")
