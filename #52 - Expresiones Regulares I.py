#Expresiones regulares
import re

cadena="Vamos a aprender expresiones regulares"

#Primero ponemos el texto que queremos buscar y luego en donde se va a buscar:
print(re.search("expresiones", cadena))#Esto nos devuelve un objeto si está el texto sino devuelve "None"

#Otra manera de buscar
textobuscado="aprender"

if re.search(textobuscado, cadena)is not None:
    print("Texto encontrado")
else:
    print("No encontrado")

#Otras expresiones

cadena2="I'm not another Python regular expression. Python is awesome and i know it"

textobuscado2="another"

textoencontrado=re.search(textobuscado2, cadena2)

print(textoencontrado.start())#Nos devuelve donde comienza el texto que buscamos
print(textoencontrado.end())#Nos devuelve donde termina el texto que buscamos
print(textoencontrado.span())#Nos devuelve donde comienza y donde termina el texto que buscamos

textobuscado3="Python"
print(len(re.findall(textobuscado3, cadena2)))#PAra saber cuantas veces está una misma palabra en un texto

