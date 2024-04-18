#Faça um script em Python par ler o nome e  idade de 10 pessoas e  verificar total de pessoas maior e total menor de idade.
maior = 0
menor =0 
for i in range(1,11):
    nome=input("Digite seu nome: ")
    idade=int(input("DIgite sua idade: "))

    if (idade>=18):
        maior = maior +1
    else:
        menor = menor+1
print("A quantidade de pessoas maiores de idade é: ",maior,"\nA quantidade de pessoas menores de idade: ",menor)