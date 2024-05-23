def CalcAno(a):
    return a%4==0

while True:
    print(CalcAno(int(input("Digite ano: "))))
    if input("Deseja continuar S/N: ").upper() == "N":
        break