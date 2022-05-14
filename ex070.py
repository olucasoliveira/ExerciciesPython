x=0
y=0
while True:
    nome=str(input("DIGITE O NOME DO PRODUTO: "))
    preco=int(input("DIGITE O PREÇO: R$ "))
    ask=str(input('QUER CONTINUAR ? [S/N]: '))
    x += preco
    if ask in "Ss":
        if preco > 1000:
            y+=1
    else:
        break
print(f"""=================================
                    RESULTADOS
         ==================================
          R$ {x} FORAM GASTOS NA COMPRA
          {y} PRODUTOS SÃO MAIS QUE 1000 REAIS""")