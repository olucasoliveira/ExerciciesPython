s=0
for c in range(1, 7):
    numeros=int(input("DIGITE UM NUMERO:"))
    if numeros % 2 == 0:
        s += numeros

print(" A SOMATORIA DOS NUMEROS PARES DIGITADO É: {}".format(s))