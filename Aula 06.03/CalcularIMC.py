#Faça um algoritmo que receba como entrada os dados de uma pessoa: Nome, idade, peso e altura. Após, calcule o seu IMC – Índice de Massa Corporal utilizando a formula: 

nome = input("Digite nome: ")
idade = int(input("Digite idade: "))
peso = float(input("DIgite peso: "))
altura = float(input("Digite altura: "))

imc =peso/(altura*altura)

print("")
print("##############")
print("O IMC é: ", imc)