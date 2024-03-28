
ValorHoras = float(input("Digite quanto você ganha por hora: "))
HorasTrabalhadas = float(input("Digite quantas horas você trabalha no mês: "))

SalarioMes = ValorHoras*HorasTrabalhadas*30
ImpostoRenda = (SalarioMes*11)/100
inss = (SalarioMes*8)/100
Sindicato = (SalarioMes*5)/100

SalarioLiquido = SalarioMes - ImpostoRenda - inss - Sindicato

print(" ")
print("****************************")
print("Salário Bruto : R$,",SalarioMes)
print("IR (11%) : R$", ImpostoRenda)
print("INSS (8%) : R$ ", inss)
print("Sindicato ( 5%) : R$", Sindicato)
print("Salário Liquido : R$",SalarioLiquido)


