from tkinter import *

root=Tk()

barramenu=Menu(root)#Creamos la barra de menú
root.config(menu=barramenu, width=300, height=300)

#Creamos las pestañas del menú
archivo_menu=Menu(barramenu, tearoff=0)
#"tearoff" es para eliminar la barra que aparece por defecto en el submenu
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como...")

archivo_menu.add_separator()
#Para agregar una barra separadora. Sirve para agrupar instrucciones o diferenciarlas
archivo_menu.add_command(label="Salir")

#------------------------------------------------------

editar_menu=Menu(barramenu,tearoff=0)
editar_menu.add_command(label="Deshacer")
editar_menu.add_command(label="Rehacer")
editar_menu.add_command(label="Cortar")
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Pegar")
editar_menu.add_command(label="Borrar")
#------------------------------------------------------

herramientas_menu=Menu(barramenu, tearoff=0)

#------------------------------------------------------

ayuda_menu=Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label="Acerca de...")
ayuda_menu.add_command(label="Licencia")

#------------------------------------------------------
#Esto es para ponerle los nombres a las pestañas del menú
barramenu.add_cascade(label="Archivo", menu=archivo_menu)
barramenu.add_cascade(label="Editar", menu=editar_menu)
barramenu.add_cascade(label="Herramientas", menu=herramientas_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)






root.mainloop()