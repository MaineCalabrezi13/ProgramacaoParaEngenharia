#Faça um Programa Python que leia 4 notas, ao final mostre as notas e a média geral.

valor = []

for i in range(1,5):
    notas = float(input("Digite nota: "))

 #Trazer as notas
    valor.append(notas)

    #Media
soma_das_notas = sum(valor)
media = soma_das_notas/4

print("Notas: ", valor,"\nMédia: ",media)

