#Faça um script em Python que leia nome, a altura e o sexo de 50 pessoas, após calcule e mostre o seu peso ideal, utilizando as seguintes fórmulas
sexoF = 0
sexoM =0
for i in range(1,5):
    nome = input("DIgite seu nome: ")
    altura = float(input("Digite sua altura: "))
    sexo = input("Digite seu sexo (M/F): ").upper()
    
    if(sexo=="M"):
        sexoM = sexoM+1
        PesoIdeal = ((72.7 * altura)-58)
        print("O peso ideal é: ",PesoIdeal)
    else: 
        sexoF = sexoF+1
        PesoIdeal=((62.1 * altura) - 44.7)
        print("O peso ideal é: ",PesoIdeal)
print("A quntidade de pessoas do sexo feminino é: ",sexoF,"\nA quantidade de pessoas do sexo masculino é: ",sexoM)



