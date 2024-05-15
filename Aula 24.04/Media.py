# Criando a lista medias vazia 
medias = []
total = 0

for contador in range(0,5):
    print (f"Digite notas do aluno {contador+1}")
    nota1 = float(input("Insira uma nota1: "))
    nota2 = float(input("Insira uma nota2: "))
    nota3 = float(input("Insira uma nota3: "))
    nota4 = float(input("Insira uma nota4: "))
    media = (nota1 + nota2 + nota3 + nota4)/4
    print ("Média do aluno: ", media)
    medias.append(media)
    #contar alunos aprovados
    if (media >= 7):
        total += 1
print ("Lista de medias digitados  : ",medias)
print ("Total alunos Aprovados     : ", total)
