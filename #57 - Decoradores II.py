#Decoradores II

def fun_decoradora(funcion_parametro):
    def fun_interna(*args,**kwargs):#La nomenclatura "*args"(puede sero otra cosa), nos indica que esta función..
                           #..puede recibir un número indeterminado de parámetros.
                           #Además es posible agregarle "**kwargs"(argumentos con clave[keywords]), lo que ...
                           #..hace posible pasar argumentos clave valor x ej: en la potencia--->...
                           #..."base=5, exponente=5" (mirar mas abajo)
        print("Vamos a ralizar un cálculo:")
        funcion_parametro(*args, **kwargs)
        print("Hemos terminado el cálculo")
    return fun_interna

@fun_decoradora #Con esto ("@ejemplofuncion") llamamos a nuestra función decoradora, en este caso se le añade..
def suma(num1,num2, num3):#..aquí a la suma
    print(num1+num2+num3)

@fun_decoradora
def resta(num1,num2):#...y luego a la resta
    print(num1-num2)

@fun_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7,8,5)
print("")
resta(30,15)
print("")
potencia(base=5,exponente=5)