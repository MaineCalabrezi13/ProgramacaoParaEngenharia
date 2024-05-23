def somar(a):
    j=0
    for i in range(1,a + 1):
        j=j+i
    return j

    

while True:
    n = int(input("Digite número: "))
    print(somar(n))

    if input("Deseja continuar: ").upper() == "N":
        break



    
              