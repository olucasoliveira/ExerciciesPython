nome=input(" Escreva seu nome: ")

 #NOME EM FORMA DE LISTA CADA PALAVRA
pnome= nome.split()

#RETIRANOD OS ESPAÇOS
esse = nome.replace(" ", "")


print("Seu primeiro nome tem {} letras".format(len(pnome[0])))
print("Seu nome é {}".format(esse.upper()))
print("Seu nome é {}".format(esse.lower()))
print("seu nome tem {} letras".format(len(esse)))
