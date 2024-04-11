#Escrever um programa que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos.

soma=0
for i in range(0,10):
    Num = int(input("Digite um número: "))
    soma += Num
print(soma)
    