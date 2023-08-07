from tkinter import *
import sqlite3

# BASE DE DATOS USUARIOS
Conexion = sqlite3.connect('Usuarios.db')

#Cursor o puntero para realizar acciones
Cursor = Conexion.cursor()
try:
	#	Creación de tabla para la base de datos
	Cursor.execute("CREATE TABLE Usuarios (MATRICULA VARCHAR(5), NOMBRE VARCHAR(50), APELLIDO_PATERNO VARCHAR(50), APELLIDO_MATERNO VARCHAR(50))")	
	#VARCHAR = STRING
except sqlite3.OperationalError:
	print("Se ha tratado de crear una table con el mismo nombre")
finally:
	pass

#Cursor.execute("INSERT INTO Usuarios VALUES ('\s', \'s\')")

Root = Tk()
#Esto es mucho pedo xd
Var1 = StringVar()
Var2 = StringVar()
Var3 = StringVar()
VarMatricula = StringVar()

EntradaM = Entry(Root, textvariable = VarMatricula) 
EntradaM.grid(row = 0, column = 0)

def BotonOKMatricula():
	EntradaM.destroy()
	Boton1.destroy()
	Entrada = Entry(Root, textvariable = Var1) 
	Entrada.grid(row = 0, column = 0)

	Entrada2 = Entry(Root, textvariable = Var2) 
	Entrada2.grid(row = 1, column = 0)

	Entrada3 = Entry(Root, textvariable = Var3) 
	Entrada3.grid(row = 2, column = 0)

	def GuardarDatosVariables():
		w = VarMatricula.get()
		x = Var1.get()
		y = Var2.get()
		z = Var3.get()
		
		try:
			Cursor.execute("INSERT INTO Usuarios VALUES (\'%s\', \'%s\', \'%s\', \'%s\')" %(w, x, y, z))
			Conexion.commit()
		#except:
		#	print("Creo que la cagué")
		finally:
			Root.destroy()

	Boton2 = Button(Root, command = GuardarDatosVariables)
	Boton2.grid(row = 4, column = 0)

Boton1 = Button(Root, command = BotonOKMatricula, text = "OK")
Boton1.grid(row = 1, column = 0)

Root.mainloop()
Cursor.close()
Conexion.close()