from datetime import date
import time
ano=int(input("Escolha um ano:"))

print("ANALISANDO...")
time.sleep(2)
if  ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano %400 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")
