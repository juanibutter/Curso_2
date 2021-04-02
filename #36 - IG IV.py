#Introducir cuadros de texto
from tkinter import *

raiz=Tk()

myframe=Frame(raiz, width=1280, height=720)
myframe.pack()

cuadronombre=Entry(myframe) #Asi creamos el cuadro de texto
cuadronombre.grid(row=0, column=1)
cuadronombre.config(fg="blue", justify="center")

cuadroapellido=Entry(myframe)
cuadroapellido.grid(row=1, column=1)
cuadroapellido.config(fg="blue", justify="center")

cuadropass=Entry(myframe)
cuadropass.grid(row=2, column=1)
cuadropass.config(fg="blue", justify="center",show="#") #Con el parametro "show" logramos que no se muestre lo que se...
#...está escribiendo sino que quede oculto por (en este caso) "#". Muy importante para los passwords

cuadroedad=Entry(myframe)
cuadroedad.grid(row=3, column=1)
cuadroedad.config(fg="blue", justify="center")

#Hemos creado con "grid", una grilla para ubicar mejor los elementos

nombrelabel=Label(myframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="e",pady=14,padx=14)

apellidolabel=Label(myframe, text="Apellido:")
apellidolabel.grid(row=1, column=0, sticky="e",pady=14,padx=14)

passlabel=Label(myframe, text="Password:")
passlabel.grid(row=2, column=0, sticky="e",pady=14,padx=14)

edadlabel=Label(myframe, text="Edad:")
edadlabel.grid(row=3, column=0, sticky="e",pady=14,padx=14)
#Con el parametro sticky(puntos cardinales) ubicamos donde queremos que este el texto del label
#"pady" y "padx" nos sirven para separar los elementos, el primero vertical el segundo horizontal

raiz.mainloop()