import pickle

fichero=open("#30_lista_nombres","rb") #Ahora debemos leer el archivo binario creado anteriormente

lista=pickle.load(fichero) #Importante para poder cargar la información del fichero

print(lista)