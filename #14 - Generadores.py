print("""
*********************
*** GENERADORES I ***
*********************\n""")

print("Lista de números pares:\n")


#Método tradicional
def generaPares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num+=1
    return lista

print(generaPares(10))
print("")


#Con Generadores
def genera_pares(limite):
    num=1
    while num<limite:
        yield num*2     #Quitamos la lista, el return, el append y ponemos el yield y creamos el objeto iterable "devuelve_pares"
        num+=1
devuelve_pares=genera_pares(10)

for a in devuelve_pares:
    print(a)

#AHORA LA POSTA DEL GENERADOR:

print("\nValor a valor:\n")

def genera_Pares1(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
devuelve_Pares1=genera_Pares1(10)

print(next(devuelve_Pares1)) #Con esto conseguimos que nos devuelva el primer valor

#(Acá abajo solo sirve de ejemplo)

print("Código por aquí código por allá")

print(next(devuelve_Pares1)) #Entre llamada y llamada se entra en estado de suspensión y se ahorran recursos

print("Código por aquí código por allá parte2")

print(next(devuelve_Pares1))









