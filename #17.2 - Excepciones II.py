print("""
*********************
*** Excepciones I ***
*********************\n
""")
print("\nSegunda manera de generar excepción:\n")

def divide():
    try:
        numuno=float(input("Introduce un número: "))
        numdos=float(input("Introduce otro número: "))
        print("El resultado de la división es: ",round(numuno/numdos,2))
    except ValueError:
        print("El valor introducido es erróneo.")
    except ZeroDivisionError:   #Lo bueno es que se pueden agregar varias "except" en Python, por lo que podemos anidarlas en un solo "try"
        print("No se puede dividir por 0.")
    finally:    #Lo que introdujamos en la clausala "finally" siempre se ejecutara(aunque en este caso no influye)
        print("\nCálculo finalizado.")
divide() #Cuando utilizamos una función hay que llamarla sino no funciona


def divide():
    try:
        numuno=float(input("Introduce un número: "))
        numdos=float(input("Introduce otro número: "))
        print("El resultado de la división es:",(round(numuno/numdos,2)))
    except:     #Es posible usar solo un except para evitar anidar 5,10, o más(por ejemplo). Y que los errores no interrumpan, aunque nunca se sabra cuál fue el error
        print("\nHa ocurrido un error.")
    print("\nCálculo finalizado.")
divide()
