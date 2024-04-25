#Elabore um script em linguagem Python que contenha uma lista com o nome de 5 dos seus melhores amigos. Mostrar na tela a seguir, cada nome em uma linha separada por meio de estrutura de repetição.
amigos = []

while True: 
    nomes = input("Insira um nome de amigo: ") 
    amigos.append(nomes)
    opcao = input("Deseja cadastrar mais nomes S ou N ? ").upper()
    if opcao == "N":
        break

print ("Lista de amigos : ",amigos)
