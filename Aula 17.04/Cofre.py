#Desenvolva um script Python onde o usuário necessita digitar a senha de um cofre, esta senha é numérica (987654), enquanto os valores digitais não forem corretos, o programa deverá pedir novamente informando que o valor está incorreto, assim que estiver correto, informar “cofre aberto”.

while True:
    senha = int(input("Digite senha do cofre: "))

    if(senha!=987654):
        print("Digite novamente, valor está incorreto")
    elif (senha==987654):
        print("Cofre aberto")
        break
