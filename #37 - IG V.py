#Widgets text y button
from tkinter import *

raiz=Tk()

myframe=Frame(raiz, width=1280, height=720)
myframe.pack()

#Cuadros

minombre=StringVar()#Esto tiene que ver con el boton

cuadronombre=Entry(myframe,textvariable=minombre)
cuadronombre.grid(row=0, column=1)
cuadronombre.config(fg="red", justify="center")

cuadroapellido=Entry(myframe)
cuadroapellido.grid(row=1, column=1)
cuadroapellido.config(fg="red", justify="center")

cuadropass=Entry(myframe)
cuadropass.grid(row=2, column=1)
cuadropass.config(fg="red", justify="center",show="#")

cuadroedad=Entry(myframe)
cuadroedad.grid(row=3, column=1)
cuadroedad.config(fg="red", justify="center")

cuadrocomentarios=Text(myframe, width=16, height=5) #Acá creamos un cuadro de comentarios(por defecto es muuuuy grande)..
#..por eso lo limitamos con "width" y "height"
cuadrocomentarios.grid(row=4, column=1,pady=14,padx=14 )
scrollvertical=Scrollbar(myframe, command=cuadrocomentarios.yview)
#Creamos una barra de movimiento, el comando es "Scrollbar". Los parámetros son primero a donde va en general, luego...
#...con el "command" la ubicacion mas especifica y si se mueve de manera vertical u horizontal(yview/xview)
scrollvertical.grid(row=4, column=2, sticky="nsew") #Con esto hacemos que se muestre o aparezca la barra de movimiento
#Con el parametro "sticky" hacemos que la barra se adapte al tamaño del texto
cuadrocomentarios.config(yscrollcommand=scrollvertical.set)#Con este comando hacemos que la barra indique en que punto...
#...nos encontramos en el panel/cuadro(esto es para la barra vertical. Para la horizontal es "xscrollcommand")


#Labels

nombrelabel=Label(myframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="e",pady=14,padx=14)

apellidolabel=Label(myframe, text="Apellido:")
apellidolabel.grid(row=1, column=0, sticky="e",pady=14,padx=14)

passlabel=Label(myframe, text="Password:")
passlabel.grid(row=2, column=0, sticky="e",pady=14,padx=14)

edadlabel=Label(myframe, text="Edad:")
edadlabel.grid(row=3, column=0, sticky="e",pady=14,padx=14)

commentslabel=Label(myframe, text="Comentarios:")
commentslabel.grid(row=4, column=0, sticky="e",pady=14,padx=14)

def codigoboton():
    minombre.set("Kiwi") #Para darle la funcionalidad al boton de abajo

botonenvio=Button(raiz, text="Enviar", command=codigoboton)#Con este comando creamos botones(El "command" es para...
#...agregarle funcion al boton, es decir, que realice la tarea que queremos(mirar arriba de este comando))

botonenvio.pack()





raiz.mainloop()