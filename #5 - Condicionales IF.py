print("*******************")
print("*** SEXTA CLASE ***")
print("*******************\n")

print("Condicional IF\n")

print("Programa de evaluación de notas de alumnos:\n")
nota=input("Que nota tiene el alumno? ")
def evaluacion(notalum):
    valor="Aprobado"
    if notalum<6:
        valor="Reprobado"
    return valor
print(evaluacion(int(nota)))
