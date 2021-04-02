print("***********************************")
print("***** BUCLE FOR (DETERMINADO) *****")
print("***********************************\n")

for i in [1,2,3]: #Luego de in ponemos la cantidad de veces que queres repetir el bucle, en este caso 3 veces porque es una lista de 3 elementos
    print("Kiwi")

print("")

for j in ["Madrid","Roma","Londres"]:
    print(j)

print("")

for w in ["Messi",10,"FC Barcelona"]:
    print("G.O.A.T.",end=" ") #Para imprimir en la misma linea se utiliza 'end'. Si se deja entre comillas un espacio no quedan pegados

print("\n")

for s in "FC Barcelona": #Imprime x veces según la cantidad de caracteres en el string
    print("Diciembre")

print("")

email=False #Para comprobar un estado

mail=input("Introduce tu mail: ")

for t in mail:
    if(t=="@"):
        email=True
if email==True: #Tambien es posible escribir: "if email:" sin escribir el True ya que queda de manera implicita de esa manera
    print("E-mail válido")
else:
    print("E-mail incorrecto")
