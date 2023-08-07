import EjemploClases1
from tkinter import Button, Tk, mainloop, Checkbutton, BooleanVar, Menu, Label, StringVar, IntVar, Entry, Radiobutton
from tkinter import messagebox
from BuscaSerial2punto0 import *

global x, y 
x = ""
y = ""

ObjetoColores = EjemploClases1.Colores()

raizColores = Tk()
SeleccionColor = BooleanVar(master=raizColores)
LabelPregunta = Checkbutton(raizColores, text = "¿Activar modo obscuro?", variable = SeleccionColor)
LabelPregunta.grid(row = 0, column = 0, columnspan = 2)
LabelPregunta.config(bg = "#FFFFFF")

def UI(x):
	global raiz
	q, b, c = BuscaSerial(100)

	def DestruccionMasiva():
		valor = messagebox.askokcancel("Salir", "¿Salir de la aplicación?")
		if valor:
			raiz.destroy()

	def infoAcercaDe(x, y):
		messagebox.showinfo(x, y)
	
	def AvisoLicencia():
		messagebox.showwarning("Licencia", "Esto es robado")
		raiz.destroy()

	def ChequeoConexion():
		if a == "Aún no se ha seleccionado un puerto":
			messagebox.showwarning("ERROR", "Aún no se ha seleccionado un puerto serial")
		elif a == "No hay puertos disponibles":
			messagebox.showwarning("ERROR", "El puerto ingresado manualmente no está disponible")
		else:
			infoAcercaDe("Puerto seleccionado", "El puerto seleccionado es: %s" % a)	
	def DefinirPuertoS():
		global ejemplo, a, ingresePuerto, SelecPuerto1, SelecPuerto2
		a = "Aún no se ha seleccionado un puerto"
		ejemplo.destroy()
		largoPantalla = raiz.winfo_screenwidth()
		altoPantalla = raiz.winfo_screenheight()
		raiz.geometry("%dx%d" % (largoPantalla/4, altoPantalla/4))
		raiz.config(bg = x)
		PuertoManual = StringVar()
		PuertoAuto = IntVar()
		lambda:BuscaSerial(100)

		def SelecManual():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2
			BotonManual.destroy()
			BotonAutoma.destroy()
			Parche = Label(raiz, text = "                       ", fg = x, bg = y)
			Parche.grid(row = 2, column = 2, sticky = 'W')
			Parche.config(bg = x)
			ingresePuerto = Entry(raiz, textvariable = PuertoManual)
			ingresePuerto.grid(row = 1, column = 2, sticky = 'W')
			ingresePuerto.config(bg = x, width = 11, justify = "center")

		def SelecAutoma():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2
			BotonAutoma.destroy()
			BotonManual.destroy()
			lambda:Parche.destroy()
			lambda:ingresePuerto.destroy()
			SelecPuerto1 = Radiobutton(raiz, text=q, variable = PuertoAuto, value = 1)
			SelecPuerto1.grid(row = 1, column = 2, columnspan = 2, sticky = 'W')
			SelecPuerto1.config(bg = x)
			if b != "No hay segundo puerto disponible":
				SelecPuerto2 = Radiobutton(raiz, text=b, variable = PuertoAuto, value = 2)
				SelecPuerto2.grid(row = 2, column = 2, columnspan = 2, sticky = 'W')
				SelecPuerto2.config(bg = x)

		def BotonOK():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2, a, x
			
			if PuertoManual.get() == "1" or "2":
				try:
					if PuertoAuto.get() == 1:
						a = q
						if a == "No hay dispositivos disponibles en los puertos COM":
							a = "No conectado"
						SelecPuerto1.destroy()
					elif PuertoAuto.get() == 2:
						a = b
						SelecPuerto2.destroy()

					elif PuertoManual.get() != "":
						a = PuertoManual.get()
						ingresePuerto.destroy()
						Parche.destroy()
						try:
							x = PuertoManual.get()
							filtrao = Filtro(x)
							ProbarPuerto = Serial("COM%s" %filtrao, 9600)
							ProbarPuerto.close()
							a = "COM" + filtrao
						except:
							a = "No hay puertos disponibles"
						finally:
							pass
					
					elif PuertoManual.get() == "":
						ingresePuerto.destroy()
						Parche.destroy()

					else: 
						a = "Aún no se ha seleccionado un puerto"

				finally:
					BotonAutoma.destroy()
					BotonManual.destroy()
					BotonOKSelec.destroy()
					UI(x)
			else:
				pass

		BotonManual = Button(raiz, text = "Manual", command = SelecManual)
		BotonManual.grid(row = 1, column = 1)
		BotonAutoma = Button(raiz, text = "Automático", command = SelecAutoma)
		BotonAutoma.grid(row = 2, column = 1)

		BotonOKSelec = Button(raiz, text = "OK", command = BotonOK)
		BotonOKSelec.grid(row = 3, column = 1, columnspan = 3)


	def inicio():

		global ejemplo, a, raiz
		raiz = Tk()
		raiz.title("Interfaz CANSAT ITSA")
		largoPantalla = raiz.winfo_screenwidth()
		altoPantalla = raiz.winfo_screenheight()
		raiz.geometry("%dx%d" % (largoPantalla, altoPantalla))
		barraMenu = Menu(raiz)
		raiz.config(menu = barraMenu, bg = x)
		ejemplo = Label(raiz, text = "Aquí irá la interfaz", fg= y, bg= x)
		ejemplo.grid(row = 0, column = 0, padx = 10)
		ejemplo.config(bg = x)

		menuPrograma = Menu(barraMenu, tearoff = 0)
		menuPrograma.add_separator()
		menuPrograma.add_command(label = "Salir", command = DestruccionMasiva)

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
	
	inicio()

def principal():
	global x, y
	print(SeleccionColor.get())

	if SeleccionColor.get():
		x, y = ObjetoColores.ObtenerColores()
		ObjetoColores.MostrarColores()
		raizColores.destroy()
		UI(x)
	else:
		ObjetoColores.CambioNombre(x, y)
		x, y = ObjetoColores.ObtenerColores()
		raizColores.destroy()
		UI(y)

Boton1 = Button(raizColores, text = "OK", command = principal)
Boton1.grid(row = 1, column = 0, columnspan = 2)	

raizColores.mainloop()