import sqlite3


try:
	miConexion = sqlite3.connect("Alumnos")
	miCursor = miConexion.cursor()
	miCursor.execute("CREATE TABLE PRODUCTOS9 (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(50), MATRICULA VARCHAR(6) UNIQUE, TIMESTAMP CURRENT_TIME)")

	x = "Otromen"
	y = "KEEEEE"

#	if art == "197
#	elif art == "123":
#		x = "Oscoloscopio 2"
#	else:
#		x = "otro"

	#UPDATE `valores` SET `Distancia`=666,`Inclinacion`="No inclinado",`Tamanio`=666 WHERE Distancia = 0

	#unString = "INSERT INTO PRODUCTOS VALUES (null," + "\'" + x  + "\'" + "," + "\'" + y + "\'" + ")"
	unString = "INSERT INTO PRODUCTOS9 VALUES (null, \'%s\',\'%s\', null)" % (x, y)
	
	miCursor.execute(unString)
	miConexion.commit()
	print(0/0)
	print("Los valores ingresados son: %s y %s" % (x, y))

except sqlite3.IntegrityError:
	print("El artículo seleccionado ya está en uso")

except sqlite3.OperationalError:
	print("Se ha intentado crear dos veces la misma tabla")
except ZeroDivisionError:
	print("No se puede dividir entre 0")#, end = "")
except NameError:
	print("Otro error de Python")
finally:
	miConexion.close()
	for i in "SeEjecutaraTantasVecesComoHayaCaracteresEnElString":
		print(i, end = " ")
