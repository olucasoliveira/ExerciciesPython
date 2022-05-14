from random import randint

print("""
=========================
 VAMOS JOGAR PAR E IMPAR
=========================""")


x= 0
while True:
    n = randint(1, 10)
    print(n)
    valor = int(input("DIGITE UM VALOR: "))
    tipo = str(input("PAR OU ÍMPAR? [P/I]: "))
    if tipo in "Pp":
        if (valor + n ) % 2 == 0:
            print("Você ganhou essa partida")
            x+=1
        else:
            print("Você perdeu essa partida")
            print(f"VOCÊ GANHOU {X} VEZES")
            break
    elif tipo in "Ii":
        if (valor + n) % 2 == 1:
            print("Você ganhou essa partida")
            x+=1
        else:
            print("Você perdeu essa partida")
            print(f"VOCÊ GANHOU {X} VEZES")
            break
