#Serializacion de objetos
import pickle

class vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,
        "\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

auto1=vehiculos("Ferrari","F12berlinetta")

auto2=vehiculos("Porsche","911 Carrera s")

auto3=vehiculos("Lamborghini","Huracán Evo RWD")

autos=[auto1, auto2, auto3] #Colección de objetos

fichero=open("#31_misautos", "wb")

pickle.dump(autos, fichero)

fichero.close()

del(fichero)

ficheroabrir=open("#31_misautos", "rb")

misauticos=pickle.load(ficheroabrir)

ficheroabrir.close()

for a in misauticos:
    print(a.estado())

