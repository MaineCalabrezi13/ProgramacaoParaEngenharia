def media(a,d):
    med=a/d
    return med

    

n = int(input("Digite número de notas: "))
notas=0
for i in range(n):
    nota = float(input("Digite nota: "))
    notas = notas+nota
resul = media(notas,n)
print("Média final: ",resul)

