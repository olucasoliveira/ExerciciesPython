valor= int(input("Quer ver a tabuada de qual valor ? "))
c = 0
while True:
    while c <10:
        c+=1
        print(f"{valor} X {c} = {valor * c}")
    c += -10
    valor = int(input("Quer ver a tabuada de qual valor ? "))
    if valor < 0:
        break