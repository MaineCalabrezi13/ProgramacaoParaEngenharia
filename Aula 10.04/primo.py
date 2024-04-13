#Elabore um programa que leia um número inteiro e indique se o número é primo ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele mesmo. No entanto, o número 1 não é primo.

numero = int(input("Digite um número inteiro: "))
dividir = 0
for i in range(2, numero):
    if numero % i == 0:
        dividir += 1

if dividir == 1:
    print("É primo")
else:
    print("Não é primo")