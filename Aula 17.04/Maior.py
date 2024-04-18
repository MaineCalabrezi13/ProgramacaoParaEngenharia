#Desenvolva um script Python que leia 10 números e informe o maior e menor número lido.
maior=0
menor=9999
for i in range(1,11):
    Num = int(input("Digite um número: "))
    if maior<Num:
        maior=Num
    if menor>Num:
        menor=Num
print("O maior número: ",maior)
print("O menor número: ",menor)

