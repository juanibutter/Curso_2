print("""
*************************************
*** BUCLES V (Continue-Pass-Else) ***
*************************************\n
""")
print("Instrucción CONTINUE:\n")

print("Sin instrucción:\n")
for letra in "Python":
    print("Viendo la letra: "+letra)
    
print("\nCon instrucción:\n")

for letra in "Python":
    if letra=="h":
        continue    #Sirve para ignorar una instrucción
    print("Viendo la letra: "+letra)

print("")

nombre="Otorrinolaringólogo o Ladrón"
contador=0
for a in nombre:
    if a==" ":
        continue    #Acá estamos haciendo que se ignoren los espacios en blanco
    contador+=1
print(contador)
print(len(nombre))

print("\nInstrucción PASS:\n")

class miclase:
    pass #para implementar mas tarde

print("\nInstrucción ELSE:\n")

email=input("Introduce tu e-mail por favor: ")

for b in email:
    if b=="@":
        arroba=True
        break;
else:   #En este caso el else se activa cuando termina el bucle
    arroba=False

print(arroba)













