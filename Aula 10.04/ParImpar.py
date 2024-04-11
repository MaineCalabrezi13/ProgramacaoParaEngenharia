#Para construir o programa a seguir, considere que os usuários só informarão números inteiros positivos. Crie um programa que receba 10 números digitados e exiba todos os números pares e ímpares.
i = 1
soma = 0
while i<=10:
    num=int(input("Digite número: "))
    if num<0:
        break
    if num %2==0:
        print(num,"PAR ")
    else:
        print(num,"IMPAR")
    i=i+1
    