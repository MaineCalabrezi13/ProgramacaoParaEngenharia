#Escrever um algoritmo para ler dois valores e escolher a operação matemática desejada (adição, subtração, multiplicação e divisão). Ao final exibir o resultado.

valor1 = float(input("Digite valor 1: "))
valor2 = float(input("Digite valor 2: "))
print(" ")
print("###########################")
opcao = input("Escolha opção e operação: ")
print(" | + | - | x | / |")

if opcao == "+":
    soma = valor1+valor2
    print("O resultado é: ",soma)
elif opcao =="-":
   subtracao = valor1-valor2    
   print("O resultado é: ",subtracao) 
elif opcao =="x":
    multiplicacao = valor1*valor2
    print("O resultado é: ",multiplicacao)
elif opcao =="/":
    divisao= valor1/valor2
    print("O resultado é: ",divisao)
else:
    print("Operação inválida")



