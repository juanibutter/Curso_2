print("*********************")
print("*** BUCLE FOR III ***")
print("*********************\n")

#Para concatenar texto con variable:
for a in range(5): #Aquí la variable va del 0 al 5
    print(f"Valor de la variable: {a}") #Al escribir la f, le estamos diciendo a python que queremos que la variable vaya tomando los distintos valores del bucle.
                                        #Si quitamos la f, quedaria de manera literal y la variable quedaría como esta definida.


for b in range(5,10): #Aquí la variable va del 5 al 9
    print(f"Valor de la variable: {b}")


for c in range(10,21,2): #Aquí la variable va del 10 al 20, pero además en el tercer componente podemos poner de cuanto en cuanto se realiza el conteo(en este caso de a 2).
    print(f"Valor de la variable: {c}")

print("\nValidar e-mail:\n")

valido=False

email=input("Introduce tu e-mail: ")

for d in range(len(email)):
    if email[d]=="@":
        valido=True

if valido:
    print("E-mail Válido")
else:
    print("Incorrecto")
