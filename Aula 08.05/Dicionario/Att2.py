
D={
    1 : 'Maine',
    2 : 'Agnes',
    3 : 'Gustavo',
    4 : 'Augusto',
}
    
excluir = int(input("Digite código para a exclusão do funcionário: "))
    
if excluir in D:
    for indice, nome in D.items():
        print(f"{indice}: {nome}")
        break

    