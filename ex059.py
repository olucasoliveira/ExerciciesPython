valor1= int(input("DIGITE UM NUMERO: "))
valor2= int(input("DIGITE OUTRO VALOR: "))
menu= int(input( """ESCOLHA UMA DAS OPÇÕES:        
                 [1] SOMAR
                 [2] MULTIPLICAR
                 [3] MAIOR
                 [4] NOVOS NUMEROS
                 [5] SAIR DO PROGRAMA
                 DIGITE A OPÇÃO SELECIONADA: """))

while menu != 5:
    if menu== 1:
        print("A soma desses numeros é {}".format(valor1 + valor2))
        menu2= int(input("""ESCOLHA UMA OPÇÃO:
                 [1] VOLTAR AO MENU DE TAREFAS
                 DIGITE A OPÇÃO SELECIONADA: """))
        if menu2 == 1:
            menu = int(input("""ESCOLHA UMA DAS OPÇÕES:        
                             [1] SOMAR
                             [2] MULTIPLICAR
                             [3] MAIOR
                             [4] NOVOS NUMEROS
                             [5] SAIR DO PROGRAMA
                             DIGITE A OPÇÃO SELECIONADA: """))

    if menu == 2:
        print("A multiplicação desses numeros é {}".format(valor1 * valor2))
        menu2 = int(input("""ESCOLHA UMA OPÇÃO:
                         [1] VOLTAR AO MENU DE TAREFAS
                         DIGITE A OPÇÃO SELECIONADA: """))
        if menu2 == 1:
            menu = int(input("""ESCOLHA UMA DAS OPÇÕES:        
                                     [1] SOMAR
                                     [2] MULTIPLICAR
                                     [3] MAIOR
                                     [4] NOVOS NUMEROS
                                     [5] SAIR DO PROGRAMA
                                     DIGITE A OPÇÃO SELECIONADA: """))


    if menu == 3:
        print("O valor valor entre {} e {} é o numero {}".format(valor1, valor2, max(valor1, valor2)))
        menu2 = int(input("""ESCOLHA UMA OPÇÃO:
                         [1] VOLTAR AO MENU DE TAREFAS
                         DIGITE A OPÇÃO SELECIONADA: """))
        if menu2 == 1:
            menu = int(input("""ESCOLHA UMA DAS OPÇÕES:        
                                     [1] SOMAR
                                     [2] MULTIPLICAR
                                     [3] MAIOR
                                     [4] NOVOS NUMEROS
                                     [5] SAIR DO PROGRAMA
                                     DIGITE A OPÇÃO SELECIONADA: """))

    if menu == 4:
        valor1 = int(input("DIGITE UM NUMERO: "))
        valor2 = int(input("DIGITE OUTRO VALOR: "))
        menu = int(input("""ESCOLHA UMA DAS OPÇÕES:        
                         [1] SOMAR
                         [2] MULTIPLICAR
                         [3] MAIOR
                         [4] NOVOS NUMEROS
                         [5] SAIR DO PROGRAMA
                         DIGITE A OPÇÃO SELECIONADA: """))
print("OK, VOCE ENCERROU O PROGRAMA")
