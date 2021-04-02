print("""
***********************
*** EXCEPCIONES III ***
***********************\n""")

print("Generación de excepciones propias(Sintaxis):\n")

def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas") #Sirve para hacer saltar un error, nos sirve para poner un mensaje también
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<60:
        return "Eres adulto"
    elif edad<100:
        return "Eres anciano"
print(evaluaEdad(70))

import math
print("Cálculo de raiz cuadrada:\n")

def calculoraiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
op1=int(input("Introduce un número: "))

try:
    print(calculoraiz(op1))
except ValueError as ErrorNumeroNegativo: #Con 'as' evitamos que aparezca el cartel rojo ya que logramos darle un contexto y un nombre al error que habiamos definido con el raise
    print(ErrorNumeroNegativo)

print("Programa finalizado.")
