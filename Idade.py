#Faça um Programa Python que peça a idade de 10 pessoas, armazene  a informação na sua respectiva lista. Imprima a lista das idades na ordem menor para maior.
ordem=[]
Lista_idade=[]
for i in range(0,4):
    idade = int(input("Digite idade: "))
    Lista_idade.append(idade)


Lista_idade.sort(reverse = False)
print("Idades do menor para maior: ",Lista_idade)

