sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0]

while sexo not in  "MmFf":
    print("Opção invalida")
    sexo = str(input("Informe o seu sexo [M/F]: ")).upper()

print("Obrigado por informar")