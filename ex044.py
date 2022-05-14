
valor=int(input("Qual o valor do produto ? "))
pagamento=int(input("""SUAS OPÇÕES SÃO: 
                     [1]CHEQUE 
                     [2]DINHEIRO 
                     [3]CARTÃO
                     -  Qual o modo de pagamento?"""))

if pagamento == 3:
    vezes=int(input("""VAI PARCELAR EM QUANTAS VEZES?
                    [0] À VISTA
                    [2] DUAS VEZES
                    [3] TRES VEZES OU MAIS
                    - Escolha um opção:"""))

    if vezes == 0 :
        print("O VALOR A SER PAGO É R${}".format(valor * 0.95))

    elif vezes == 2:
        print("O VALOR A SER PAGO É DE R${}".format(valor))

    elif vezes >= 3:
        print("O VALOR A SER PAGO É DE R${}".format(valor*1.2))

else:
    print("O VALOR A SER PAGO É R${}".format(valor * 0.9))





