n1=int(input("Digite um numero:"))
n2=int(input("Digite outro numero:"))

if n1 == n2:
    print("Os dois valores sâo iguais, não existe maior")

elif max(n1, n2) == n1:
    print("O primeiro valor é maior ")

elif max(n1, n2) == n2:
    print(" O valor maior é {}".format(n2))
