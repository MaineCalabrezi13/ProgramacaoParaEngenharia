VelocidadeMaxima = float(input("Digite a velocidade máxima permitida na rodovia: "))
VelocidadeDirigida = float(input("Digite a velocidade dirigida na rodovia: "))

if (VelocidadeDirigida>=(VelocidadeMaxima+31)):
    print("Tipo da Multa: Grave - Penalidade de 7 pontos")
    print("Valor da Multa R$ 574,62")
elif (VelocidadeDirigida>=(VelocidadeMaxima+11))and(VelocidadeDirigida<=(VelocidadeMaxima+30)):
    print("Tipo de Multa: Média - Penalidade de 5 pontos")
    print("Valor da Multa R$ 127,69")
elif (VelocidadeDirigida>=VelocidadeMaxima)and(VelocidadeDirigida<=(VelocidadeMaxima+10)):
    print("Tipo de Multa: Leve - Penalidade de 3 pontos")
    print("Valor da Mula R$ 85,13")
else:
    print("Velocidade normal")