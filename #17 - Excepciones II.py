print("""
*********************
*** Excepciones I ***
*********************\n
""")
print("Primera parte de excepciones:\n")
def suma(numuno, numdos):
    return numuno+numdos

def resta(numuno, numdos):
    return numuno-numdos

def multiplica(numuno, numdos):
    return numuno*numdos

def divide(numuno, numdos):
    try:
        return numuno/numdos
    except ZeroDivisionError:
        print("Es imposible dividir por 0")
        return"Operación erronea"

while True: #(Leer dsps del comentario de abajo)Al agregar el "while True" con el "break", logramos que el programa se vuelva a ejecutar en esta parte
    try: #Corrige en parte el value error, y aunque el programa sigue funcionando, no deberia ser de esta forma. (Mirar el comentario de arriba)
        numuno=int(input("Introduce un número: "))
        numdos=int(input("Introduce otro número: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")

oper=input("Introduce la operación a realizar(suma, resta, multiplica, divide): ")

if oper=="suma":
    print(suma(numuno, numdos))
elif oper=="resta":
    print(resta(numuno, numdos))
elif oper=="multiplica":
    print(multiplica(numuno, numdos))
elif oper=="divide":
    print(divide(numuno, numdos))
else:
    print("Operación no disponible.")

print("Operación ejecutada. Continuemos: ")
