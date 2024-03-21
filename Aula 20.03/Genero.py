#Elabore um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M – Masculino ou Sexo Não Informado.

sexo = input("Digite gênero (M/F): ")

if (sexo=="M")or(sexo=="m"):
    print("Masculino")
elif (sexo=="F")or(sexo=="f"):
    print("Feminino")
else: 
    print("Sexo Não Informado")
