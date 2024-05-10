#Desenvolva um código em Python que adicione em um dicionário “D” os seguintes campos: nome, idade, endereço e telefone e mostre os dados no final.

D ={}

while True:
    nome = input("Digite nome: ")
    idade = int(input("Digite idade: "))
    endereco = input("Digite endereço: ")
    telefone = int(input("Digite telefone: "))

    dados = []
    dados.append(nome)
    dados.append(idade)
    dados.append(endereco)
    dados.append(telefone)
    D.update({nome:dados})
    
    if input("Deseja continuar: ").upper() == "N":
        break
print(D)

