
while True:
    print("********************************************\nCÁLCULO DE GRANDEZAS ELÉTRICAS\n********************************************")
    print("1. Tensão (em Volt)\n2. Resistência (em Ohm)\n3. Corrente (em Ampére)\n 4. Sair\n********************************************\n  ")
    escolha = input("Qual grandeza deseja calcular?")
    if(escolha==" "):
        escolha = True
    if(escolha=="1"):
            R = float(input("Digite a Resistência: "))
            I = float(input("Digite a Corrente: "))
            U = R*I
            print("A Tensão é: ",U)
    elif(escolha=="2"):
            U = float(input("Digite a Tensão: "))
            I = float(input("Digite a Corrente: "))
            R = U*I
            print("A Resistência é: ",R)
    elif(escolha=="3"):
            R = float(input("Digite a Resistência: "))
            U = float(input("Digite a Tensão: "))
            I = U/R
            print("A Corrente é: ",I)
    elif(escolha=="4"):
        break

    