#Práctica calculadora
from tkinter import *

raiz=Tk()
raiz.config(bg="#727578")
miframe=Frame(raiz)
miframe.config(bg="#727578")
miframe.pack()

operacion="" #Esto nos va a permitir resetear la pantalla, guardar el valor que introdujimos y que...
#...se pueda realizar la operación deseada
resultado=0 #Con esta variable declaramos resultados y almacenamos las operaciones a realizar

#**************************************************Pantalla*****************************************************

numeropantalla=StringVar() #Para poder hacer que funcionen los...
#...botones debemos crear variables y llamar a funciones


pantalla=Entry(miframe,textvariable=numeropantalla)#Creamos la pantalla de la calculadora
#"textvariable" es para que se vea en la pantalla lo que pulsamos
pantalla.grid(row=1,column=1,padx=10,pady=10,rowspan=2,columnspan=4)#le indicamos donde está ubicada
#Con "columnspan" logramos que un widget ocupe un determinado número de columnas, en este caso 4
pantalla.config(bg="#b6c0ce",fg="black",justify="right")#La configuramos a nustro parecer

#********************************************Pulsaciones botones************************************************
def numeropulsado(num): #Con esto hacemos que cuando pulsemos un numero aparezca en pantalla
    global operacion
    if operacion!="":
        numeropantalla.set(num) #Si el usuario pulsa el boton suma, lo unico que le decimos al programa con...
        #..esto es que no concatene sino que resetee la pantalla para realizar la operación
        operacion="" #Esto es para que al teclear el segundo número comience a concatenar y no sobreescriba los nums
    else:
        numeropantalla.set(numeropantalla.get() + num)


#***********************************************Función Suma****************************************************
def suma(num):
    global operacion #Al decirle que es "global" la funcion es accesible desde cualquier lugar del programa...
    #...desde todas las funciones y desde todos los metodos
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeropantalla.set(resultado)

#***********************************************Función Resta****************************************************
#def resta(num):
    global operacion
    global resultado
    resultado-=int(num)
    operacion="resta"
    numeropantalla.set(resultado)

#***********************************************Función resultadototal****************************************************
def resultadototal():
    global resultado
    numeropantalla.set(resultado+int(numeropantalla.get()))
    resultado=0

#********************************************Primera fila de botones********************************************
boton7=Button(miframe,text="7",width=4,command=lambda:numeropulsado("7"))#creamos los botones y los configuramos
boton7.grid(row=3,column=1)#Los ubicamos
boton8=Button(miframe,text="8",width=4,command=lambda:numeropulsado("8"))
boton8.grid(row=3,column=2)
boton9=Button(miframe,text="9",width=4,command=lambda:numeropulsado("9"))
boton9.grid(row=3,column=3)
botondiv=Button(miframe,text="/",width=4)
botondiv.grid(row=3,column=4)

#********************************************Segunda fila de botones********************************************
boton4=Button(miframe,text="4",width=4,command=lambda:numeropulsado("4"))#Con el "command" cuando apretemos el boton...
#...lograremos que aprezca en pantalla. Con lambda(funcion anónima)no aparece nada en la pantalla a menos que...
#...nosotros pulsemos el botón
boton4.grid(row=4,column=1)
boton5=Button(miframe,text="5",width=4,command=lambda:numeropulsado("5"))
boton5.grid(row=4,column=2)
boton6=Button(miframe,text="6",width=4,command=lambda:numeropulsado("6"))
boton6.grid(row=4,column=3)
botonmult=Button(miframe,text="x",width=4)
botonmult.grid(row=4,column=4)

#********************************************Tercera fila de botones********************************************
boton1=Button(miframe,text="1",width=4,command=lambda:numeropulsado("1"))
boton1.grid(row=5,column=1)
boton2=Button(miframe,text="2",width=4,command=lambda:numeropulsado("2"))
boton2.grid(row=5,column=2)
boton3=Button(miframe,text="3",width=4,command=lambda:numeropulsado("3"))
boton3.grid(row=5,column=3)
botonresta=Button(miframe,text="-",width=4,#command=lambda:resta(numeropantalla.get())
botonresta.grid(row=5,column=4)

#********************************************Cuarta fila de botones*********************************************
boton0=Button(miframe,text="0",width=4,command=lambda:numeropulsado("0"))
boton0.grid(row=6,column=1)
botoncoma=Button(miframe,text=",",width=4,command=lambda:numeropulsado(","))
botoncoma.grid(row=6,column=2)
botonigual=Button(miframe,text="=",width=4,command=lambda:resultadototal())
botonigual.grid(row=6,column=3)
botonsuma=Button(miframe,text="+",width=4,command=lambda:suma(numeropantalla.get()))
botonsuma.grid(row=6,column=4)

#***************************************************Mainloop****************************************************
raiz.mainloop()
