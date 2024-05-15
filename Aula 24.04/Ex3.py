#Em um script Python, crie uma lista vazia, que seja preenchida com médias de N alunos. Após a leitura das notas, mostrar a lista de notas:

medias = []
n = int(input("Quantos alunos deseja cadastrar médias: "))

for contador in range(0,n):
    valor = input("Insira uma nota: ") 
    medias.append(valor)

print ("Nr de alunos: ",n)
print ("Lista de médias digitados : ",medias)
