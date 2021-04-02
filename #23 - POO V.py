print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
#Herencia III. Funciones "super()" e "isinstance()"
class persona():
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.resindencia=residencia
    
    def descripcion(self):
        print("Nombre:",self.nombre,"\nEdad:",self.edad,"\nLugar de residencia:",self.resindencia)

class empleado(persona):
    def __init__(self,salario,antigüedad):
        self.salario=salario
        self.antigüedad=antigüedad


Antonio=persona("Antonio",55,"España") #Sin funciones. No podemos utilizar la clase empleado.
Antonio.descripcion()