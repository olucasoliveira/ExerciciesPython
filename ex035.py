l1=int(input("Digite uma reta:"))
l2=int(input("Digite uma reta:"))
l3=int(input("Digite uma reta:"))

lista=[l1, l2, l3]
ordem=sorted(lista)

c1=ordem[0]+ ordem[1]
c2=ordem[1]+ordem[2]
c3= ordem[0] + ordem [2]

if c1 > ordem[2] and c2 > ordem[0] and c3 > ordem[1]:
    print("Forma um triangulo")

else:
    print("Não forma um triangulo")

print(ordem)