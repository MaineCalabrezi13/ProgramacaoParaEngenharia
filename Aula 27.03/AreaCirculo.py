Comprimento = float(input("lDigite um número de unidade de comprimento: "))
if Comprimento >=0:
    area= 3.14159 *(Comprimento*Comprimento)
    print("A área do círculo de raio ",Comprimento,"unidades e {:.2f}".format(area),"unidades")
else:
    print("Valores negativos não são permitidos")