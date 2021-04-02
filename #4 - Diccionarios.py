print("********************")
print("*** QUINTA CLASE ***")
print("********************\n")
diccionario={"Argentina":"Buenos Aires","España":"Madrid","Inglaterra":"Londres","Francia":"París","Italia":"Roma","Portugal":"Lisboa"}
print(diccionario["Francia"]) #Para conocer el valor de una clave
print("")
diccionario["Alemania"]="Munich" #Para añadir un elemento
print(diccionario) #Diccionario entero
print("")
diccionario["Alemania"]="Berlín"
print(diccionario) #Para corregir, pero lo sobreescribe
print("")
del diccionario["Portugal"] #Para eliminar un elemento
print(diccionario)
print("")
diccionario2={"Argentina":"Mendoza",28:"Juan","Dorrego":5519}
print(diccionario2)
print("")
tupla=("España","Francia","Inglaterra","Italia")
diccionario3={tupla[0]:"Madrid",tupla[1]:"París",tupla[2]:"Londres",tupla[3]:"Roma"} #Para crear un diccionario desde una tupla
print(diccionario3)
print("")
print(diccionario3["Inglaterra"]) #Para saber un valor
print(diccionario3[tupla[1]]) #Otra manera de conocer un valor
print("")
diccionario4={10:"Messi","Club":"FC Barcelona","País":"Argentina","Champions":[2006,2009,2011,2015]} #Para agregar una tupla además de otras claves y valores
print(diccionario4)
print(diccionario4["Champions"])
print("")
diccionario5={10:"Lionel Messi","Club":"FC Barcelona","Argentina":"Rosario","Champions":{"Años campeón":[2006,2009,2011,2015]}} #Diccionario dentro de un diccionario
print(diccionario5["Champions"])
print("")
print(diccionario5.keys()) #Para imprimir claves
print(diccionario5.values()) #Para imprimir valores
print(len(diccionario5)) #Para imprimir el largo del diccionario
