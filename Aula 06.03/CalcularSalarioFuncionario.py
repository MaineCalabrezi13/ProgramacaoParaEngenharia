#Faca um algoritmo que receba como entrada os dados de um funcionário: nome, cargo e salário. Calcule um aumento de 5% sobre o salário. Ao final mostrar o novo salário calculado:

nomeFunc = input("Digite o nome do funcionário: ")
cargoFunc = input("Digite o cargo do funcionário: ")
salarFunc = float(input("Digite o salário do funcionário: "))


Aumento = (salarFunc*0.05)
SalarComAumento = salarFunc + Aumento

print(" ")
print("#################")
print("Novo salário: ",SalarComAumento)