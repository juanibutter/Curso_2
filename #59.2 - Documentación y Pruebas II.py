def checkmail(usermail):
    """
    La función checkmail se encarga de comprobar que
    el mail ingresado tenga "@", que no sea más de una
    y que no esté al final.
    >>> checkmail('kiwi@python.com')
    True
    >>> checkmail('kiwipython.com@')
    False
    >>> checkmail('kiwipython.com')
    False
    >>> checkmail('ki@wi@python.com')
    False
    """
    arroba=usermail.count('@')#Esto examina y cuenta la cantidad de "@"" que hay
    if arroba!=1 or usermail.rfind('@')==(len(usermail)-1) or usermail.find('@')==0:
        return False
    else:
        return True

import doctest
doctest.testmod()