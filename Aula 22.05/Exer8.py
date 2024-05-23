def Maior(a,b,c):
    soma=a+b
    if(soma>c):
        return True
    else:
        return False

n1 = int(input("Digite número 1: "))
n2 = int(input("Digite número 2: "))
lmt = int(input("Digite o limite: "))

print(Maior(n1,n2,lmt))
