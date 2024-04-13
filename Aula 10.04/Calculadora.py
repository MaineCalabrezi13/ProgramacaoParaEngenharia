while True:
    print("*********** MENU DE OPÇÃO ***********")
    print("Adição (opção 1) \nSubtração (opção 2)\nMultiplicação (opção 3) \nDivisão (opção 4) \nSaída (opção 5)") 
    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        break
    
    n1 = float(input("Digite número 1: "))
    n2 = float(input("Digite número 2: "))
    
    match opcao:
        case 1:
            resul = n1 + n2
        case 2:
            resul = n1 - n2
        case 3:
            resul = n1 * n2
        case 4:
                resul = n1 / n2
    print("Resultado:", resul)