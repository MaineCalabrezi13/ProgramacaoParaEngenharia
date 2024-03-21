#Calcular INSS

nomeFunc = input("Digite nome: ")
horas = float(input("Digite horas trabalhadas: "))
valor = float(input("Valor da hora trabalhada: "))

SalarBruto = horas*valor*30
desc = (SalarBruto*2)/100
SalarComDesc = SalarBruto - desc

print("")
print("####################")
print(nomeFunc, "Salário final: ", SalarComDesc, "Reais")

