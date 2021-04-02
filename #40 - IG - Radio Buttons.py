from tkinter import *

root=Tk()

varop=IntVar()#Con esto vamos a poder darle valores para que se puedan seleccionar, de lo contrario..
#..aparecen seleccionados por defecto

Label(root, text="Género:").pack()
def imprimir():
    if varop.get()==1:
        etiqueta.config(text="Elegiste Masculino")
    elif varop.get()==2:
        etiqueta.config(text="Elegiste Femenino")
    else:
        etiqueta.config(text="Elegiste Otros")

#label(root, text="Género:").pack()


Radiobutton(root, text="Masculino",variable=varop, value=1, command=imprimir).pack() #Asi creamos los radiobuttons
Radiobutton(root, text="Femenino",variable=varop, value=2, command=imprimir).pack()
Radiobutton(root, text="Otros",variable=varop, value=3, command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()







root.mainloop()