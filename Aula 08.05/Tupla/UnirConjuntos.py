#Escreva um programa Python que, dados duas tuplas que representam dois conjuntos A e B, construa uma outra que represente a união dos dois conjuntos (A ∪ B). 

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


tuplaC = tuplaA + tuplaB

print("Tupla A: ", tuplaA)
print("Tupla B: ", tuplaB)
print("Tupla C: ", tuplaC)
