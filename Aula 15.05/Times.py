#Dicionario
def existeNoDicionario(d,p):
    result = False
    for i in d.values():
        if i == p:
            result =  True
            break
    return result

times = {1: "Criciuma",  
         2: "Avai",  
         3: "Marcilio Dias", 
         4: "Joinville", 
         5: "Figueirense",  
         6: "Chapecoense",  
         7: "Brusque", 
         8: "Metropolitano",
         9: "Hercílio Luz", 
         10: "Inter de Lages" }

times.update({11 : "Gremio"})
print("Incluir time: ",times)
#for i in times:
#    if times[i] == "Joinville":
#        print("Joinville está cadastrado")
#        break
#    elif i == len(times):
#        print("Joinville não está cadastrado")


if existeNoDicionario(times, "Joinville"):
    print("Joinville está cadastrado")
else:
    print("Joinville não está cadastrado")