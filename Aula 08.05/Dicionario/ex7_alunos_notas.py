#criar um dicionario vazio
alunos  = {}
n = int(input("Quantos alunos deseja cadastrar? "))

for i in range(n):
    nome   = input("digite nome : ")
    nota1  = float(input("Digite nota 1: "))
    nota2  = float(input("Digite nota 2 "))
    nota3  = float(input("Digite nota 3: "))
    #criar uma lista dentro dicionario
    notas = []
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    #adicionando elementos no dicionario
    alunos.update({nome:notas})
    #verificar a media do aluno e situacao
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print ("Aluno: ",nome," está Aprovado")
    if media >= 5 and media < 7:
        print ("Aluno: ",nome," está em Recuperação")
    if media < 5:
        print ("Aluno: ",nome," está Reprovado")
    
print ("Lista de alunos e notas : ", alunos)
