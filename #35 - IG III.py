from tkinter import *

#PRÁCTICA LABELS

root=Tk()

myframe=Frame(root, width="650", height="500")
myframe.config(bg="black")
myframe.pack()

#Si en vez de texto queremos poner una imagen utilizamos el siguiente código(sin los corchetes y sin llaves):
#[myimage=PhotoImage(file="ruta_de_la_imagen" debe ser".png/gif")]
#---->{Label(myframe,image=myimage).place(x=100, y=100)}

mylabel=Label(myframe,text="Que divertido es Python",fg="red",font=("Comic Sans MS", 18)) 
#Acá utilizamos el label, especificamos el...
#...contenedor padre "myframe" y luego las opciones
#"fg":color de fuente. "font":tipo de letra y tamaño
mylabel.place(x=100, y=100)  #Le ponemos el lugarcon (x=numero, y=numero)...
#...para evitar usar empaquetado y que arruine la dimension de la ventana

#ATENCIÓN: es posible usar el sigiuente código(sin las llaves)---->
#--->{Label(myframe,text="Que divertido es Python").place(x=100, y=100)} para ahorrar espacio y si no vamos a utilizar...
#...ninguna variable de tipo label




root.mainloop()