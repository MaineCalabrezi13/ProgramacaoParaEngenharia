#Neste exercício, você vai criar um programa em Python que verifica se um componente elétrico está obedecendo à Lei de Ohm. 

Tensao = float(input("Insira o valor da tensão em volts: "))
Corrente = float(input("Insira o valor da corrente em amperes: "))
Resistencia = float(input("Insira o valor da resistência em ogms: "))

TensaoEsperada = Corrente*Resistencia

if TensaoEsperada == Tensao:
   print("O componente obedece à Lei de Ohm")
else:
    print("O componente não obdece à Lei de Ohm")