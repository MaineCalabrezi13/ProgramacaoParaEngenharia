#Escreva um programa que verifique se uma letra digitada é vogal ou consoante. Ou ainda se não está nestes grupos.
letra = input("Digite uma letra: ").upper()

if (letra=="A") or (letra=="E") or (letra=="I") or (letra=="O") or (letra=="U"):
    print("A letra é uma vogal")
elif(letra=="B")or(letra=="C")or(letra=="D")or(letra=="F")or(letra=="G")or(letra=="H")or(letra=="J")or(letra=="K")or(letra=="L")or(letra=="M")or(letra=="N")or(letra=="P")or(letra=="Q")or(letra=="R")or(letra=="S")or(letra=="T")or(letra=="V")or(letra=="W")or(letra=="X")or(letra=="Y")or(letra=="Z"):
 print("A letra é uma consoante")
else: 
    print("Não pertence a nenhum grupo")