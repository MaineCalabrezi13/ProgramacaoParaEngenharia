#Faça um programa que peça nome e nota do aluno (entre zero e dez). Mostre uma mensagem caso o valor nota seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nome=input("Digite nome do aluno: ")
    nota=int(input("Digite nota do aluno: "))
    if (nota<=0)or(nota>=10):
        print("Digite uma nota válida")
    else:
        break
        
        