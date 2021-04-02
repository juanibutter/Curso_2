import sqlite3

miconexion=sqlite3.connect("Jugadores")

micursor=miconexion.cursor()
#Clausula "UNIQUE" para que no se pueda repetir info, en este caso el nombre del jugador


"""Con esto leemos información:
    micursor.execute("SELECT * FROM Jugadores WHERE Nacionalidad='ARGENTINA'")

    players=micursor.fetchall()
    print(players)"""


#Con esto actualizamos información:
    # micursor.execute("UPDATE Jugadores SET Nacionalidad='BÉLGICA' WHERE Jugador='Kevin De Bruyne'")


#Con esto borramos algún registro
micursor.execute("DELETE FROM Jugadores WHERE Jugador='Kevin De Bruyne'")

miconexion.commit()

miconexion.close()