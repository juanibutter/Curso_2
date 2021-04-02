print("********************")
print("*** OCTAVA PARTE ***")
print("********************\n")

print("")

edad=int(input("Edad? "))

if 0<=edad<=100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

print("")

print("EVALUADOR DE SALARIOS DEL PERSONAL:\n")

sueldo_pres=int(input("Introduce el sueldo del Presidente: "))
print("Sueldo del presidente: $"+str(sueldo_pres))
sueldo_dir=int(input("Introduce el sueldo del Director: "))
print("Sueldo del Director: $"+str(sueldo_dir))
sueldo_jef=int(input("Introduce el sueldo del Jefe de Personal: "))
print("Sueldo del Jefe de Personal: $"+str(sueldo_jef))
sueldo_adm=int(input("Introduce el sueldo del Administrativo: "))
print("Sueldo del Administrativo: $"+str(sueldo_adm))

print("")

if sueldo_adm<sueldo_jef<sueldo_dir<sueldo_pres:
    print("La compañia funciona de maravilla!!")
else:
    print("Hay algo que no está del todo bien. Se precisa una correción salarial.")
print("")
print("FIN DEL PROGRAMA")
