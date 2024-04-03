numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("Número inválido. Por favor, digite um número inteiro positivo maior que 1.")
elif numero == 2 or numero == 3:
    print(numero, "é um número primo.")
elif numero % 2 == 0 or numero % 3 == 0:
    print(numero, "não é um número primo.")
else:
    print(numero, "é um número primo.")