#Faça um Programa Python que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números impares na lista IMPAR. Imprima ao final os três vetores.
par=[]
impar=[]

numeros = []
for i in range(0,20):
    num = float(input("Digite um número: "))
    
    numeros.append(num)

    if(num%2==0):
        par.append(num)
    else:
        impar.append(num)
print("Lista: ",numeros,"Lista par: ",par,"Lista impar: ",impar)