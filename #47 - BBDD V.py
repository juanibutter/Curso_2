import sqlite3

miconexion=sqlite3.connect("Clubes de Futbol 2")

micursor=miconexion.cursor()

#VAMOS A HACER QUE LE ASIGNE UNA CLAVE LA MISMA BASE DE DATOS DE MANERA AUTOMATICA EN VEZ DE NOSOTROS
micursor.execute("""
    CREATE TABLE Equipos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Club VARCHAR(50),
    Ranking INTEGER,
    País VARCHAR(30))
""")#LO HACEMOS CON---->"ID INTEGER PRIMARY KEY AUTOINCREMENT"

equipos=[
    ("FC BARCELONA", 6, "ESPAÑA"),
    ("REAL MADRID CF", 5, "ESPAÑA"),
    ("BAYERN MUNCHEN", 1, "ALEMANIA"),
    ("BORUSSIA DORTMUND", 8, "ALEMANIA"),
    ("PSG", 4, "FRANCIA"),
    ("MANCHESTER CITY", 2, "INGLATERRA"),
    ("MANCHESTER UNITED", 7, "INGLATERRA"),
    ("LIVERPOOL", 3, "INGLATERRA"),
    ("ARSENAL", 9, "INGLATERRA"),
    ("CHELSEA", 10, "INGLATERRA")
]

micursor.executemany("INSERT INTO Equipos VALUES (NULL,?,?,?)", equipos)
#DEBEMOS PONER NULL DONDE VA EL ID QUE QUEREMOS QUE LE ASIGNE LA MISMA BASE DE DATOS



#micursor.execute("INSERT INTO Equipos VALUES ('SP03', 'ATLÉTICO DE MADRID', 11, 'ESPAÑA')")


miconexion.commit()

miconexion.close()