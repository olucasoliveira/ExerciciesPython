frase=str(input("ESCREVA UMA FRASE:")).strip().lower().replace(" ","")

if frase == frase[::-1]:
    print(" É UM PALINDROMO")
else:
    print("NÃo É UM PALINDROMO")