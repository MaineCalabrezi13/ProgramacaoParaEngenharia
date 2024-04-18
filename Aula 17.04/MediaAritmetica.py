#Crie um programa em linguagem Python que leia 5 números, calcule e mostre a média aritmética dos valores lidos.
soma=0
for i in range(0,5):
    num=int(input("Digite um número: "))
    soma +=num
Media = soma/i
print("O resultado é: ",Media)