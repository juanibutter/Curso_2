print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
#Con funciones
print("SEGUNDA PARTE:\n")

class persona1():
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.resindencia=residencia
    
    def descripcion(self):
        print("Nombre:",self.nombre,"\nEdad:",self.edad,"\nLugar de residencia:",self.resindencia)

class empleado1(persona1):
    def __init__(self,salario,antigüedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado) #Sirve para poder heredar de una clse
        self.salario=salario
        self.antigüedad=antigüedad
    def descripcion(self):
        super().descripcion()
        print("Salario Anual:",self.salario,"\nAntigüedad:",self.antigüedad,"años")

Eusebio=empleado1(150000,9,"Eusebio",45,"Portugal")
Eusebio.descripcion()
print(isinstance(Eusebio,empleado1)) #Esto sirve para saber si un objeto pertenece a una clase o no.