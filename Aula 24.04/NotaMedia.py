#Faça um Programa Python que peça as duas notas de 10 alunos e armazene numa lista. Calcule e mostre a média de cada aluno.
nota = []
notas = []
for i in range(0,3):
    alunos = input("Digite nome: ")
    nota1 = float(input("Digite nota 1: "))
    nota2 = float(input("Digite nota 2: "))
    
    media = (nota1+nota2)/2
    print("A média do aluno é: ",media) 
    
    nota = [nota1,nota2]
    notas.append(nota)

print("LIsta de notas: ",notas)
