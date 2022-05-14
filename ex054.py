from datetime import date
f= 0
f1= 0
for c in range (1, 7):

    nasc=int(input(("QUAL O SEU ANO DE NASCIMENTO ?")))

    if date.today().year - nasc > 18 :
        f += 1
    else:
        f1 += 1
print("{} pessoas são maiores de idade".format(f))
print("{} pessoas são menores de idade ".format(f1))