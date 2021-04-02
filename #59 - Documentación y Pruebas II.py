def area_triangulo(base, altura):
    
    """
    Calcula el área de un triángulo dado
    >>> area_triangulo(3,6)
    'El área del triángulo es: 9.0'
    
    >>> area_triangulo(5,8)
    'El área del triángulo es: 20.0'

    >>> area_triangulo(6,6)
    'El área del triángulo es: 18.0'
    """
    #Así es como realizamos la prueba(todo lo que está entre comillas triples)
    return "El área del triángulo es: " + str((base*altura)/2)
    #Hay que tener en cuenta quepara hacer las prubas hay que escribir todo de manera perfecta,...
    #...incluso las comillas los puntos, los dos puntos. T O D O.

import doctest
doctest.testmod()