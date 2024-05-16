#tupla

series = ("Black Mirror", "Breaking Bad", "Friends", "Game of Thrones", "The Big Bang Theory", "House",  "The Last of Us", "One Piece","Grey's Anatomy", "Stranger Things")

serie = series + tuple(["teste"])

print(series)
print("Adicionando One Piece: ",serie)
print("Posoção da série One Piece: ", serie.index("One Piece") )

nome = ()

for valor in serie:
    if valor != "House":
        nome = nome + tuple([valor])
print("Tirar House: ",nome)
