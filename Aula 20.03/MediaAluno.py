#Escrever um algoritmo para ler o nome de um aluno e a media final.

nome =input("Digite nome do aluno: ")
media = float(input("Digite sua média: "))

if media<5:
    print("Aluno reprovado!")
elif (media>=5)and(media<7):
    print("Aluno em recuperação!")
else:
    print("Aluno aprovado!")