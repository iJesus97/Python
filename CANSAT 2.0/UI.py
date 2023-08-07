import threading
from tkinter import *
from tkinter import messagebox
from BuscaSerial import Busca
import serial

y = "#000000"
x = "#FFFFFF"
#puerto = serial.Serial('COM11', 9600)

try:
	a, b, c = Busca()
	def DestruccionMasiva():
		valor = messagebox.askokcancel("Salir", "¿Salir de la aplicación?")
		if valor:
			raiz.destroy()

	def infoAcercaDe(x, y):
		messagebox.showinfo(x, y)
	
	def AvisoLicencia():
		messagebox.showwarning("Licencia", "Esto es robado")
		raiz.destroy()

	def DefinirPuertoS():
		global ejemplo, a
		a = "Aún no se ha seleccionado un puerto"
		ejemplo.destroy()
		largoPantalla = raiz.winfo_screenwidth()
		altoPantalla = raiz.winfo_screenheight()
		raiz.geometry("%dx%d" % (largoPantalla/4, altoPantalla/4))
		raiz.config(bg = x)
		PuertoManual = StringVar()
		PuertoAuto = IntVar()
		lambda:Busca()		

		def SelecManual():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2
			lambda:SelecPuerto1.destroy()
			lambda:SelecPuerto2.destroy()
			Parche = Label(raiz, text = "                       ", fg = x, bg = y)
			Parche.grid(row = 2, column = 2, sticky = 'W')
			Parche.config(bg = x)
			ingresePuerto = Entry(raiz, textvariable = PuertoManual)
			ingresePuerto.grid(row = 1, column = 2, sticky = 'W')
			ingresePuerto.config(bg = x, width = 11, justify = "center")

		def SelecAutoma():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2
			lambda:Parche.destroy()
			lambda:ingresePuerto.destroy()
			SelecPuerto1 = Radiobutton(raiz, text=a, variable = PuertoAuto, value = 1)
			SelecPuerto1.grid(row = 1, column = 2, columnspan = 2, sticky = 'W')
			SelecPuerto1.config(bg = x)
			SelecPuerto2 = Radiobutton(raiz, text=b, variable = PuertoAuto, value = 2)
			SelecPuerto2.grid(row = 2, column = 2, columnspan = 2, sticky = 'W')
			SelecPuerto2.config(bg = x)

		def BotonOK():
			global Parche, ingresePuerto, SelecPuerto1, SelecPuerto2, a
			#print(PuertoAuto.get())
			#print(PuertoManual.get())
			if PuertoAuto.get() == 1:
				a = "COM 10"
			elif PuertoAuto.get() == 2:
				a = "COM 20"
			elif PuertoManual != "":
				a = PuertoManual.get()
			else: 
				a = "Aún no se ha seleccionado un puerto"
			if PuertoManual.get() != "":
				ingresePuerto.destroy()
				Parche.destroy()
			elif PuertoAuto.get() != 0:
				SelecPuerto1.destroy()
				SelecPuerto2.destroy()

			BotonAutoma.destroy()
			BotonManual.destroy()
			BotonOKSelec.destroy()
			UI()
			

		BotonManual = Button(raiz, text = "Manual", command = SelecManual)
		BotonManual.grid(row = 1, column = 1)
		BotonAutoma = Button(raiz, text = "Automático", command = SelecAutoma)
		BotonAutoma.grid(row = 2, column = 1)

		BotonOKSelec = Button(raiz, text = "OK", command = BotonOK)
		BotonOKSelec.grid(row = 3, column = 1, columnspan = 3)

	raiz = Tk()
	a = "Aún no se ha seleccionado un puerto"
	def UI():
		raiz.title("Interfaz CANSAT ITSA")
		largoPantalla = raiz.winfo_screenwidth()
		altoPantalla = raiz.winfo_screenheight()
		raiz.geometry("%dx%d" % (largoPantalla, altoPantalla))

		global ejemplo, a
		barraMenu = Menu(raiz)
		raiz.config(menu = barraMenu, bg = x)
		ejemplo = Label(raiz, text = "Aquí irá la interfaz", fg= y, bg= x)
		ejemplo.grid(row = 0, column = 0, padx = 10)
		ejemplo.config(bg = x)

		menuPuertoS = Menu(barraMenu, tearoff = 0)
		menuPuertoS.add_command(label = "Seleccionar puerto serial", command = DefinirPuertoS)
		menuPuertoS.add_command(label = "Ver serial", command = lambda:infoAcercaDe("Puerto seleccionado", "El puerto seleccionado es: %s" % a))
		menuPuertoS.add_separator()
		menuPuertoS.add_command(label = "Salir", command = DestruccionMasiva)

		menuAyudaaa = Menu(barraMenu, tearoff = 0)
		menuAyudaaa.add_command(label = "Licencia", command = AvisoLicencia)
		menuAyudaaa.add_command(label = "Acerca de...", command = lambda:infoAcercaDe("Acerca de...", "Interfaz para CANSAT ITSA 2019\nCreada en Python 3.x"))

		barraMenu.add_cascade(label = "Programa", menu = menuPuertoS)
		barraMenu.add_cascade(label = "Ayuda", menu = menuAyudaaa)

	UI()
	raiz.mainloop()
#except:
#	print("Pasó algo")

finally:
	pass