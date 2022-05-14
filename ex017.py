import math
CA=float(input("Qual o cateto adjacente ?"))
CO=float(input("qual o cateto oposto?"))
HP=math.hypot(CA, CO)
print("A hipotenusa desse triangulo é {:.2f}".format(HP))
