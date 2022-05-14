casa=int(input("Qual o valor da casa? R$"))
salario=int(input("Qual o seu salario? R$"))
tempo=int(input("Em quantos anos pretende pagar ?"))
prestacao = casa / ( 12 *tempo )

if  prestacao > 0.3 * salario:
    print("Voçe não tem direito  ao emprestimo")
else :
    print("Parabens, emprestimo aceito, o valor da prestação será de R${:.3f}/Mensais ".format(prestacao))
