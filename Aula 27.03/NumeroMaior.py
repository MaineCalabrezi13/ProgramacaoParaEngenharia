#Elabore um script em linguagem Python que leia três números e mostre o maior deles.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

maior_numero = max(n1, n2, n3)
print("O maior número é:", maior_numero)