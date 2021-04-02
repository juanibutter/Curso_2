print("""
**************************
*** MÉTODOS DE CADENAS ***
**************************\n""")
nombreusuario=input("Introduce un nombre de usuario: ")
print("Tu nombre de usuario es",nombreusuario.upper())  #Para pasar a mayúsculas
print("Tu nombre de usuario es",nombreusuario.lower())  #Pasar a minúscula
print("Tu nombre de usuario es",nombreusuario.capitalize()) #Primer letra en mayúscula

edad=input("Cuantos años tienes? ")
print(edad.isdigit())   #Para saber si un input es número o no

edad1=input("Cual es tu edad? ")
while(edad1.isdigit()==False):
    print("Por favor introduce un valor numérico")
    edad1=input("Cual es tu edad? ")
if (int(edad)<18):
    print("Acceso Denegado")
else:
    print("Acceso Autorizado")