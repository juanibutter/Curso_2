#Expresiones regulares - metacaracteres
import re

lista_nombres=[
    "Lionel Messi",
    "Jerome Boateng",
    "Kevin-Prince Boateng",
    "Zlatan Ibrahimovic",
    "Ignacio Scocco",
    "Ignacio Fernández",
    "Federico Fernández",
    "Sergio Agüero"
]

for elemento in lista_nombres:
    if re.findall("^Ignacio", elemento):
        #Con este método hacemos que busque la palabra que comienza por... y lo indicamos con el "^"
        print(elemento)
    if re.findall("Fernández$", elemento):
        #En este caso queremos los que terminan por... y lo buscamos con el signo "$" al final de la palabra
        print(elemento)
print("")
#Tambien es posible hacerlo con dominios de internet
lista_urls=[
    "https://www.google.com.ar",
    "https://www.google.com",
    "https://www.google.com.es",
    "https://www.google.com.uk",
    "https://www.mdzol.com",
    "https://www.informaticaenespaña.com.es",
    "https://www.reservañandu.com.ar",
    "https://www.elhombrearaña.com.mx",
]

for urls in lista_urls:
    if re.findall("com$", urls):
        print(urls)
    if re.findall("[ñ]", urls):
        #Con esto podemos buscar palabra con un caracter que queramos, importante los "[]"
        print(urls)
print("")
lista_tres=[
    "Hombres",
    "Mujeres",
    "Mascotas",
    "Canción",
    "Cancion",
    "Niños",
    "Niñas"
]
#Tambien es posible buscar de la siguiente manera:
for caracter in lista_tres:
    if re.findall("Niñ[oa]s", caracter):#en la que logramos que nos muestre tanto niños como niñas
        print(caracter)
    if re.findall("Canci[oó]n", caracter):#o si queremos buscar una palabra tanto con tilde como sin tilde
        print(caracter)