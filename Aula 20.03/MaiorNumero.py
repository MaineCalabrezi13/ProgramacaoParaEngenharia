#Desenvolva um script que solicite dois números quaisquer e mostre o maior entre  eles.
n1 = int(input("Digite valor 1: "))
n2 = int(input("Digite valor 2: "))

if n1>n2:
    print("O maior número é o: ",n1)
elif n2>n1:
    print("O maior número é o: ", n2)
else :
    print("Números iguais!")