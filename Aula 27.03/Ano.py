#determine se um ano introduzido pelo usuário é ou não bissexto. 

ano = int(input("Digite ano: "))

if (ano % 4==0)or (ano %100==1)or(ano %400==0):
    print("Ano bissexto")
else:
    print("O ano não é bissexto")


