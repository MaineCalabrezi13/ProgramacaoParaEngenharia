#Calcular o novo salário de um funcionário, sendo que quem recebe salário de até R$1000,00 terá aumento de 10%, os outros terão aumento de 5%
Salario =float(input("Digite salario do funcionario: "))

if Salario<=1000:
    NovoSalar = Salario+(Salario*0.1)
else:
    NovoSalar=Salario+(Salario*0.5)
print("O novo salario com desconto é: ", NovoSalar)
