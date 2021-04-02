print("""
**********************
*** GENERADORES II ***
**********************\n""")

#Estamos viendo el método yield from ahora, recordemos que en este caso el objetivo es acceder a un subelemento de un elemento. Los dos primeros código son de ejemplo
print("Elementos:\n")
def ciudades(*cities): #Cuando ponemos un asteristo delante del argumento le estamos indicando al programa que va a recibir un num indeterminado de elementos y además en forma de tupla.
    for elemento in cities:
        yield elemento
#Bien, acabamos de definir el elemento, próximamente accederemos al subelemento
impre_ciudades=ciudades("Roma","Madrid","París","Londres","Lisboa")
#imprimimos los dos primeros
print(next(impre_ciudades))
print(next(impre_ciudades))
print("\nSubElementos:\n")
#Ahora veremos los subelementos
def comunidades(*commun):
    for element in commun:
        for subelem in element: #Con este bucle anidado accedemos al subelemento(las letras que forman la palabra)
            yield subelem
impre_comuni=comunidades("Barcelona","Madrid","Galicia","Valencia","La Coruña")
print(next(impre_comuni))
print(next(impre_comuni))
#AHORA SI VEREMOS EL "YIELD FROM"
print("\nYIELD FROM:\n")
def equipos(*clubes):
    for elemento_uno in clubes:
        yield from elemento_uno #Con esto nos ahorramos un poco de código, lo que lo hace más eficiente y menos enquilombado
teams=equipos("River","Boca","Independiente","Racing","San Lorenzo")
print(next(teams))
print(next(teams))
