#Faça um script em Python que receba dois números e gere os números que estão no intervalo compreendido por eles. Mostre no final a soma dos números.

soma=0
n1 = int(input("Digite número 1: "))
n2 = int(input("Digite número 2: "))
result = "Os números do intervalo são: "
for i in range(n1+1,n2):
    if (i == n1 + 1):
        result = result + str(i)
    else:
        result = result + "," + str(i)
    soma+=i
print(result)
print("A soma desses números é: ",soma)