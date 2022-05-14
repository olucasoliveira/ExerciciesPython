import random
from time   import sleep

print("{:^58}".format("\033[7;;40mJOGO DA VELHA\033[m"))

print(("=-="*19)) #Linha para separar

#usuario escolhe uma opcçao
usuario=str(input("PEDRA, PAPEL OU TESOURA ? :")).upper().strip()


print("Otimo, você escolheu:", usuario )
print(("=-="*19)) #linha para separar

#gerando um opção do computador

opcoes=["PEDRA", "PAPEL", "TESOURA"]
computador= random.choice(opcoes)

print("\033[4;35mPROCESSANDO...\033[m")

# Tempo de supense
sleep(2)

print("O computador fez {}".format(computador))


print(("=-="*19)) #Linha para separar

#combinaçoes de jogo

if computador == usuario :
    print("OUVE UM EMPATE")

elif computador == "PEDRA" and usuario == "TESOURA" or computador== "PAPEL" and usuario== "PEDRA"  or computador== "TESOURA" and usuario =="PAPEL":
    print("\033[1;31;40mVOCE PERDEU, TENTE NOVAMENTE !!!\033[m")

else:
    print("\033[1;32;40mPARABENS, VOCE VENCEU A PARTIDA!!!\033[m")


print(("=-="*19)) #Linha para separar


