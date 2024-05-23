
def NumPosNeg(a):
    if(a>0):
        num="O número é positivo!"
    elif(a<0):
        num="O número é negativo!"
    else:
        num="Número igual a zero!"
    return num

while True:
    n = int(input("Digite número: "))
    resul = NumPosNeg(n)
    print(resul)
    if input("Deseja continuar S/N: ").upper() == "N":
        break