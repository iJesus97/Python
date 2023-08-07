import sqlite3
miConexion = sqlite3.connect("GestionAlumnos")

miCursor = miConexion.cursor()

#No especificar con el WHERE produce una actualización en toda la tabla o borrar todo en el contenido de la misma
miCursor.execute("UPDATE ALUMNOS SET CARRERA = 'Mecatrónica' WHERE NOMBRE_ALUMNO = 'Juan'")
#miCursor.execute("DELETE FROM ALUMNOS WHERE ID = 4")

miCursor.execute("SELECT * FROM ALUMNOS WHERE NOMBRE_ALUMNO = 'Jose'")
alumno = miCursor.fetchall()

for x in alumno:
	print(x[2])

miConexion.commit()

miConexion.close()

"""	#	Creación de base de datos
miConexion = sqlite3.connect("BaseEjemplo")

	#	Cursor o puntero para realizar acciones
miCursor = miConexion.cursor()

	#	Creación de tabla para la base de datos
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")	#VARCHAR = STRING

	# Adición de un elemento en la tabla
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', '10', 'DEPORTES')")

	# Declaración de múltiples elementos
#variosProductos = [("Camiseta", "20", "DEPORTES"),
#("Vaso", "20", "COCINA"),
#("Guantes", "120", "DEPORTES")
#]

	#	Adición de múltuples elementos a la tabla
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")

	#	 Obtención de datos en forma de lista
variableLista = miCursor.fetchall()

for elemento in variableLista:
	print(elemento)
	i +=1

print("Número total de elementos en la base de datos: ", i)
	#	Confirmación de cambios a la base de datos
miConexion.commit()
	#	Desconexión de la base de datos
miConexion.close()

"""
# '''Para instrucciones muy largas '''
"""miCursor.execute('''
	CREATE TABLE ALUMNOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ALUMNO VARCHAR(50),
	MATRICULA VARCHAR(6) UNIQUE	,
	CARRERA VARCHAR(20))
''')

almunos = [
	("Jose", "IM111001", "Electronica I"),
	("Juan", "IM111002", "Electronica II"),
	("Jess", "IM111003", "Electronica III"),
	("Luis", "IM111004", "Electronica IV")
]

miCursor.executemany("INSERT INTO ALUMNOS VALUES (NULL , ?, ?, ?)", almunos)"""

"""
"""