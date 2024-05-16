#Dicionário

estados = {"Acre" : "Capital Rio Branco",  
            "Alagoas" : "Capital Maceió", 
            "Amazonas": "Capital Manaus",  
            "Bahia" : "Capital Salvador", 
            "Distrito Federal" : "Capital Brasília",  
            "Santa Catarina" : "Capital Florianópolis", 
            "Rio Grande do Sul" : "Capital Porto Alegre",
            "Paraná" : "Capital Curitiba", 
            "São Paulo" : "Capital São Paulo",
            "Minas Gerais" : "Cuiabá", 
            "Rio de Janeiro" : "Rio de Janeiro",
            "Tocantins": "Capital Palmas"}

#incluir novo ESTADO e CAPITAL
estados.update({"Maine":"Calabrezi"})
print("Estados/Capitais + Adicionado: ",estados)

#Ver se tem cadastro
if "Distrito Federal" in estados:
    print("Distrito Federal está cadastrato")
else:
    print("Distrito Federal não está cadastrato")

#Trocar dados
estados.update({"Minas Gerais":"Belo Horizonte"})

print("Trocas Minas Gerais por Belo Horizonte: ",estados)


