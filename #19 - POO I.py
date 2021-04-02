print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
class Automovil():  #El nombre de la clase se pone la primera letra en mayúscula
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self): #Este "def" es un método no una función. Y sirve para cambiar el comportamiento del "en matcha"
        self.enmarcha=True #Tenemos que poner self delante para poder cambiar el valor
    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

miCoche=Automovil()    #Esto es una instanciación de clase(crear objeto)

print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene",miCoche.ruedas,"ruedas")
miCoche.arrancar() #Se llama al método para que cambien el valor de "enmarcha"
print(miCoche.estado())

#NUESTRA CLASE AUTOMOVIL TIENE 4 PROPIEDADES Y 2 COMPORTAMIENTOS.
print("\nPOO parte 2:\n")   #Creamos el segundo objeto

miCoche2=Automovil()
print("El largo del coche es:",miCoche2.largoChasis)
print("El coche tiene",miCoche2.ruedas,"ruedas")
print(miCoche2.estado())