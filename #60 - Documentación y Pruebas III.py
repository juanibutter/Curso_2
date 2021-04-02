import math

def raizcuadrada(listanum):
    """
    La función devuelve una lista con la
    raíz cuadrada de los elementos numéricos
    pasados por parámetros en otra lista
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]
    >>> lista=[]
    >>> for i in [4, -9, 16, 50, -90, 125]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """#Los tres puntos sirven para anidar expresiones en las pruebas, en este caso para indicar que lo..
    #..que sigue del bucle for va identado y le pertenece, Esto es solo para demostración, ya que se podría..
    #..simplificar las expresiones y evitarse un dolor de cabeza totalmente innecesario
    #MUY IMPORTANTE NOTAR QUE LA ÚLTIMA LINEA DE PRUEBAS CONTEMPLA UN ERROR Y ESA ES LA SINTAXIS..
    #..CORRECTA A UTILIZAR PARA UTILIZARLA COMO COMODÍN (NOTAR LOS TRES PUNTOS)
    return [math.sqrt(n) for n in listanum] #Asi logramos que nos devuelva una lista con las raices cuadradas

#print(raizcuadrada([121,169,36,100,49,25]))


import doctest
doctest.testmod()