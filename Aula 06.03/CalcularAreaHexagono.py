raio = float(input("Digite o raio do hexágono: "))
comprimento_lado = raio * (3 ** 0.5)
area_triangulo = (3 * (3 ** 0.5) * (comprimento_lado ** 2)) / 2
area_total = 6 * area_triangulo
print(f"A área do hexágono regular com raio ", raio ,"é ", area_total)
