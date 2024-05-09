#Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um script em linguagem Python que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média. 
soma2=0
soma1=0

n = int(input("Tamanho da turma: "))
P1 = ()
P2 = ()

for contador in range(n):
    nota =float(input("Digite nota 1: "))
    P1 = P1 + tuple([nota])
    soma1 += nota

for contador in range(n):
    nota =float(input("Digite nota 2: "))
    P2 = P2 + tuple([nota])
    soma2 += nota

media1 = soma1/n
media2 = soma2/n

print("Média da turma na prova 1: ", media1 )   
print("Média da turma na prova 2: ", media2 )   

if media1>media2:
    print("A turma obteve a melhor média na prova 1.")
else:
    print("A turma obteve a melhor média na prova 2.")
