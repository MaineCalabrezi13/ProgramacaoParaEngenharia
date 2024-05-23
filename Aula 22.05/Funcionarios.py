
def salario(b, s = 9000):
    print("Nome: ",b,"\nSalario: ",s)

while True:
    nome = input("Digite nome do funcionário: ")
    salarioFunc = float(input("Digite salário do funcionário: "))
    if salarioFunc == 0:
        salario(nome)
    else:
        salario(nome, salarioFunc)
    if (input("Deseja continuar S/N: ")).upper() == "N":
        break
