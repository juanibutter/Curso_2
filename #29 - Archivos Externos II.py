from io import open

archivo_texto=open("#29_archivo2.txt","r")
archivo_texto.seek(6)

print(archivo_texto.read())
#Vamos a ver como desplazar el puntero y escribir en donde nosotros queramos con el método "seek(posición_deseada)"

archivo_texto.seek(len(archivo_texto.read())/2) #Esto sirve para posicionar el cursor en la mitad del texto....
                                                #...sin importar cuando grande o largo sea
print(archivo_texto.read())

archivo_texto.seek(len(archivo_texto.readline())) #También se puede leer linea a linea

print(archivo_texto.read())

archivo_texto.seek(0)

print(archivo_texto.read(5)) #Al utilizar el read para leer, lo que hacemos es que se lea hasta la posición especificada

print(archivo_texto.read()) #Después de utilizar la función read y poner de vuelta el print, continua la lectura desde...
                            #...donde dejo de leer el print anterior

