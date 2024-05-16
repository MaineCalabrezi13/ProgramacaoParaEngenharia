
D = {}
n = int(input("Digite o número de produtos que deseja digitar: "))

for i in range(n):
    produto = input("Digite nome do produto: ")
    valor = float(input("Digite preço do produto: "))
    D.update({produto:valor})
print("Produtos cadastrados: ",D)
    