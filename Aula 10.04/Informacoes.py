
while True:
    nome = input("Digite nome: ")
    idade = int(input("Digite idade: "))
    salario = float(input("Digite salário: "))
    sexo = input("Digite sexo: ").upper()
    estadoCiv = input("Digite estado civil: ").upper()
    
    CaracNome = len(nome)
    
    if (CaracNome<=3):
        print("Número de caracteres invalido")
    if (salario<0):
        print("Salario invalido")
    if (idade<0)or(idade>100):
        print("Idade inválida")
    if sexo not in ["M", "F"]:
        print("Sexo invalido")
    if estadoCiv not in ["S", "C", "V", "D"]:
        print("Estado civil invalido")
    else:
        break
    