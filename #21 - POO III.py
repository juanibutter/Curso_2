print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
#Encapsulamiento en chequeo interno
class Automovil():
    def __init__ (self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequear=self.__chequeoInterno()
        if(self.__enmarcha and chequear):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequear==False):
            return "Algo anda mal. No podemos arrancar el coche."
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)
    
    def __chequeoInterno(self):   #Vamos a agregar un chequeo antes de que arranque el auto
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Automovil()
print(miCoche.arrancar(True))
miCoche.estado()

print("\nPOO parte 2:\n")

miCoche2=Automovil()
print(miCoche2.arrancar(False))
miCoche2.estado()