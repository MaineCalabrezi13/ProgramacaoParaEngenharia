D = {}

while True:
    nome = input("Digite nome: ").upper()
    idade = int(input("Digite idade: "))
    sexo = input("Digite sexo (M/F)").upper()

    dados = []
    dados.append(nome)
    dados.append(idade)
    dados.append(sexo)
    D.update({nome:dados})

    if input("Deseja continuar: ").upper() == "N":
        break
print(D)