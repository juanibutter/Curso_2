print("********************")
print("*** CUARTA CLASE ***")
print("********************\n")

tupla=("Juan", 170, 28, 1992)
print(tupla[1])
lista=list(tupla) #Para transformar tupla en lista
print(lista)
print(tupla)
print("")
lista2=["Messi", "Ronaldo", "Neymar", "Ronaldo", "Mbappé"]
tupla2=tuple(lista2) #Para transformar lista en tupla
print(lista2)
print(tupla2)
print("Messi" in tupla2) #Para saber si un elemento se encuentra en la tupla, si es asi, es true, sino false
print(tupla2.count("Ronaldo")) #Para conocer cuantas veces se encuentra un elemento en una tupla
print(len(tupla2)) #Para averiguar la longitud de la tupla
print("")
tupla_unitaria=(7,) #Para las tuplas unitaria es necesario poner una coma al final del elemento
print(len(tupla_unitaria))
print("")
tupla3="BBs", 7, 5, 2 #Es posible crear tuplas sin parentesis, aunque es mas confuso(se llama "empaquetado de tupla")
print(tupla3)
print("")
tupla4=("Armani","Montiel","Borré","Enzo")
arquero, defensor, mediocampista, delantero=tupla4 #Desempaquetado de tuplas
print(tupla4)
print(mediocampista)
print(defensor)
print(delantero)
print(arquero)
