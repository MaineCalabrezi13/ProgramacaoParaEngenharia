D = {}

for i in range(1,6):
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite valor do produto: "))
    
    dados = []
    dados.append(nome)
    dados.append(valor)
    D.update({nome:valor})
    
print(D)