import datetime
ano= int(input("Digite o ano do seu nascimento:"))

idade = (datetime.date.today().year ) - ano

if idade == 18:
    print("Voce precisa se alistar ate julho, é o seu ano ")

elif idade< 18:
    print("Sua hora vai chegar guerreirso, falta {} ano(s)".format(18-idade))

else:
    print("Já passou da hora pangaré, voce deveria estar alistado há {} ano(s)".format(idade-18))

