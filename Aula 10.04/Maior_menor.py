#Escreva um programa que leia 10 valores inteiros e encontre o maior e o menor deles.

maior=0
menor=999
soma=0
for i in range(0,10):
    Num = int(input("Digite um número: "))
    if maior<Num:
        maior=Num
    if menor>Num:
        menor=Num
print("O maior número: ",maior)
print("O menor número: ",menor)