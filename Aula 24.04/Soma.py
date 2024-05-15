#Faça um Programa Python que leia uma lista de 5 números inteiros, mostre a soma dos elementos da lista.

soma=[]
for i in range(0,5):
    num = int(input("Digite números inteiros: "))
    soma.append(num)
print("A soma é: ",sum(soma))