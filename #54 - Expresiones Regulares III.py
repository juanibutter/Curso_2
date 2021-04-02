#Expresiones regulares - rangos

import re

lista_nombres=[
    "Ana",
    "Rosa",
    "Pedro",
    "Celia",
    "Cecilia",
    "Cara",
]
#Es importante señalar que se distingue entre mayúsculas y minúsculas
for elemento in lista_nombres:
    if re.findall("[o-t]", elemento):#Esto es para tomar un rango de letras en este caso [o, p, q, r, s, t]
        print(elemento)
#Se puede combinar con lo visto en el archivo anterior (ver "#53 - Expresiones Regulares II.py")

print("")

lista_codigos=[
    "Ma1",
    "Se.1",
    "Ma2",
    "Ba1",
    "Ma3",
    "Va1",
    "Va2",
    "Ma4",
    "Va3",
    "Va4",
    "Se:2",
    "Se3",
    "Se.A",
    "Se:B",
    "SeC",
]

for code in lista_codigos:
    if re.findall("Ma[0-3]", code):
        print(code)
    if re.findall("Va[^0-3]", code):
        #Esto sería la negación de lo que ponemos en el rango. Debería devolver solo uno ("Va4")
        print(code)
    if re.findall("Se[0-2A-B]", code):
        #Asi podemos combinar
        print(code)

    if re.findall("Se[.:]", code):#O buscar algo en especial
        print(code)