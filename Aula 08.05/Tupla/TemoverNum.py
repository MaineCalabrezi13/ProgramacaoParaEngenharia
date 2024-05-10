#Dada uma tupla  T  de n valores inteiros, elabore um programa que remova todos os números pares da tupla. 

T = (1,2,3, 4, 5, 6, 7, 8, 9, 10)

impar=()
for valor in T:
    if valor%2==1:
        impar = impar + tuple([valor])
print(impar)
