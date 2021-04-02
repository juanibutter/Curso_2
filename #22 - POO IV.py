print("""
****************************************
*** PROGRAMACIÓN ORIENTADA A OBJETOS ***
****************************************\n""")
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

class moto(vehiculos): #Para crear una herencia de una clase se le pone entre paréntesis la clase que queremos que herede
    granwheelee=""
    def wheelee(self):
        self.granwheelee="Voy Haciendo wheelee"
    
    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,
        "\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.granwheelee)

mimoto=moto("Ducati", "959 Panigale")
mimoto.wheelee()
mimoto.estado()

class furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta esta vacía"

mifurgoneta=furgoneta("Renault", "Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))

class v_elec(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarenergia(self):
        self.cargando=True

class bici_elec(v_elec,vehiculos):  #Atento!!, la herencia solo le da importancia al primer elemento que ponemos
    pass

mibici=bici_elec("Orbe","ZRW-9350")