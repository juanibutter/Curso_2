from tkinter import *

root=Tk()

root.title("Opciones de Turismo")

playa=IntVar()
montania=IntVar()
ciudad=IntVar()
rural=IntVar()
viniedos=IntVar()

def op_viajes():
    op_elegida=""
    if playa.get()==1:
        op_elegida+=" Playa "
    
    if montania.get()==1:
        op_elegida+=" Montaña "
    
    if ciudad.get()==1:
        op_elegida+=" Ciudad "
    
    if rural.get()==1:
        op_elegida+=" Rural "
    
    if viniedos.get()==1:
        op_elegida+=" Viñedos "

    eleccion.config(text=op_elegida)
#Con esta función logramos mostrar que opciones elegimos


foto=PhotoImage(file="D:/Usuario/Documents/(((Programación)))/Python/Curso #2/Interfaz Gráfica/Turismo.png")
#Para poder agregar una ruta hay que cambiar las "\"" por "/""
Label(root,image=foto).pack()


frame=Frame(root)
frame.pack()
Label(frame,text="Elige destino:", width=50).pack()


Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=op_viajes).pack()
Checkbutton(frame, text="Montaña", variable=montania, onvalue=1, offvalue=0, command=op_viajes).pack()
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=op_viajes).pack()
Checkbutton(frame, text="Rural", variable=rural, onvalue=1, offvalue=0, command=op_viajes).pack()
Checkbutton(frame, text="Viñedos", variable=viniedos, onvalue=1, offvalue=0, command=op_viajes).pack()
#"onvalue" y "offvalue" es para saber cunado selleccionamos o deseleccionamos

eleccion=Label(frame)
eleccion.pack()








root.mainloop()