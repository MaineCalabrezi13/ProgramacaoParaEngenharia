#Faça um Programa Python que leia uma lista de 10 caracteres, e diga quantas vogais e consoantes foram lidas. Mostre a lista ao final.

letra=0
vogais = 0
consoante = 0
for i in range(1,11):
    caracter = input("Digite caracter: ").upper()
    letra.append(caracter)
    if caracter in("A","E","I","O","U"):
        vogais = vogais + 1
    else:
        consoante = consoante + 1
Letras = [vogais,consoante]
print("A quantidade de vogais: ",Letras[0],"\nA quantidade de consoantes: ",Letras[1])
