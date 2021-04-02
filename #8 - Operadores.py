print("************************")
print("*** CLASE OPERADORES ***")
print("************************\n")

print("PROGRAMA DE BECAS")

print("")

distancia=int(input("A que distancia vive de la escuela en km? "))
print(distancia)
num_herm=int(input("Cuántos hermanos tiene? "))
print(num_herm)
sala_fam=int(input("Cúal es el salario anual familiar? "))
print(sala_fam)

print("")

if distancia>20 and num_herm>2 and sala_fam<=350000:
    print("Con derecho a beca completa")
else:
    print("Sin derecho a beca completa")

print("\nREEVALUACION DE BECAS\n")

distancia1=int(input("A que distancia vive de la escuela en km? "))
print(distancia1)
num_herm1=int(input("Cuántos hermanos tiene? "))
print(num_herm1)
sala_fam1=int(input("Cúal es el salario anual familiar? "))
print(sala_fam1)

print("")

if distancia1>20 or num_herm1>2 or sala_fam1<=350000:
    print("Con derecho a beca parcial")
else:
    print("Sin derecho a beca parcial")

print("\nOPERADOR IN\n")

print("ASIGNATURAS ELECTIVAS\n")

print("""
ASIGNATURAS DISPONIBLES:

-Negocios Bursátiles
-Turismo
-Industria Pesada
""")

materia=input("Qué asignatura eliges?: ")

opc=materia.lower() #Para poner el input en minusculas  evitar problemas

if opc in ("negocios bursatiles","negocios bursátiles","turismo","industria pesada"):
    print("Asignatura elegida: "+opc)
else:
    print("Opción erronea.")

print("")
print("PROGRAMA FINALIZADO.")


