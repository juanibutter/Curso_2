print("********************")
print("*** TERCER CLASE ***")
print("********************\n")

lista=["Messi","Ronaldo","Neymar","Mbappé"]
print(lista[:]) #Cuenta de izq. a der. desde 0 y si ponemos entre corchetes un número negativo empieza de d. a izq. pero desde 1.
print(lista[0:2]) #Porción de la lista
print(lista[2:3]) #Porción de la lista (excluye al ultimo elemento escrito, en este caso el tres)
print(lista[:2]) #Desde el ppio hasta el elemento dos (siempre excluye el último num.)
print(lista[2:]) #Desde el segundo elemento hasta el final (siempre excluye el último num.)
print(lista[1]) #Imprime el elemento deseado
print("")
lista.append("Rashford") #Para agregar un elemento, siempre al final
print(lista[:])
print("")
lista.insert(2,"Cavani") #Para agregar un elemento en el lugar deseado
print(lista[:])
print("")
lista.extend(["Koke","Pulisic","Ibrahimovic"]) #Para agregar varios elementos
print(lista[:])
print("")
print(lista.index("Koke")) #Para conocer la posición de un elemento
print("")
print("Neymar" in lista) #Para saber si un elemento se encuentra en mi lista}
print("Neymarrrr" in lista)
print("")
lista2=["Juan",28,True,1.70] #Lista de distintos elementos
print(lista2)
print(lista2[3])
lista2.remove(True) #Para quitar elementos (cualquiera sea)
print(lista2)
lista2.remove("Juan")
print(lista2)
lista2.pop() #Para eliminar el último elemento de la lista
print(lista2)
print("")
lista3=[1,2,3,4,5,6,7,8]
print(lista3)
lista4=lista+lista2+lista3 #Para poder combinar listas
print(lista4)
print("")
lista5=[8,7,6,5,4,3,2,1]*4 #Para repetir el número de veces que quiera la lista, peeeero en la misma lista (es como si se sumara a si misma una x cantidad de veces)
print(lista5)





