#FUNÇÃO


## PESQUISA ##

def pesquisarAgendamento(agendamentos,pets):
    os.system("cls")
    if len(agendamentos) == 0:
        input("NENHUM AGENDAMENTO CADASTRADO")
        return
    print("*"*8,"MENU DE PESQUISA","*"*8)
    print("\n1 - CÓDIGO\n2 - NOME DO PET")
    espaco()
    opcao = input("Escolha opção para pesquisar: ")
    espaco()

    pesquisa = {}

    if opcao == "1":
        codigo = int(input("Digite o código do agendamento: "))
        espaco()
        if codigo in agendamentos:
            pesquisa.update({codigo:agendamentos[codigo]})
        else:
            input("NENHUM AGENDAMENTO ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_pet(pesquisa)
        input()
        
    elif opcao == "2":
        nome = input("Digite o nome do pet: ").upper()
        for i in pets:
            for j in pets[i]:
                if j == "Nome do Pet ":
                    if nome == pets[i][j]:
                        pesquisa.update({i:pets[i]})
        
        if not pesquisa:
            input("NENHUM PET ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_pet(pesquisa)
        input()
        
def pesquisarPet(pets):
    os.system("cls")
    if len(pets) == 0:
        input("NENHUM PET CADASTRADO")
        return
    print("*"*8,"MENU DE PESQUISA","*"*8)
    print("\n1 - CÓDIGO\n2 - NOME")
    espaco()
    opcao = input("Escolha opção para pesquisar: ")
    espaco()

    pesquisa = {}

    if opcao == "1":
        codigo = int(input("Digite o código do pet: "))
        if codigo in pets:
            pesquisa.update({codigo:pets[codigo]})
        else:
            input("NENHUM PET ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_pet(pesquisa)
        input()
        
    elif opcao == "2":
        nome = input("Digite o nome: ").upper()
        for i in pets:
            for j in pets[i]:
                if j == "Nome do Pet ":
                    if nome == pets[i][j]:
                        pesquisa.update({i:pets[i]})
        
        if not pesquisa:
            input("NENHUM PET ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_pet(pesquisa)
        input()
    
def pesquisarCliente(clientes):
    os.system("cls")
    if len(clientes) == 0:
        input("NENHUM CLIENTE CADASTRADO")
        return
    
    print("*"*8,"MENU DE PESQUISA","*"*8)
    print("\n1 - CÓDIGO\n2 - NOME")
    espaco()
    opcao = input("Escolha opção para pesquisar: ")
    espaco()
    pesquisa = {}

    if opcao == "1":
        codigo = int(input("Digite o código do cliente: "))
        if codigo in clientes:
            pesquisa.update({codigo:clientes[codigo]})
        else:
            input("NENHUM CLIENTE ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_clientes(pesquisa)
        input()
            
    elif opcao == "2":
        nome = input("Digite o nome: ").upper()
        for i in clientes:
            for j in clientes[i]:
                if j == "Nome do Cliente ":
                    if nome == clientes[i][j]:
                        pesquisa.update({i:clientes[i]})
        
        if not pesquisa:
            input("NENHUM CLIENTE ENCONTRADO")
            return
        print("RESULTADO DA PESQUISA\n")
        listar_clientes(pesquisa)
        input()
        
    
    input()

##################################################

## EXCLUSÃO ##
def excluirAgendamento(agendamentos):
    os.system("cls")
    if len(agendamentos) == 0:
        input("NENHUM AGENDAMENTO CADASTRADO")
        return
    
    print("EXCLUIR\n")
    print("LISTA DE AGENDAMENTOS\n")
    listar_pet(agendamentos)
    excluir = int(input("\nDigite ID para excluir: \n"))
    if excluir in agendamentos:
        agendamentos.pop(excluir)
        input("\nAGENDAMENTO EXCLUIDO COM SUCESSO!")                     
    else:
        input("ID DO AGENDAMENTO NÃO ENCONTRADO! TENTE NOVAMENTE")
        
def excluirPet(pets):
    os.system("cls")
    if len(pets) == 0:
        input("NENHUM PET CADASTRADO")
        return
    
    print("EXCLUIR\n")
    print("LISTA DE PETS CADASTRADOS\n")
    listar_pet(pets)
    excluir = int(input("\nDigite ID para excluir: \n"))
    if excluir in pets:
        pets.pop(excluir)
        input("\nPET EXCLUIDO COM SUCESSO!")                     
    else:
        input("ID DO PET NÃO ENCONTRADO! TENTE NOVAMENTE")
    
def excluirCliente(clientes):
    os.system("cls")
    if len(clientes) == 0:
        input("NENHUM CLIENTE CADASTRADO")
        return
    
    print("EXCLUIR\n")
    print("LISTA DE CLIENTES CADASTRADOS\n")
    listar_clientes(clientes)
    excluir = int(input("\nDigite ID para excluir: \n"))
    if excluir in clientes:
        clientes.pop(excluir)
        input("\nCLIENTE EXCLUIDO COM SUCESSO!")                     
    else:
        input("ID DO CLIENTE NÃO ENCONTRADO! TENTE NOVAMENTE")
        
##############################

## EDIÇÃO ##    
def editar_agendamento(agendamentos):
    os.system("cls")
    if len(agendamentos) == 0:
        input("NENHUM AGENDAMENTO CADASTRADO")
        return

    print("EDITAR AGENDAMENTO\n")
    print("LISTA DE AGENDAMENTOS\n")
    listar_agendamento(agendamentos)
    editar = int(input("\nDigite o código do agendamento para editar: \n"))
    print()
    print()

    if not editar in agendamentos:
        input("CÓDIGO DO AGENDAMENTO NÃO ENCONTRADO! TENTE NOVAMENTE")
        return

    print("*"*8,"MENU DE EDIÇÃO","*"*8)
    print("1 - DATA\n2 - HORA\n3 - SAIR")
    espaco()
    opcao = input("Escolha a opção do campo que deseja editar: ")
    espaco()
    match opcao:
        case "1":
            nova_data = input("Digite data (dd/mm/aaaa): ")
            agendamentos[editar]["Data "] = nova_data
        case "2":
            nova_hora = input("Digite hora (hh:mm): ")
            agendamentos[editar]["Hora "] = nova_hora
        case "3":
            return
        case _:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")

    input("\nAGENDAMENTO EDITADO COM SUCESSO!")  
        

def editarPet(pets, clientes):
    os.system("cls")
    if len(pets) == 0:
        input("NENHUM PET CADASTRADO")
        return
    
    print("EDITAR\n")
    print("LISTA DE PET CADASTRADOS\n")
    listar_pet(pets)
    editar = int(input("\nDigite ID para editar: \n"))
    print()
    print()
    
    if not editar in pets:
        input("CÓDIGO DO PET NÃO ENCONTRADO! TENTE NOVAMENTE")
        return
                            
    print("*"*8,"MENU DE EDIÇÃO","*"*8)
    print("1 - NOME\n2 - ESPECIE\n3 - RAÇA\n4 - IDADE\n5 - PESO\n6 - SEXO\n7 - DONO\n8 - SAIR")
    espaco()
    opcao = input("Escolha opção do campo que deseja editar: ")
            
    match opcao:
        case "1":
            novo_nome = input("Digite novo nome: ").upper()
            pets[editar]["Nome do Pet "] = novo_nome
        case "2":
            novo_especie = input("Digite nova espécie: ").upper()
            pets[editar]["Espécie "] = novo_especie
        case "3":
            novo_raca = input("Digite nova raça: ") .upper()
            pets[editar]["Raça "] = novo_raca
        case "4":
            nova_idade= input("Digite a nova idade: ")
            pets[editar]["Idade "] = nova_idade
        case "5":
            novo_peso= input("Digite o novo peso: ")
            pets[editar]["Peso "] = novo_peso
        case "6":
            
            while True:
                novo_genero = input("Digite o novo gênero (F/M): ").upper()
                if novo_genero in ["F", "M"]:
                    pets[editar]["Sexo "] = novo_genero
                    break
                else:
                    print("SEXO INVÁLIDO! DIGITE F PARA FÊMEA OU M PARA MACHO.")
                    
        case "7":            
            print("\nLISTA DE CLIENTES CADASTRADOS\n")
    
            listar_clientes(clientes)

            while True:
                codDono = int(input("\nDigite código do dono: "))
                                
                if codDono in clientes:
                    novo_dono = clientes[codDono]
                    pets[editar]["Dono "] = novo_dono
                    break                                                                                                                        
                else:
                    input("CÓDIGO DO CLIENTE NÃO ENCONTRADO! TENTE NOVAMENTE ")   
        case "8":
            return                                       
    input("\nPET EDITADO COM SUCESSO!")  
        
def editarCliente(clientes,pets):
    os.system("cls")
    if len(clientes) == 0:
        input("NENHUM CLIENTE CADASTRADO")
        return
    
    print("EDITAR\n")
    print("LISTA DE CLIENTES CADASTRADOS\n")
    listar_clientes(clientes)
    editar = int(input("\nDigite ID para editar: \n"))
    print()
    print()
    
    if not editar in clientes:
        input("CÓDIGO DO CLIENTE NÃO ENCONTRADO! TENTE NOVAMENTE")
        return
                            
    print("*"*8,"MENU DE EDIÇÃO","*"*8)
    print("\n1 - NOME\n2 - ENDEREÇO\n3 - TELEFONE\n4 - SAIR")
    espaco()
    opcao = input("Escolha opção do campo que deseja editar: ")                                                                    
        
    match opcao:
        case "1":
            novo_nome = input("Digite novo nome: ").upper()
            clientes[editar]["Nome do Cliente "] = novo_nome
            for pet in pets.values():
                if pet["Dono "].get(editar):
                    pet["Dono "][editar] = novo_nome
        case "2":
            novo_endereco = input("Digite novo endereço: ").upper()
            clientes[editar]["Endereço "] = novo_endereco
        case "3":
            novo_tell = input("Digite novo teleone: ") 
            clientes[editar]["Telefone para contato "] = novo_tell
        case "4":
            return                               
    input("\nCLIENTE EDITADO COM SUCESSO!")    
    
##############################         

## AGREGADOS ##
def espaco():
    print("\n**************************\n")
    
    
def pegaIdRegistro(lista, tipo):
    ids = []
    #percorre todos os ids do dicionario e guarda em uma lista
    for i in lista:
        ids.append(i)
        
    if tipo.upper() == "P": #retorna o primeiro id
        return ids[0]
    elif tipo.upper() == "U": #retorna o ultimo id
        return ids[len(ids) - 1]
    elif tipo.upper() == "T": #retorna todos os ids
        return ids

def fechar_caixa(clientes,pets,agendamentos):
    os.system("cls")
    print("*"*8,"FECHAMENTO DE CAIXA","*"*8)
    print()
    print(f"Quantidade de clientes cadastrados: {len(clientes)}")
    print(f"Quantidade de pets cadastrados: {len(pets)}")
    print(f"Quantidade de agendamentos realizados: {len(agendamentos)}")
    
    total_faturado = 0
    for agendamento in agendamentos.values():
        # Remove o "R$ " e converte o valor para float
        valor = float(agendamento["Valor "])
        total_faturado += valor
    
    print(f"Total faturado: R$ {total_faturado:.2f}")
    input()

    
#####################################
   
## LISTAR ##
def listar_agendamento(agendamentos):
    os.system("cls")
    if len(agendamentos) == 0:
        print("NENHUM AGENDAMENTO CADASTRADO")
        return
    print("LISTA DE AGENDAMENTOS\n")
    #pega o id do ultimo agendamento
    ultimoId = pegaIdRegistro(agendamentos, "U")
    for i in agendamentos:
        print("*"*30)
        
        for j in agendamentos[i]:
            print(str(j)+ ": " + str(agendamentos[i][j]))

        #só mostra na tela se estiver no ultimo cliente                    
        if i == ultimoId:
            print("*"*30)
            
def listar_clientes(clientes):
    os.system("cls")
    if len(clientes) == 0:
        print("NENHUM CLIENTE CADASTRADO")
        return
    print("LISTA DE CLIENTES CADASTRADOS\n")
    #pega o id do ultimo cliente
    ultimoId = pegaIdRegistro(clientes, "U")
    for i in clientes:
        print("*"*30)
        print("Código: " + str(i))
        
        for j in clientes[i]:
            print(str(j)+ ": " + str(clientes[i][j]))

        #só mostra na tela se estiver no ultimo cliente                    
        if i == ultimoId:
            print("*"*30)
    
    
def listar_pet(pets):
    os.system("cls")
    if len(pets) == 0:
        print("NENHUM PET CADASTRADO")
        return
    print("LISTA DE PETs CADASTRADOS\n")
    ultimoId = pegaIdRegistro(pets, "U")
    for i in pets:
        print("*"*30)
        print("Código: " + str(i))
        
        for j in pets[i]:
            print(str(j)+ ": " + str(pets[i][j]))

        #só mostra na tela se estiver no ultimo pet                    
        if i == ultimoId:
            print("*"*30)

################################

## CADASTRO ##
        
def agendar(agendas,pets,id):
    
    if not pets:
        input("Nenhum pet cadastrado!")
        return
    while True:
        os.system("cls") 
        print("AGENDAMENTO\n")
        print("*"*8,"SERVIÇOS","*"*8)
        print("\n1 - BANHO E TOSA | R$ 50,00 \n2 - CASTRAÇÃO | R$ 200,00\n3 - VACINAS | R$ 80,00\n4 - CONSULTAS | R$ 100,00\n5 - SAIR")
        espaco()
        servico = input("Escolha o serviço: ")
        if servico == "1":
            servico = "BANHO E TOSA" 
            valor = 50
        elif servico == "2":
            servico = "CASTRAÇÃO"
            valor = 200
        elif servico == "3":                
            servico = "VACINAS"
            valor = 80
        elif servico == "4":
            servico = "CONSULTAS"
            valor = 100
        elif servico == "5":
            return
        
        listar_pet(pets)
        pet = int(input("Digite o código do Pet: "))
        espaco()
        if pet not in pets:
            input("PET NÃO ENCONTRADO")
            continue
            
        agendaData = input("Digite data (dd/mm/aaaa): ")
        agendaHora = input("Digite hora (hh:mm): ")
        
        agenda={
            "Código ":id,
            "Serviço ":servico,
            "Pet ":{pets[pet]["Nome do Pet "]},
            "Dono ":pets[pet]["Dono "],
            "Data ":agendaData,#VER FUNC
            "Hora ":agendaHora,
            "Valor ":valor
        }
        agendas.update({id:agenda})
        input("AGENDAMENTO CADASTRADO COM SUCESSO! ")
        
def cadastroCliente(clientes, id):
    os.system("cls") 
    print("CADASTRO DE CLIENTE\n")
    nomeClient = input("Digite nome do cliente: ").upper()
    enderecoClient = input("Digite endereço do cliente: ").upper()
    tellClient = input("Digite número de telefone do cliente: ")
    dadosClient={

        "Nome do Cliente ":nomeClient,
        "Endereço ":enderecoClient,
        "Telefone para contato ":tellClient
    }
    clientes.update({id:dadosClient})
    input("\nCLIENTE SALVO COM SUCESSO!")
    
    
def cadastroPet(pets, id, clientes):
    if len(clientes) == 0:
        input("NENHUM CLIENTE CADASTRADO")
        return
    
    print("CADASTRO DE PET\nLISTA DE DONOS CADASTRADOS\n")
    
    listar_clientes(clientes)
    codDono = int(input("\nDigite código do dono: \n"))
    espaco()
    
    if codDono in D_clientes:    
        print("CADASTRO DE PET\n")
        nomePet=input("Digite nome do Pet: ").upper()
        especiePet=input("Digite espécie do Pet: ").upper()
        racaPet=input("Digite raça do Pet: ").upper()
        idadePet=input("Digite idade do Pet: ")
        pesoPet=float(input("Digite peso do Pet: "))
        while True:
            sexoPet=input("Digite sexo do Pet (F/M): ").upper()
            if sexoPet in ["F", "M"]:
                break
            else:
                print("SEXO INVÁLIDO! DIGITE F PARA FÊMEA OU M PARA MACHO.")
                
        dadosPet = {
            "Nome do Pet ":nomePet,
            "Espécie ":especiePet,
            "Raça ":racaPet,
            "Idade ":idadePet,
            "Peso ":pesoPet,
            "Sexo ":sexoPet,
            "Dono ": {codDono:D_clientes[codDono]["Nome do Cliente "]}
            }
        
        pets.update({id:dadosPet})
        input("\nPET SALVO COM SUCESSO!")            
    else:
        input("CÓDIGO NÃO ENCONTRADO! TENTE NOVAMENTE ")        
    
################################################# 



import os

idPet=1
idClient=1
idAgendar=1

#DICIONARIOS
D_clientes={}
D_Pet={}
D_agenda={}

while True:
    os.system("cls")
    print("*"*10,"MENU","*"*10)
    print("1 - CLIENTE\n2 - PET\n3 - AGENDAMENTO\n4 - SAIR")
    espaco()
    opcao=input("Escolha opção: ")
    if (opcao == "4"):
        fechar_caixa(D_clientes,D_Pet,D_agenda)
        break
    
    match opcao:
        case "1":
            while True:
                os.system("cls")
                print("*"*8,"MENU CLIENTE","*"*8)
                print("\n1 - CADASTRAR\n2 - EDITAR\n3 - EXCLUIR\n4 - LISTAR\n5 - PESQUISAR\n6 - SAIR")
                espaco()
                opcao = input("Digite opção: ")
        
                if opcao == "1":
                    cadastroCliente(D_clientes, idClient)
                    idClient+=1
                if opcao == "2":
                    editarCliente(D_clientes,D_Pet)
                if opcao == "3":                
                    excluirCliente(D_clientes)
                if opcao == "4":
                    listar_clientes(D_clientes)  
                    input()
                if opcao == "5":
                    pesquisarCliente(D_clientes)
                if opcao == "6":
                    break
        
        case "2":
            while True:
                os.system("cls")
                print("*"*8,"MENU PET","*"*8)
                print("\n1 - CADASTRAR\n2 - EDITAR\n3 - EXCLUIR\n4 - LISTAR\n5 - PESQUISAR\n6 - SAIR")
                espaco()
                opcao = input("Digite opção: ")
        
                if opcao == "1":
                    cadastroPet(D_Pet, idPet, D_clientes)
                    idPet+=1
                if opcao == "2":
                    editarPet(D_Pet, D_clientes)
                if opcao == "3":                
                    excluirPet(D_Pet)
                if opcao == "4":
                    listar_pet(D_Pet)  
                    input()
                if opcao == "5":
                    pesquisarPet(D_Pet)
                if opcao == "6":
                    break

        
        case "3":
            while True:
                os.system("cls")
                print("*"*8,"MENU AGENDAMENTO","*"*8)
                print("\n1 - AGENDAR \n2 - EDITAR\n3 - EXCLUIR\n4 - LISTAR\n5 - PESQUISAR\n6 - SAIR")
                espaco() 
                opcao = input("Digite opção: ")
                
                if opcao == "1":
                    agendar(D_agenda,D_Pet,idAgendar)
                    idAgendar+=1
                if opcao == "2":
                    editar_agendamento(D_agenda)
                if opcao == "3":                
                    excluirAgendamento(D_agenda)
                if opcao == "4":
                    listar_agendamento(D_agenda)  
                    input()
                if opcao == "5":
                    pesquisarAgendamento(D_agenda,D_Pet)
                if opcao == "6":
                    break

                                
                            
            