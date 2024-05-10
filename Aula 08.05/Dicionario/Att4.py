D = {}

for i in range(1,6):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite nome do autor do livro: ")
    
    dados = []
    dados.append(nome)
    dados.append(autor)
    D.update({nome:autor})
    
print(D)