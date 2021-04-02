from tkinter import *
from tkinter import messagebox
import sqlite3

#----------------------------Raiz y Menú--------------------------------------------------
raiz=Tk()
raiz.title("App de creación de base de datos")
barramenu=Menu(raiz)
raiz.config(bg="#D4CECD", menu=barramenu, width=300, height=300)

#----------------------------Funciones Menú-----------------------------------------------
#-------------#
def salida():
    valor=messagebox.askquestion("Salir", "Deseas cerrar el programa?")
    if valor=="yes":
        raiz.destroy()

def crearbase():
    bbdd=messagebox.askokcancel("Crear BBDD", "Deseas crear una Base de Datos?")
    if bbdd==True:
        try:
            miconexion=sqlite3.connect("BBDD Usuarios de esta App")

            micursor=miconexion.cursor()

            micursor.execute("""
                CREATE TABLE Usuarios(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre VARCHAR(50),
                Apellido VARCHAR(50),
                Password VARCHAR(50),
                Dirección VARCHAR(50),
                Comentarios VARCHAR(90))
            """)
        except:
            messagebox.showwarning("Atención!","La Base de Datos ya existe.")

#-------------#
def borrarcampos():
    a_id.set("")
    a_nombre.set("")
    a_apellido.set("")
    a_password.set("")
    a_direccion.set("")
    cuadrocomentarios.delete(1.0, END)
#-------------#
def crearusuario():
    miconexion=sqlite3.connect("BBDD Usuarios de esta App")
    micursor=miconexion.cursor()
    datos=a_nombre.get(), a_apellido.get(), a_password.get(), a_direccion.get(), cuadrocomentarios.get("1.0", END)
    micursor.execute("INSERT INTO Usuarios VALUES(NULL,?,?,?,?,?)", (datos))
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro creado con éxito.")
#-------------
def leerusuario():
    miconexion=sqlite3.connect("BBDD Usuarios de esta App")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM Usuarios WHERE ID=" + a_id.get())
    leeruser=micursor.fetchall()
    for user in leeruser:
        a_id.set(user[0])
        a_nombre.set(user[1])
        a_apellido.set(user[2])
        a_password.set(user[3])
        a_direccion.set(user[4])
        cuadrocomentarios.insert(1.0, user[5])
    miconexion.commit

#-------------
def actualizarusuario():
    miconexion=sqlite3.connect("BBDD Usuarios de esta App")
    micursor=miconexion.cursor()
    datos=a_nombre.get(), a_apellido.get(), a_password.get(), a_direccion.get(), cuadrocomentarios.get("1.0", END)
    micursor.execute("UPDATE Usuarios SET Nombre=?, Apellido=?, Password=?, Dirección=?, Comentarios=?" +
    "WHERE ID=" + a_id.get(), (datos))
    miconexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito.")
#-------------
def borrarusuario():
    miconexion=sqlite3.connect("BBDD Usuarios de esta App")
    micursor=miconexion.cursor()
    micursor.execute("DELETE FROM Usuarios WHERE ID=" + a_id.get())
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito.")
#-------------#
def acercade():
    messagebox.showinfo("Información del programa", "Práctica autónoma de Python 2021 - App de BBDD")

def licencia():
    messagebox.showinfo("LICENCIA", "KIWI Inc. Todos los derechos reservados.")
#----------------------------Pestañas Menú------------------------------------------------
#----
bbdd_menu=Menu(barramenu, tearoff=0)
bbdd_menu.add_command(label="Crear", command=crearbase)
bbdd_menu.add_command(label="Salir", command=salida)
#----
borrar_menu=Menu(barramenu,tearoff=0)
borrar_menu.add_command(label="Borrar campos", command=borrarcampos)
#----
crud_menu=Menu(barramenu,tearoff=0)
crud_menu.add_command(label="Crear", command=crearusuario)
crud_menu.add_command(label="Leer", command=leerusuario)
crud_menu.add_command(label="Actualizar", command=actualizarusuario)
crud_menu.add_command(label="Borrar", command=borrarusuario)
#----
ayuda_menu=Menu(barramenu, tearoff=0)
ayuda_menu.add_command(label="Acerca de...", command=acercade)
ayuda_menu.add_command(label="Licencia", command=licencia)
#----------------------------Cascadas Menú------------------------------------------------
barramenu.add_cascade(label="BBDD", menu=bbdd_menu)
barramenu.add_cascade(label="Borrar", menu=borrar_menu)
barramenu.add_cascade(label="CRUD", menu=crud_menu)
barramenu.add_cascade(label="Ayuda", menu=ayuda_menu)

#----------------------------Frame 1--------------------------------------------------------
miframe=Frame(raiz)
miframe.pack(fill="both", expand=True)
miframe.config(bg="#D4CECD", width=500, height=500)

#-----------------------------Cuadros------------------------------------------------------
a_id=StringVar()
a_nombre=StringVar()
a_apellido=StringVar()
a_password=StringVar()
a_direccion=StringVar()

cuadroid=Entry(miframe, textvariable=a_id)
cuadroid.grid(row=0, column=1, padx=10, pady=10)
cuadroid.config(fg="#BB1919", justify="center", font=("Comic Sans MS", 8))

cuadronombre=Entry(miframe, textvariable=a_nombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)
cuadronombre.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadroapellido=Entry(miframe, textvariable=a_apellido)
cuadroapellido.grid(row=2, column=1, padx=10, pady=10)
cuadroapellido.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadropass=Entry(miframe, textvariable=a_password)
cuadropass.grid(row=3, column=1, padx=10, pady=10)
cuadropass.config(fg="black", justify="center",show="*", font=("Comic Sans MS", 8))

cuadrodireccion=Entry(miframe, textvariable=a_direccion)
cuadrodireccion.grid(row=4, column=1, padx=10, pady=10)
cuadrodireccion.config(fg="black", justify="center", font=("Comic Sans MS", 8))

cuadrocomentarios=Text(miframe, width=18, height=6, font=("Comic Sans MS", 10))
cuadrocomentarios.grid(row=5, column=1, padx=10, pady=10)
scrollvertical=Scrollbar(miframe, command=cuadrocomentarios.yview)
scrollvertical.grid(row=5, column=2, sticky="nsew")
cuadrocomentarios.config(yscrollcommand=scrollvertical.set)


#----------------------------Labels---------------------------------------------------------
idlabel=Label(miframe, text="Id:", bg="#D4CECD")
idlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombrelabel=Label(miframe, text="Nombre:", bg="#D4CECD")
nombrelabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miframe, text="Apellido:", bg="#D4CECD")
apellidolabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miframe, text="Password:", bg="#D4CECD")
passlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miframe, text="Dirección:", bg="#D4CECD")
direccionlabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioslabel=Label(miframe, text="Comentarios:", bg="#D4CECD")
comentarioslabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------------------------Botones Frame 2-----------------------------------------------
miframe2=Frame(raiz)
miframe2.config(bg="#D4CECD")
miframe2.pack()

botoncrear=Button(miframe2, text="Create",  command=crearusuario)
botoncrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)
botonleer=Button(miframe2, text="Read", command=leerusuario)
botonleer.grid(row=1,column=1,sticky="e",padx=10,pady=10)
botonactualizar=Button(miframe2, text="Update", command=actualizarusuario)
botonactualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)
botonborrar=Button(miframe2, text="Delete", command=borrarusuario)
botonborrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

#------------------------------Mainloop------------------------------------------------------
raiz.mainloop()