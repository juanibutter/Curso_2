from tkinter import *   #Importamos la librería para interfaces gráficas

raiz=Tk()   #Tenemos que construir la raiz(no necesariamente se llama raiz, pero mejor no conplicarla)

raiz.title("Ventana de pruebas del kiwi")    #Para ponerle título a la ventana

raiz.resizable(1,1) #Para darle dimensión a la ventana(los parametros son booleanos, es decir True o False o 1 y 0)
#El primer parametro es width(ancho), el segundo height(alto).Si ponemos (0,0) NO nos deja redimensionar con el mouse

#Para cambiar el icono necesitamos un archivo ".ico"(Que sea chiquito). Para transformar un archivo a ico usamos...
#"raiz.iconbitmap("plants.ico")" --->comando para poner el icono
#...google(buscar conversor .ico). El archivo debe estar en la misma carpeta donde tenemos el proyecto.

raiz.geometry("650x500") #Esto es para el tamaño de la ventana

raiz.config(bg="black") #Para cambiar el fondo de la ventana

raiz.mainloop() #Para poder abrir la ventana es necesario que este en un bucle infinito por eso usamos esta instrucción
#El método mainloop siempre debe estar en último lugar

#IMPORTANTE SI CAMBIAMOS LA EXTENSIÓN ".py" POR ".pyw"...
#...HAREMOS QUE LA CONSOLA NO SE ABRA,SINO QUE SE ABRA SOLO LA APLICACIÓN