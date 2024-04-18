#Votos em eleição
Cand1=0
Cand2=0
Cand3=0
Cand4=0
Nulo=0
Branco=0

while True:
    print("***************** MENU *****************\n1 - Maine\n2 - Agnes\n3 - Gustavo\n4 - Augusto\n5 - Voto nulo\n6 - Voto em branco\nS - Encerrar a votação\n**********************************")
    print()
    opcao=input("Digite opção: ").upper()
    if (opcao=="S"):
        break
    else:
        codigo = input("Digite código do cantidato que queira votar: ")
        
        if(codigo=="1"):
            Cand1+=1
        if(codigo=="2"):
            Cand2+=1
        if(codigo=="3"):
            Cand3+=1
        if(codigo=="4"):
            Cand4+=1
        if(codigo=="5"):
            Nulo+=1
        if(codigo=="6"):
            Branco+=1
print("\nTotal de votos para o candidato 1: ",Cand1,"\nTotal de votos para o candidato 2: ",Cand2,"\nTotal de votos para o candidato 3: ",Cand3,"\nTotal de votos para o candidato 4: ",Cand4,"\nTotal de votos em nulo: ",Nulo,"\nTotal de votos em branco: ",Branco)