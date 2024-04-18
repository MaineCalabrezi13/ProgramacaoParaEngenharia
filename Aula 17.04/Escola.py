#A Secretaria de Educação do Estado está realizando uma pesquisa com estudantes. Fazendo um levantamento de alunos em cada nível escolar, onde:
ContEF1=0
ContEF2=0
ContEM=0
while True:
    print("****************MENU*******************\nEducação Infantil\nEF1 = Ensino Fundamental 1 \nEF2 = Ensino Fundamental 2\nEM  = Ensino Médio\nS = encerrar pesquisa\n******************************************")
    opcao = input("Escolha uma opção: ").upper()
    if (opcao == "S"):
        break

    aluno = input("Digite nome do aluno: ")
    NivelEscolar = input("Digite nível escolar: ").upper()

    if(NivelEscolar=="EF1"):
        ContEF1=ContEF1+1
    if(NivelEscolar=="EF2"):
        ContEF2=ContEF2+1
    if(NivelEscolar=="EM"):
        ContEM=ContEM+1
if ((ContEF1 != 0) or (ContEF2 != 0) or (ContEM != 0)):
    print("A quantidade de crianças no Ensino Fundamental 1 é: ",ContEF1,"\nA quantidade de crianças no Ensino Fundamental 2 é: ",ContEF2,"\nA quantidade de crianças no Ensino Médio é: ",ContEM)


    