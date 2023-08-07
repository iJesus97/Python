from tkinter import Button, Tk, mainloop, Checkbutton, BooleanVar
from FuncionesColores import *

x = ""
y = ""

ManipulacionClase = Colores() #Creación del objeto

otraraiz = Tk()
SeleeccionColor = BooleanVar()
SelecPuerto1 = Checkbutton(otraraiz, text = "¿Activar modo obscuro?", variable = SeleeccionColor)
SelecPuerto1.grid(row = 1, column = 2, columnspan = 2, sticky = 'W')
SelecPuerto1.config(bg = "#FFFFFF")

def UI(x):
	raiz = Tk()
	raiz.config(bg = x)
	raiz.mainloop()

def Obten():
	print(SeleeccionColor.get())
	
	if SeleeccionColor.get():
		x, y = ManipulacionClase.ObtenerColores()
		ManipulacionClase.MostrarColores()
		otraraiz.destroy()
		UI(x)
	else:
		x = ""
		y = ""
		ManipulacionClase.CambioNombre(x, y)
		x, y = ManipulacionClase.ObtenerColores()
		otraraiz.destroy()
		UI(y)

Boton1 = Button(otraraiz, text = "OK", command = Obten)
Boton1.grid(row = 2, column = 3)

otraraiz.mainloop()