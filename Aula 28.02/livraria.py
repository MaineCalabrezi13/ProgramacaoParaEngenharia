
copias= float(input("Digite quantidade de cópias: "))

vLivro = 24.95
vLivroComPercentual = (24.95*35)/100
vLivroTotal = 0
copias = int(copias)
vLivroTotal = vLivroComPercentual+3
for i in range(copias -1):
    vLivroTotal = vLivroTotal -(vLivroComPercentual + 0.75)

print ("O valor total é:", vLivroTotal)
