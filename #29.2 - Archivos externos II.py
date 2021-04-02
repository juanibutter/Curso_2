from io import open

archivo_texto=open("#29_archivo2.txt","r+") #Cuando ponemos "r+" indicamos que el archivo es para lectura y escritura

archivo_texto.write(" Hoy es un gran gran gran")

#print(archivo_texto.readlines())

print(archivo_texto.read())

lista_texto=archivo_texto.readlines()

lista_texto[4]=" Linea incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

