#Documentación

class areas:

    def area_cuadrado(lado):
    
        """Esta función calcula el área de un cuadrado, 
        al multiplicar lado por lado""" #Esta sería la famosa documentación (se usa la triple """), que sirve... 
        #...para comentar de manera más exquisita que con los numerales, ya que permite comentarios multilinea
    
        return "El área del cuadrado es:" + str(lado*lado)

    def area_triangulo(base,altura):

        """Cálcula el área de un triángulo multiplicando base por altura y 
        dividiendo el resultado entre dos"""

        return "El área del triángulo es:" + str((base*altura)/2)

print(areas.area_cuadrado(5))
print(areas.area_triangulo(5,2))

print(areas.area_cuadrado.__doc__)
#Con esto logramos que se imprima el comentario/documentación que le agregamos,sin la función obviamente

help(areas.area_cuadrado)
#Esta es otra manera de imprimir la documentación aunque de manera más detallada incluso

help(areas.area_triangulo)
#Cuando la función está dentro de una clase, si o si hay que llamar primero la clase y luego la función
#Es decir "areas.area_cuadrado", se llama la clase, luego se pone el punto y se llama a la función

help(areas)
#Esto ya es una ayuda para saber como funciona la clase en general. A la cuál también podemos comentar