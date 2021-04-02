print("*****************")
print("*** BUCLE FOR ***")
print("*****************\n")

print("COMPROBADOR DE MAIL:\n")

contador=0

mail=input("Introduce tu mail: ")

for t in mail:
    if(t=="@" or t=="."):
        contador+=1
        
if contador==2:
    print("E-mail válido")
else:
    print("E-mail incorrecto")

print("\n")

for i in range(5):
    print("Kiwi")

print("")

for u in range(5):
    print(u)
