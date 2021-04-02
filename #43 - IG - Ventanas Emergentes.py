from tkinter import *
from tkinter import messagebox
#Necesitamos importar esta libreria porque no forman parte de tkinter por defecto

root=Tk()

#-----------------------------------------------------------------------------------------------------

def infoadicional():
    messagebox.showinfo("Información del programa", "Práctica de Python 2021")

def licencia():
    messagebox.showwarning("Licencia", "KIWI Inc. Todos los derechos reservados")

def salida():
    #valor=messagebox.askquestion("Salir", "Deseas cerrar el programa?")---> aquí se cambia el valor por "yes"
    valor=messagebox.askokcancel("Salir", "Deseas cerrar el programa?")
    if valor==True:
        root.destroy()
#Esta ultima función permite salir del programa

def re_hacer():
    valor1=messagebox.askretrycancel("Reintentar","No es posible rehacer. Error")
    if valor1==False:
        root.destroy()
#-----------------------------------------------------------------------------------------------------

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

#-----------------------------------------------------------------------------------------------------

archivo_menu=Menu(barramenu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como...")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir",command=salida)

#-----------------------------------------------------------------------------------------------------

editar_menu=Menu(barramenu,tearoff=0)
editar_menu.add_command(label="Deshacer")
editar_menu.add_command(label="Rehacer", command=re_hacer)
editar_menu.add_command(label="Cortar")
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Pegar")
editar_menu.add_command(label="Borrar")
#-----------------------------------------------------------------------------------------------------

herramientas_menu=Menu(barramenu, tearoff=0)

#-----------------------------------------------------------------------------------------------------

ayuda_menu=Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label="Acerca de...", command=infoadicional)
ayuda_menu.add_command(label="Licencia",command=licencia)

#-----------------------------------------------------------------------------------------------------

barramenu.add_cascade(label="Archivo", menu=archivo_menu)
barramenu.add_cascade(label="Editar", menu=editar_menu)
barramenu.add_cascade(label="Herramientas", menu=herramientas_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)


#-----------------------------------------------------------------------------------------------------
root.mainloop()