D={}

n = int(input("Quantos funcionários deseja cadastrar: "))

for i in range(n):
    cod = input("Digite código do funcionário: ")
    nome = input("Digite nome do funcionário: ")
    D.update({cod:nome})

excluir = input("Digite código para a exclusão do funcionário: ")
if excluir in D:
    D.pop(excluir)
else:
    print("Código inexistente")
 
print("Lista de funcionário atualizad: ",D)
