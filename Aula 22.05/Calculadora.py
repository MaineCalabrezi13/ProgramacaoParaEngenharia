def adicao(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

while True:
    print("adição (opção 1)\nsubtração (opção 2)\nmultiplicação (opção 3)\ndivisão (opção 4) \nSaída (opção 5)")
    opcao=input("Digite opção: ")
    if opcao == "5":
        break
    n1 = int(input("Digite número 1: "))
    n2 = int(input("Digite número 2: "))
    if(opcao=="1"):
        print("Soma: ",adicao(n1,n2))
    elif(opcao=="2"):
        print("Subtração: ",subtracao(n1,n2))
    elif(opcao=="3"):
        print("Multiplicação: ",multiplicacao(n1,n2))
    elif(opcao=="4"):
        print("divisão: ",divisao(n1,n2))
