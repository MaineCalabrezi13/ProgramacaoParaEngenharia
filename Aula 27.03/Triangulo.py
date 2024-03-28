#Desenvolva um script em linguagem Python que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formar um triângulo. 
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else: 
    print("Não é um triângulo")