def media(a,b,c):
    med=(a+b+c)/3
    return med

    

while True:
    nome = input("Digite nome: ")
    nota1 = float(input("Digite nota 1: "))
    nota2 = float(input("Digite nota 2: "))
    nota3 = float(input("Digite nota 3: "))
    resul = media(nota2,nota2,nota3)
    print("Média final: ",resul)

    if input("Deseja continuar: ").upper() == "N":
        break