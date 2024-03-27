VelocidadeMaxima = float(input("Digite a velocidade máxima permitida na rodovia: "))
VelocidadeDirigida = float(input("Digite a velocidade dirigida na rodovia: "))

Velocidade = VelocidadeDirigida - VelocidadeMaxima
if VelocidadeDirigida==VelocidadeMaxima:
    print("Velocidade Permitida!")
elif (Velocidade <=10):
    print("O valor da multa é igual a: 85,13 /n Tipo de multa: Leve /n Pontos: 3")
elif (Velocidade>=12)and(Velocidade<=30):
     print("O valor da multa é igual a: 127,60 /n Tipo de multa: Media /n Pontos: 5")
elif(Velocidade>=31):
     print("O valor da multa é igual a: 574.62 /n Tipo de multa: Gravissima /n Pontos: 7")