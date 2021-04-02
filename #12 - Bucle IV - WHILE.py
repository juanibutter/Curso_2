print("""
***********************************
*** BUCLE WHILE (Indeterminado) ***
***********************************\n""")


a=1

while a<=10:
    print("Ejecución "+str(a))
    a+=1 #Es muy necesario agregarle algo que impida que sea un bucle infinito, sino el uso de recursos de la pc causaría un desastre
print("Ejecución finalizada.")

edad=int(input("Introduce tu edad por favor: "))
while edad<18 or edad>100:
    print("Has introducido una edad restringida. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar, puedes pasar")
print("Edad del aspirante:",edad)

print("\nCOMO EVITAR QUE UN BUCLE SEA INFINITO:\n")

import math #Sirve para importar una clase con todos sus métodos y/o funciones. Siempre se pone al ppio del código. Es necesario para poder hacer algunas cosas

print("Programa de cálculo de raíz cuadrada")
num=int(input("Introduce un número: "))
intentos=0

while num<0:
    print("Error. No existe la raíz cuadrada de un número negativo.")
    if intentos==4:
        print("Has agotado tus intentos. El programa se cerrara.")
        break; #Esta instrucción termina el bucle
    num=int(input("Introduce un número: "))
    if num<0:
        intentos+=1

if intentos<2:
    solucion=math.sqrt(num) #Introdujimos la clase "math" y "sqrt"(square root/raíz cuadrada)
    print("La raíz cuadrada de ",num,"es",solucion)
