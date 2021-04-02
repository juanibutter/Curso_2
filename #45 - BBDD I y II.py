import sqlite3

miconexion=sqlite3.connect("Primera BBDD")  #Con esto creamos/abrimos la conexion...
#..y la base de datos si no exitiera

micursor=miconexion.cursor()  #Creamos el cursor

#[micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")]
#Creamos la tabla llamada "Productos". Dentro de ella ponemos los nombre de las columnas y el tipo...
#..de dato (x ej.: nombre:"Precio", tipo:"varchar" y entre parentesis la longitud (20))
#IMPORTANTE: INVALIDAR LA LINEA DE CODIGO QUE CREA LA TABLA UNA VEZ QUE INTRODUZCAMOS LA INFO, PQ SINO..
#..DARA ERROR YA QUE LA TABLA ESTA CREADA

#Comentamos para no causar error[micursor.execute("INSERT INTO PRODUCTOS VALUES('PELOTA', 15, 'DEPORTES')")]
#Creamos un producto para nuestra tabla

#[varios_productos=[
#    ("Camiseta", 10, "Deportes"),
#    ("Jarrón", 90, "Cerámica"),
#    ("Camión de bomberos", 14, "Jugueteria"),
#    ("Vasos", 2, "Bazar")]]
#Utilizamos una lista con tuplas para introducir varios objetos. Poner coma al final de cada tupla...
#...excepto la ultima
#[micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos)]
#Utilizamos la instrucción "executemany" para poder ingresar variios productos y MUY IMPORTANTE...
#..tenemos que poner entre paréntesis tantos signos de interrogación como columnas tiene la tabla

micursor.execute("SELECT * FROM PRODUCTOS") #Ahora vamos a leer los registros

leerlista=micursor.fetchall()

#print(leerlista)---> Asi nos va a dar directamente una lista con todos los productos

for producto in leerlista:
    print("Nombre artículo:", producto[0], "\nSección:", producto[2])
#Con esto hacemos que nos devuelva una tupla y no una lista



miconexion.commit()
#Con esto confirmamos que queremos hacer cambios o introducir algo en la tabla






miconexion.close()  #Con esto cerramos la conexión