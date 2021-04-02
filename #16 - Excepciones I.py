#Las excepiones son errores que ocurren durante la ejecución de un programa. Sintaxis correcta, pero sin embargo ocurre "algo inesperado".
#Si el programa es chiquito y de juguete como este no pasa nada, pero puede llegar a ser de mucha gravedad si es un programa muy grande.
#Este tipo de errores se pueden evitar con un "manejo o control de excepciones"
print("""
*********************
*** Excepciones I ***
*********************\n
""")
def suma(numuno, numdos):
    return numuno+numdos

def resta(numuno, numdos):
    return numuno-numdos

def multiplica(numuno, numdos):
    return numuno*numdos

def divide(numuno, numdos):
    try: #Ponemos el try, para que se haga pero....
        return numuno/numdos
    except ZeroDivisionError:   #...Añadimos un except para poder salvar el error
        print("Es imposible dividir por 0")
        return"Operación erronea"
#El error que puede ocurrir es que alguien quiera dividir un numero por 0, lo cual es un error matemático, por eso puede ser inesperado.

numuno=int(input("Introduce un número: "))
numdos=int(input("Introduce otro número: "))

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
