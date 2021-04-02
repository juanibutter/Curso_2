#Funciones filter

#Vamos a suponer que queremos crear una funcion que nos devuelva los numeros pares de una lista
"""
def num_par(num):
    if num % 2==0:
        return True
"""

#Forma de optimizar con lambda
"""
numeros=[1,4,6,9,14,17,26,55,67,100]

print(list(filter(lambda num_par:num_par%2==0, numeros)))
"""

#Vamos a utilizar filter para filtrar objetos. En este caso para que nos imprima auqellos empleados con $50000

class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
    
lista_empleados=[
empleado("Juan", "Python Developer", 95000),
empleado("Ivana", "RRHH", 50000),
empleado("Ariel", "PHP Back-end Developer", 45000),
empleado("Sabrina", "PHP Front-end Developer", 45000),
empleado("Macarena", "Android Developer", 100000),
empleado("Claudio", "CEO", 250000),
empleado("Sofía", "R+D", 49000)
]

salarios_altos=filter(lambda Empleados:Empleados.salario>50000, lista_empleados )

for a in salarios_altos:
    print(a)

