from tkinter import *

raiz=Tk()

raiz.title("Interfaces Gráficas II")

raiz.resizable(True,True)

#raiz.geometry("500x500")---->La raíz siempre se va a adaptar al tamaño del frame

raiz.config(bg="black")

miFrame=Frame() #Asi creamos el frame, que debe ir dentro de la raíz, empaquetándolo más abajo

miFrame.pack()  #Con esto empaquetamos el frame, para que quede dentro de la raíz...
#..(lo de adentro de los paréntesis es para anclar el frame). "anchor" utiliza puntos cardinales para posicionarse...
#"side" para anclarlo a algún costado(top,bottom,left,right). "fill" para rellenar("y","x","both","none")[Atento:
# para usar "y" y "both" es necesario lo siguiente: (fill="y", expand=True) sino no toma la expansión con "y" o "both"

miFrame.config(bg="grey")

miFrame.config(width="600",height="500") #Para darle tamaño al frame

miFrame.config(bd="40") #Para darle grosor al borde

miFrame.config(relief="groove")   #Para ponerle bordes al frame(si el expand está activado no lo vamos a notar) y tmb..
#..hay que darle un grosor al borde (linea de arriba)
miFrame.config(cursor="pirate")

#TODAS LAS CONFIGURACIONES QUE LE APLICAMOS AL FRAME SE LAS PODEMOS APLICAR TAMBIEN A LA RAIZ, AUNQUE LA DE
#"raiz.geometry("33x344")" NO TIENE SENTIDO YA QUE LA RAIZ SE ADAPTA AL FRAME


raiz.mainloop()