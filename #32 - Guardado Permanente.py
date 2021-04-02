import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva. Su nombre es:",self.nombre)

    def __str__(self):  #Esto es para convertir a string info
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:

    personas=[]
    
    def  __init__(self):
        lista_de_personas=open("#32_lista_fichero_externo","ab+") #Con el constructor creamos el fichero y seteamos para...
        lista_de_personas.seek(0)                                 #...agregar info binaria con el "ab+"
#Lo de arriba es para que cuando termine de leer vuelva de nuevo al ppio
        try:
            self.personas=pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero aún está vacío")
        finally:
            lista_de_personas.close()
            del(lista_de_personas)

    def agregar_personas(self,p):
        self.personas.append(p)
        self.guardar_personas_en_fichero_externo()

    def mostrar_personas(self):
        for p in self.personas:
            print(p)

    def guardar_personas_en_fichero_externo(self):
        lista_de_personas=open("#32_lista_fichero_externo","wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del(lista_de_personas)

    def mostrar_info_fichero_externo(self):
        print("La información del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

mi_lista=ListaPersonas()
persona=Persona("Natasha","Femenino",23)
mi_lista.agregar_personas(persona)
mi_lista.mostrar_info_fichero_externo()