#Faça um script em linguagem Python para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
media = (nota1+nota2)/2

if media==10:
    print("Aprovado com Distinção")
elif media>=7:
    print("Aluno aprovado")
elif media<7:
    print("Aluno reprovado")
