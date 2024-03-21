#Crie um programa que peça um valor e imprima na tela se o valor é positivo, negativo ou ainda igual a zero

valor = int(input("Digite valor: "))

if valor <0 :
    print("O valor é negativo")
elif valor>0:
    print("O valor é positivo")
else:
    print("Valor igual a 0")