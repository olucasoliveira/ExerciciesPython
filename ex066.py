x = c= 0

while x != 999:
    s =int(input("Digite um numero ( 999 para parar) : "))
    if s == 999:
        break
    x += s
    c +=1
print(f"A soma dos {c} valores foi {x}")