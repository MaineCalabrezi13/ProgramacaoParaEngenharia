#Criar um programa em Python que ajuda a verificar se um parafuso está apertado corretamente de acordo com o torque especificado. 

ToqueAplicado = float(input("Insira o valor do toqu aplicado em Nm: "))
ToqueApertoRecomendado = float(input("Insira o valor do toque de aperto recomendado em Nm: "))

ToqueAplicadoPorc = (ToqueAplicado*10)/100
if ToqueAplicado>=ToqueApertoRecomendado:
    print("O parafuso está apertado corretamente")
else:
    print("O parafuso não está apertado corretamente")
