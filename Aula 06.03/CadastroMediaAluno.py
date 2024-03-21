#Faca um script que receba como entrada os dados  de um aluno: nome, curso, disciplina, nota1, nota2, nota3. Calcule a média do aluno e mostre o resultado:

nome = input("Digite seu nome: ")
curso = input("Digite o nome do seu curso: ")
disciplina= input("Digite a disciplina: ")
n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))
n3 = float(input("Digite nota 3: "))

media = (n1 + n2 + n3 )/3

print(" ")
print("########################")
print("Olá, ",nome, "Sua média é: ",media)