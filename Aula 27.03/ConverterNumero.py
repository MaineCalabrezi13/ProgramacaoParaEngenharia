#solicita um número decimal e imprime o correspondente em hexa, binário e octal.

NumeroDecimal=int(input("Digite um número: "))

hexa = hex(NumeroDecimal)
binario = bin(NumeroDecimal)
octal = oct(NumeroDecimal)

print("HEXA: ",hexa)
print("BINARIO: ",binario)
print("OCTAL: ",octal)
