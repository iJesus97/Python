from tkinter import *

raiz = Tk()
raiz.title("Interfaz CANSAT ITSA")
largoPantalla = raiz.winfo_screenwidth()
altoPantalla = raiz.winfo_screenheight()
raiz.geometry("%dx%d" % (largoPantalla, altoPantalla))

Color = BooleanVar()

def SeleccionColor(x):
	if x:
		ColorPrincipal = "#000000"
		ColorSecundario = "#FFFFFF"
	else:
		ColorPrincipal = "#FFFFFF"
		ColorSecundario = "#000000"
	return ColorPrincipal, ColorSecundario

def ActualizarColores():
	Color1, Color2  = SeleccionColor(Color.get())
	raiz.config(menu = barraMenu, bg = Color1)
	SelecPuerto1.config(bg = Color1, fg = Color2)
	BotonManual.config(bg = Color1, fg = Color2)
	ejemplo = Label(raiz, text = "Aquí irá la interfaz", fg= Color2, bg= Color1)
	ejemplo.config(bg = x)

SelecPuerto1 = Checkbutton(raiz, text = "Dark", variable = Color, activeforeground="#0743F5", activebackground="#FFF", cursor="hand1")
SelecPuerto1.grid(row = 0, column = 20, sticky = 'W')

BotonManual = Button(raiz, text = "Actualizar", command = ActualizarColores, activeforeground="#0743F5", activebackground="#FFF", relief="flat", overrelief="raised")
BotonManual.grid(row = 1, column = 20)

BotonInactivo = Button(raiz, text = "Actualizar", command = ActualizarColores, activeforeground="#0743F5", activebackground="#FFF", state="disabled")
BotonInactivo.grid(row = 15, column = 0)

barraMenu = Menu(raiz)

menuPrograma = Menu(barraMenu, tearoff = 0)
menuPrograma.add_separator()
menuPrograma.add_command(label = "Salir")

menuPuertoS = Menu(barraMenu, tearoff = 0)
menuPuertoS.add_command(label = "Seleccionar puerto serial", command = DefinirPuertoS)
menuPuertoS.add_command(label = "Ver serial", command = ChequeoConexion)

menuIMU = Menu(barraMenu, tearoff = 0)

menuBBDD = Menu(barraMenu, tearoff = 0)

menuAyuda = Menu(barraMenu, tearoff = 0)
menuAyuda.add_command(label = "Licencia", command = AvisoLicencia)
menuAyuda.add_command(label = "Acerca de...", command = lambda:infoAcercaDe("Acerca de...", "Interfaz para CANSAT ITSA 2019\nCreada en Python 3.x"))

barraMenu.add_cascade(label = "Programa", menu = menuPrograma)
barraMenu.add_cascade(label = "Puerto Serial", menu = menuPuertoS)
barraMenu.add_cascade(label = "IMU", menu = menuIMU)
barraMenu.add_cascade(label = "Base de datos", menu = menuBBDD)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

raiz.mainloop()