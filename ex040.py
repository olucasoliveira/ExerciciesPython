n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
media= (n1 + n2 )/2

if media < 5.0 :
    print("REPROVADO COM MEDIA {:.1f}".format(media))

elif media >= 5.0 and media <= 6.9 :
    print("RECUPERAÇÃO COM MEDIA {:.1f}".format(media))

else:
    print("APROVADO COM MEDIA {:.1f}".format(media))
