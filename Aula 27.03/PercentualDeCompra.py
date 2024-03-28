#Dados o valor da compra e o percentual de desconto, calcule o valor a ser pago. Considere que o percentual de desconto é um número real entre 0 e 1.
ValorCompra = float(input("Digite o valor da compra: "))
Percentual = float(input("Digite o percentual de desconto: "))

ValorComPercentual = ValorCompra-(ValorCompra*Percentual)
print("O valor final com o desconto é igual a: ",ValorComPercentual)