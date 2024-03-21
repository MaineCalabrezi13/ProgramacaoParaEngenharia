#Sua tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto. Você deve mostrar:

precoProd = float(input("Digite valor do produto: "))

desc = (precoProd*20)/100
precoComDesc = (precoProd-desc)

print("")
print("################")
print("Valor do preço original: ", precoProd)
print("Valor do desconto: ", desc)
print("Valor do produto com desconto: ", precoComDesc)
