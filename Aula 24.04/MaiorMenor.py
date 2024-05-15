#Faça um Programa Python que leia uma lista com 10 números inteiros, calcule e mostre o maior e menor elemento da lista.

num=[]
for i in range(0,5):
    numero = int(input("Digite numero: "))
    num.append(numero)

print("O maior valor é: ",max(num),"\nO menor valor é: ",min(num))