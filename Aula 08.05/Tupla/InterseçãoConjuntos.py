#Escreva um programa Python que, dados duas tuplas que representam dois conjuntos (A e B), construa uma outra que represente a interseção dos dois conjuntos (A ∩ B). 

n = int(input("Digite nr deseja inserir: "))
tuplaA = ()
tuplaB = ()
tuplaC = ()

for contador in range(n):
    valor = int(input("Digite número tupla A: "))
    tuplaA = tuplaA + tuple([valor])

for contador in range(n):
    valor = int(input("Digite número tupla B: "))
    tuplaB = tuplaB + tuple([valor])

#Verifica se o valor ja foi digitado
    if valor in tuplaA and valor not in tuplaC:
        tuplaC = tuplaC + tuple([valor])

print("Tupla A: ", tuplaA)
print("Tupla B: ", tuplaB)
print("Tupla C: ", tuplaC)