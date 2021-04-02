from tkinter import *
from tkinter import filedialog

#Como abrir archivos. Tambien especificamo la ruta y...
#...el tipo de archivos(nos pide una tupla asique tenemos que abrir paréntesis de vuelta)[Se precisan..
#...2 parámetros como mínimo]

root=Tk()

def abrir_archivo():
    archivo=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Archivos pdf","*.pdf"),
    ("Ficheros word","*.doc"),("Todos los archivos","*.*")))
    print(archivo)

Button(root, text="Abrir archivo", command=abrir_archivo).pack()




root.mainloop()