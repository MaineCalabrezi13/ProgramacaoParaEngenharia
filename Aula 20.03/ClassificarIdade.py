#Escrever um algoritmo para ler nome e idade de uma pessoa e verificar a classificação:

nome = input("Digite nome: ")
idade= int(input("Digite idade: "))

if (idade>=0)and(idade<=3):
    print("Bebe")
elif (idade>=4)and(idade<=11):
    print("Criança")
elif(idade>=12)and(idade<=17):
    print("Adolescente")
elif(idade>=18)and(idade<=60):
    print("Adulto")
elif(idade>=61)and(idade<=99):
    print("3º idade")

