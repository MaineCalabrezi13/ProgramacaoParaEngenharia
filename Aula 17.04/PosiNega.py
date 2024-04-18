#Crie um programa em linguagem Python que leia 5 números, informando a quantidade de valores positivos, a quantidade de valores negativos
negativo=0
positivo = 0
for i in range(0,5):
    numero=int(input("Digite um número: "))

    if(numero>0):
        positivo=positivo+1
    elif(numero<0):
        negativo=negativo+1
print("A quantidade de números positivos é: ",positivo,"\nA quantidade de numeros negativos é: ",negativo)