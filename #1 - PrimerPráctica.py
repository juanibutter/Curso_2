print("********************")
print("*** PRIMER CLASE ***")
print("********************\n")
print("Primera vez:\n")
def mensaje(): #Declaración de la función
    print("Primer práctica curso #2")
    print("Bloque de código")           #Cuerpo de la función
    print("Utilización de funcion")
mensaje() #Llamada de la función; se pueden llamar las veces que se quiera

print("\nSegunda vez:\n")
mensaje() #Segunda llamada

print("\n\n")

print("*********************")
print("*** SEGUNDA CLASE ***")
print("*********************\n")

def suma(numuno, numdos):
    print(numuno+numdos)
suma(4,6)
suma(3,3)
suma(11,19)

print("\nCon función return, parte1:\n")

def suma(numuno, numdos):
    resultado=numuno+numdos
    return resultado
print (suma(4,6))
suma(3,3)
print (suma(11,19))

print("\nCon función return, parte2:\n")

def suma(numuno, numdos):
    resultado=numuno+numdos
    return resultado
almacenador=suma(9,9)
print(almacenador)
