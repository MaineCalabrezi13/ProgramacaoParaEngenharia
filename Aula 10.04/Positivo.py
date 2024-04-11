#Desenvolva um script Python que lê vários números positivos via teclado. Quando o número lido for -1, o script deve parar e exibir a soma de todos os números positivos inseridos, a média desses números, o menor e o maior número digitado

soma =0
while True:
    num=int(input("Digite número: "))
    if num<0:
        break
    soma = soma+num
    
print(soma)