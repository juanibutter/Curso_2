from tkinter import *
import sqlite3

#----------------------------Raiz y Menú--------------------------------------------------
raiz=Tk()
raiz.title("App de creación de base de datos")
barramenu=Menu(raiz)
raiz.config(bg="black", menu=barramenu, width=300, height=300)
#----------------------------Pestañas Menú------------------------------------------------
#----
bbdd_menu=Menu(barramenu, tearoff=0)
bbdd_menu.add_command(label="Crear")
bbdd_menu.add_command(label="Salir")
#----
borrar_menu=Menu(barramenu,tearoff=0)
borrar_menu.add_command(label="Borrar campos")
#----
crud_menu=Menu(barramenu,tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")
#----
ayuda_menu=Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label="Acerca de...")
ayuda_menu.add_command(label="Licencia")
#----------------------------Cascadas Menú------------------------------------------------
barramenu.add_cascade(label="BBDD", menu=bbdd_menu)
barramenu.add_cascade(label="Borrar", menu=borrar_menu)
barramenu.add_cascade(label="CRUD", menu=crud_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)

#----------------------------Frame--------------------------------------------------------
miframe=Frame(raiz)
miframe.pack(fill="both", expand=True)
miframe.config(bg="grey", width=500, height=500, relief="groove", bd=10)

#-----------------------------Cuadros------------------------------------------------------
cuadroid=Entry(miframe)
cuadroid.grid(row=0, column=1)
cuadroid.config(fg="black", justify="center", state="readonly", font=("Comic Sans MS", 8))

cuadronombre=Entry(miframe)
cuadronombre.grid(row=1, column=1)
cuadronombre.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2, column=1)
cuadroapellido.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadropass=Entry(miframe)
cuadropass.grid(row=3, column=1)
cuadropass.config(fg="black", justify="center",show="*", font=("Comic Sans MS", 8))

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=4, column=1)
cuadrodireccion.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadrocomentarios=Text(miframe, width=18, height=6, font=("Comic Sans MS", 10))
cuadrocomentarios.grid(row=5, column=1, pady=14, padx=14)
scrollvertical=Scrollbar(miframe, command=cuadrocomentarios.yview)
scrollvertical.grid(row=5, column=2, sticky="nsew")
cuadrocomentarios.config(yscrollcommand=scrollvertical.set)


#----------------------------Labels---------------------------------------------------------
idlabel=Label(miframe, text="Id:")
idlabel.grid(row=0, column=0, sticky="e",pady=14,padx=14)

nombrelabel=Label(miframe, text="Nombre:")
nombrelabel.grid(row=1, column=0, sticky="e",pady=14,padx=14)

apellidolabel=Label(miframe, text="Apellido:")
apellidolabel.grid(row=2, column=0, sticky="e",pady=14,padx=14)

passlabel=Label(miframe, text="Password:")
passlabel.grid(row=3, column=0, sticky="e",pady=14,padx=14)

direccionlabel=Label(miframe, text="Dirección:")
direccionlabel.grid(row=4, column=0, sticky="e",pady=14,padx=14)

comentarioslabel=Label(miframe, text="Comentarios:")
comentarioslabel.grid(row=5, column=0, sticky="e",pady=14,padx=14)



#------------------------------Mainloop------------------------------------------------------
raiz.mainloop()