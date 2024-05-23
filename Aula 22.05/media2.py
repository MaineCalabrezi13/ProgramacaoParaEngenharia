def media(a,b,c):
    med=(a+b+c)/3
    return med

def aprovar(a,b,c):
    if media(a,b,c) >=6:
        print("Aprovado")
    elif (media(a,b,c)>=4)and(media(a,b,c)<6):
        print("Verificação Suplementar")
    elif (media(a,b,c)<4):
        print("Reprovado")
    

while True:
    nome = input("Digite nome: ")
    nota1 = float(input("Digite nota 1: "))
    nota2 = float(input("Digite nota 2: "))
    nota3 = float(input("Digite nota 3: "))
    resul = media(nota2,nota2,nota3)
    print("Média final: ",resul)
    aprovar(nota2,nota2,nota3)

    if input("Deseja continuar: ").upper() == "N":
        break