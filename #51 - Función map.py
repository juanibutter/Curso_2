#Función map

class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
    
lista_empleados=[
empleado("Juan", "Python Developer", 65000),
empleado("Ivana", "RRHH", 60000),
empleado("Sabrina", "PHP Developer", 40000),
empleado("Macarena", "Android Developer", 100000),
empleado("Sofía", "CEO", 250000),
empleado("Claudio", "R+D", 50000),
]

#Vamos a crear una función que le establezca una comisión al empleado
def calculocomision(empleado):
    if (empleado.salario<=50000):
        empleado.salario=empleado.salario*1.15
    return empleado
#Y ahora si usamos la función map
listacomision=map(calculocomision, lista_empleados)

for employee in listacomision:
    print(employee)

