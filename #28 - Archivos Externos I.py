#Crear, abrir, escribir y cerrar archivo:

from io import open

archivo_texto=open("#28_archivo.txt","w") #La '"w"' representa "write", para poder modificar el archivo

frase="Maravilloso día para seguir aprendiendo Python\nEl miércoles"

archivo_texto.write(frase)
archivo_texto.close()

#Abrir, leer y cerrar archivo

archivo_texto=open("#28_archivo.txt","r") #La '"r"' representa "read", para leer el archivo

texto=archivo_texto.read()

archivo_texto.close()

print(texto)
#También podemos usar el método "readlines()"
archivo_texto=open("#28_archivo.txt","r")
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)
#Para ver solo una linea (entre corchetes la linea que quiero acceder, no necesariamente siempre "0")
print(lineas_texto[0])

#Abrir archivo para agregar información

archivo_texto=open("#28_archivo.txt","a") #La "'a'" es de "append", para agregar información al archivo

archivo_texto.write("\nA las 17 vemos el partido de champions y volvemos a estudiar")

archivo_texto.close()