#Escrever um algoritmo para ler o nome de uma pessoa e a idade e verificar de é maior ou menor de idade.

nome = input("Digite seu nome: ")
idade = int(input("Digite idade: "))

if idade>=18:
    print("Maior de idade")
else:
    print("Menor de idade")