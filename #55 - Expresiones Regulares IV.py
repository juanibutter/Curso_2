#Expresiones regulares - match y search
import re

nombre1="Liz Hurley"
nombre2="Jo Wilson"
nombre3="Dorrest Wilson"
nombre4="Forrest Gump"
nombre5="james Gunn"
cadena1="a453445"
cadena2="0984352"
cadena3="7654335"

#La función match busca coincidencias en un patrón de busquedas al comienzo de una cadena de texto
if re.match("James", nombre5, re.IGNORECASE):
    #Con "re.IGNORECASE" hacemos que ignore si una palabra esta en mayúscula o minúscula
    print("Nombre encontrado.")
else:
    print("Nombre no hallado.")

#Es posible incluso buscar por ejemplo una cadena de texto que comience por una letra sin determinar, x ej:
"""if re.match(".orrest", nombre3, re.IGNORECASE):
        print("Nombre encontrado")
    else:
        print("Nombre no encontrado")"""
    #Veremos que podrá encontrar tanto "Forrest" como "Dorrest"

if re.match("\d", cadena1):#La "\d"(digit) sirve para buscar numeros
    print("Hemos encontrado el número.")
else:
    print("Número no hallado.")

#La función search sirve para buscar en cualquier punto de una cadena lo que queremos sea numeros o palabras
if re.search("Wilson", nombre3, re.IGNORECASE):
    print("Apellido encontrado")
else:
    print("No encontrado")