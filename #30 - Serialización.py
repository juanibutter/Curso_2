#SERIALIZACIÓN
import pickle       #Importante importar la biblioteca "pickle" para poder serializar

lista_nombres=["Lionel", "Sergio", "Gonzalo", "Ángel"]

fichero_binario=open("#30_lista_nombres", "wb") #Con esta función creamos un fichero de escritura binaria(notese el "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)    #Esto es solo para borrar de la memoria el fichero