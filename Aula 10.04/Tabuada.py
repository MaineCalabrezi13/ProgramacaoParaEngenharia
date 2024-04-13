#Escrever um programa que imprima a tabuada de um número informado pelo usuário.

valor = int(input("Digite número: "))

for i in range(0,11):
    tabuada = valor*i
    print(valor,"X" , i ,"=",tabuada)



