Vf = float(input("Digite valor final: "))
n = int(input("Digite número de meses que pretende deixar o dinheiro: "))
i = int(input("Digite rendabilidade: "))

pv = (Vf/(1+i)**n)
print("Você deve investir inicialmente: ", pv)