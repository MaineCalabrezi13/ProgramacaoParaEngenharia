#solicita um número decimal e imprime o correspondente em hexa, binário e octal.

NumeroDecimal=int(input("Digite um número: "))

hexa = NumeroDecimal/16
binario = NumeroDecimal/2
octal = NumeroDecimal/8

print("HEXA: ",hexa)
print("BINARIO: ",binario)
print("OCTAL: ",octal)
