"""Funciones lambda

def area_triangulo(base, altura):
    return (base*altura)/2

trian1=area_triangulo(5, 7)
trian2=area_triangulo(9, 6)

print(trian1)
print(trian2)
"""

"""#Asi se podria usar una funcion lambda
area_triangulo=lambda base,altura:(base*altura)/2
#En funciones más complejas con bucles o condicionales no podremos utilizar funciones lambda
print(area_triangulo(6,6))
print(area_triangulo(8,5))
tri1=area_triangulo(7,7)
tri2=area_triangulo(4,4)
print(tri1)
print(tri2)
"""

"""#Dos maneras de utilizar una funcion lambda exponencial
"al_cubo=lambda numero:numero**3"
al_cubo=lambda numero:pow(numero, 3)
print(al_cubo(15))
"""

destacarcomision=lambda comision:"$¡{}!".format(comision)
comision_ana=155000
print(destacarcomision(comision_ana))