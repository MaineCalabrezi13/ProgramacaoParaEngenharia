
def Existe(a,b):
    return a in b
    
numeros=[]
while True:
    n1 = int(input("Digite número: "))
    numeros.append(n1)


    if input("Deseja continuar S/N: ").upper() == "N":
        break

numConf=int(input("Digite número para conferir na lista: "))
print(Existe(numConf,numeros))
