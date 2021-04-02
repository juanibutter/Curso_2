print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
#POLIMORFISMO
class auto():
    def desplazamiento(self):
        print("Un auto se desplaza utilizando 4 ruedas")
class moto():
    def desplazamiento(self):
        print("Una moto se desplaza utilizando 2 ruedas")
class camion():
    def desplazamiento(self):
        print("Un camión se desplaza utilizando 6 ruedas")

def desplazamientovehiculos(vehiculo): #Con esto podemos utilizar polimorfismo
    vehiculo.desplazamiento()

mivehiculo=moto()
desplazamientovehiculos(mivehiculo)