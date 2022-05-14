print("VAMOS CONSTRUIR UM TRIANGULO")

l1=int(input("PRIMEIRO LADO:"))
l2=int(input("SEGUNDO LADO: "))
l3=int(input("TERCEIRO LADO:"))

triangulo= bool( (l1+l2 > l3) and (l2+l3 > l1) and (l3+l1 > l2))

if l1 == 0 and l2 == 0 and l3 == 0 and triangulo == False:
    print("NÂO FORMA UM TRIANGULO")

elif l1==l2==l3  and triangulo == True:
    print("O TRIANGULO É EQUILATERO")

elif l1== l2 or l2==l3 or l3==l1 and triangulo == True :
    print("O TRIAGULO FORMADO É ISOCELES")

elif l1!=l2!=l3 and triangulo == True:
    print("O TRIANGULO É ESCALENO")

else:
    print("OS LADOS INFORMADOS NÃO FORMAM UM TRIANGULO")
