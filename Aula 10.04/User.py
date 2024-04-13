#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = input("Digite nome de usuario: ")
    senha = input("Digite senha de usuario: ")
    if (senha==user):
        print("Senha não pode ser igual ao nome de usuario")
    else:
        break