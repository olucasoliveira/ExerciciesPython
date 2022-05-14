
cidade= str(input("Digite o nome da sua cidade: "))


pcidade= cidade.strip() #tira os espaços
fim=pcidade.upper()
esse=fim.split() #lista


print("Sua cidade começa com o nome Santo ? {}".format("SANTO" in esse[0]))


