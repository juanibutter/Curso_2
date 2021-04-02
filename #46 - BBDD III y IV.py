import sqlite3

miconexion=sqlite3.connect("Clubes de Futbol")

micursor=miconexion.cursor()

# micursor.execute("""
#     CREATE TABLE Equipos (
#     Clave VARCHAR(4) PRIMARY KEY,
#     Club VARCHAR(50),
#     Ranking INTEGER,
#     País VARCHAR(30))
# """)

# equipos=[
#     ("SP01", "FC BARCELONA", 6, "ESPAÑA"),
#     ("SP02", "REAL MADRID CF", 5, "ESPAÑA"),
#     ("GE01", "BAYERN MUNCHEN", 1, "ALEMANIA"),
#     ("GE02", "BORUSSIA DORTMUND", 8, "ALEMANIA"),
#     ("FR01", "PSG", 4, "FRANCIA"),
#     ("EN01", "MANCHESTER CITY", 2, "INGLATERRA"),
#     ("EN02", "MANCHESTER UNITED", 7, "INGLATERRA"),
#     ("EN03", "LIVERPOOL", 3, "INGLATERRA"),
#     ("EN04", "ARSENAL", 9, "INGLATERRA"),
#     ("EN05", "CHELSEA", 10, "INGLATERRA")
# ]

# micursor.executemany("INSERT INTO Equipos VALUES (?,?,?,?)", equipos)




micursor.execute("INSERT INTO Equipos VALUES ('SP03', 'ATLÉTICO DE MADRID', 11, 'ESPAÑA')")


miconexion.commit()

miconexion.close()