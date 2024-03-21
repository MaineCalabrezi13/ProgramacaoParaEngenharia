#Crie um programa em Python para calcular a média de três notas inseridas pelo usuário e dar feedback baseado na média calculada.

import math
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3= float(input("Digite nota 3: "))

media= (nota1+nota2+nota3)/3

print("Sua média é: ""{:.2f}".format(media))

if media>=7 :
    print("Parabéns, sua média é alta")
elif media>=5: 
    print("Sua média é razoavel")
elif media<5:
    print("Sua média é baixa. É uma boa oportunidade para melhorar")
    