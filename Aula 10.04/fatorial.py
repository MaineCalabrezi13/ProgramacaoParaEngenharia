#Escreva um programa que lido um número, calcule e informe o seu fatorial. 

num = int(input("Digite um número: "))
fator = num
for i in range(num - 1, 1, -1):
    fator = fator * i
print(fator)

