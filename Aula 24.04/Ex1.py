#Desenvolva um script em linguagem Python com uma lista vazia. Em seguida, leia e insira 5 valores inteiros na lista. Ao final mostre na tela, os valores contidos na lista. Ordem de entrada e inversa.
numeros = []

for contador in range(0,5):
    valor = input("Insira um numero inteiro: ") 
    numeros.append(valor)

print ("Lista de numeros digitados : ",numeros)
