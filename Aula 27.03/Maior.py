#Escolha do maior número de dois números distintos
n1 = float(input("Digite valor do número 1: "))
n2 = float(input("Digite valor do número 2: "))

if n1>n2:
    print("O maior número é: ",n1)
elif n2>n1:
    print("O maior número é: ",n2)
else:
    print("Iguais")
