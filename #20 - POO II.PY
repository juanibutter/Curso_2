print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
class Automovil(): #Estas son las características del estado inicial
    def __init__ (self): #Esto es un constructor. Sirve para declarar el estado inicial de un objeto. Cuando lo hacemos...
                         #...es importante que les agreguemos "self." a las propiedades.
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Al agregar los 2 guiones bajos logramos encapsulamiento. Esto es para que una prop. no pueda ser modificada desde fuera de la clase
        self.__enmarcha=False
    
    def arrancar(self,arrancamos): #con el "arrancamos" logramos que el metodo arrancar reciba un parámetro y lo que estaba en estado pasa a este método
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)
        

miCoche=Automovil()
print(miCoche.arrancar(True))
miCoche.estado()

print("\nPOO parte 2:\n")

miCoche2=Automovil()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2 #Esto es solo para ver cosas que no deberían ser permitidas(modificar un objeto). Por eso vamos a encapsular
miCoche2.estado()
#Hemos optimizado el código al pasar lo que antes estaba en "estado" a "arrancar". Modificar el método "estado" y poner...
#..."prints" en "miCoche.arrancar()" y sacar los prints de "miCoche.estado". Y borrar los "prints" anteriores del método "estado".
#IMPORTANTE---------->COMPARAR CÓDIGO CON "#19 - POO I.PY"