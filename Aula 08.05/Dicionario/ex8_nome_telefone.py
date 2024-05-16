#criar um dicionario vazio
agenda  = {}

while True:
    nome       = input("Digite nome : ")
    telefone   = int(input("Digite telefone : "))  
    #incluir elemento no dicionario 
    agenda[nome] = telefone
    opcao = input("Deseja continuar S ou N ? ").upper()
    if opcao == "N":
        break
  
print ("Lista de contatos : ", agenda)

novonome     = input("Qual nome deseja incluir ? ")
novotelefone = int(input("Qual ptelefone deseja incluir ? "))
#incluir novo elemento do dicionario
agenda.update({novonome:novotelefone})

print ("Lista atualizada: ", agenda)

