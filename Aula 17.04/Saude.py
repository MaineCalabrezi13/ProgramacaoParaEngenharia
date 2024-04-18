#Elabore um script em Python que leia nome pessoa entrevistada, sexo (M/F) e seu tipo doença. Calcule e mostre o total de entrevistados em cada tipo e de cada sexo.

sexoM=0
sexoF=0
DB =0
HP=0
CO=0
AS=0
NP=0

while True:
    print("************ MENU ************** \nDB - Diabetes \nHP - Hipertensão \nCO - Colesterol Alto \n AS – Asma \nNP – Não possui doença \nS - Encerrar pesquisa \n *****************************")
    print()
    opcao=input("Digite opção: ").upper()
    if (opcao=="S"):
        break
    else:
        nome = input("Digite nome da pessoa: ")
        sexo = input("Digite sexo (M/F): ").upper()
        tipoDoenca = input("Digite o tipo de doença: ").upper()
        
        if(sexo=="M"):
            sexoM+=1
        else:
            sexoF+=1
        if(tipoDoenca=="DB"):
            DB += 1
        if(tipoDoenca=="HP"):
            HP += 1
        if(tipoDoenca=="CO"):
            CO += 1
        if(tipoDoenca=="AS"):
            AS += 1
        if(tipoDoenca=="NP"):
            NP += 1
print("\nA quantidade de pessoas do sexo feminino é: ",sexoF,"\nA quantidade de pessoas do sexo masculino é: ",sexoM,"\nA quantidade de pessoas que possuem Diabetes é: ",DB,"\nA quantidade de pessoas que possuem Hipertensão é: ",HP,"\nA quantidade de pessoas que possuem Colesterol Alto é: ",CO,"\nA quantidade de pessoas que possuem Asma é: ",AS,"\nA quantidade de pessoas que não possuem nenhuma doença é: ",NP)