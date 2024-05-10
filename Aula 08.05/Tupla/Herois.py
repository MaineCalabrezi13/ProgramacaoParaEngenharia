#Crie uma tupla com os nomes dos super-heróis que devem participar do Filme Vingadores seguindo a ordem:

Nome_herois = ('Homem de Ferro', 'Capitão América','Thor', 'Hulk','Viúva Negra','Gavião Arqueiro')
print(Nome_herois)
#Agora, inclua o Homem-Aranha no final da lista e mostre em qual posição está o Thor. 
Nome_herois = Nome_herois + tuple(["Homem_Aranha"])
print(Nome_herois)
print("A posição do Thor é: ", Nome_herois.index("Thor"))

#Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte do filme Vingadores, então retire-os da lista.

nome = ()

for valor in Nome_herois:
    if valor != "Homem de Ferro" and valor != "Viúva Negra": 
        nome = nome + tuple([valor])

print(nome)


