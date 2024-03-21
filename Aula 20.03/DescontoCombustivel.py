#Um posto de abastecimento está comercializando combustíveis com a seguinte tabela de descontos:

NumeroLitrosVendidos = float(input("Digite a quantidade de litros: "))
TipoCombustivel = input("Digite tipo de combustível: (Sigla A/G) ")

if TipoCombustivel == "A":
    if NumeroLitrosVendidos <=20 :
        descLitro = (4.98*NumeroLitrosVendidos)
        descLitro =descLitro - (descLitro* 2)/100
    if NumeroLitrosVendidos >20:
        descLitro = (4.98*NumeroLitrosVendidos)
        descLitro = descLitro -(descLitro* 5)/100
        
elif TipoCombustivel =="G":
    if NumeroLitrosVendidos<=20:
        descLitro = (5.57*NumeroLitrosVendidos)
        descLitro = descLitro -(descLitro* 4)/100
    if NumeroLitrosVendidos >20:
        descLitro = (5.57*NumeroLitrosVendidos)
        descLitro = descLitro -(descLitro* 6)/100

print("O valor a ser pago será: ",descLitro)


