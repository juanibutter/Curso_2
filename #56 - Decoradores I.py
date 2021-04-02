#Decoradores I

def fun_decoradora(funcion_parametro):
    def fun_interna():
        print("Vamos a ralizar un cálculo:")
        funcion_parametro()
        print("Hemos terminado el cálculo")
    return fun_interna

@fun_decoradora #Con esto ("@ejemplofuncion") llamamos a nuestra función decoradora, en este caso se le añade..
def suma():#..aquí a la suma
    print(15+20)

@fun_decoradora
def resta():#...y luego a la resta
    print(30-10)

suma()
print("")
resta()







