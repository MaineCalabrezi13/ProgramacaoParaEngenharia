D = {}

for i in range(1,11):
    nome = input("Digite o nome do amigo: ")
    tell = input("Digite o telefone: ")
    
    dados = []
    dados.append(nome)
    dados.append(tell)
    D.update({nome:tell})
    
print(D)