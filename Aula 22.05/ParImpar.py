
def ParImpar(a):
    if(a%2==0):
        num="PAR"
    else:
        num="IMPAR"
    return num

while True:
    n = int(input("Digite número: "))
    resul = ParImpar(n)
    print(resul)
    if input("Deseja continuar S/N: ").upper() == "N":
        break