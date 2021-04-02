print("*********************")
print("*** SEPTIMA CLASE ***")
print("*********************\n")

print("Condicional IF - ELSE - ELIF")
print("")

print("Verificación de edad para acceso:")
edad=int(input("Cuántos años tenes? "))
print("")

if edad<18:
    print("Acceso Restringido")
elif edad>=120:
    print("No Autorizado")
else:
    print("Acceso Autorizado")

print("")
print("************************")
print("*** SEGUNDO PROGRAMA ***")
print("************************")

print("")

nota=int(input("Cuál es tu nota? "))

if nota>=6 and nota <11:
    print("Felicidades has pasado!")
elif nota>10:
    print("Error.")
elif nota<6 and nota>3:
    print("Insuficiente, va a recuperatorio.")
else:
    print("Reprobado, repite el año.")

print("\nPROGRAMA FINALIZADO.")
