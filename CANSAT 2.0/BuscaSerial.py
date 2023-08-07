from serial import Serial

def Busca():
	for x in range(1,100):
		Numero = '%s' % x
		Puerto = "COM" + Numero
		try:
			puerto = Serial(Puerto, 9600)
		except:
			continue
		finally:
			pass
		break

	for x in range(x,100):
		Numero = '%s' % x
		Puerto2 = "COM" + Numero
		try:
			puerto2 = Serial(Puerto2, 9600)
		except:
			puerto2 = "NO"
		finally:
			pass
		break

	for x in range(x,100):
		Numero = '%s' % x
		Puerto3 = "COM" + Numero
		try:
			puerto3 = Serial(Puerto3, 9600)
		except:
			puerto3 = "NO"
		finally:
			pass
		break

	try:
		puerto = Serial(Puerto, 9600)
		puerto.close()
		qwer = "Dispositivo encontrado en el puerto: %s" % Puerto
	except:
		qwer = "No hay dispositivos disponibles en los puertos COM"
	finally:
		print(qwer)

	if puerto2 != "NO":
		print("Otro dispositivo encontrado en el puerto:", Puerto2)
		infoPuerto2 = "Otro dispositivo encontrado en el puerto:", Puerto2
		puerto2.close()
	else:
		infoPuerto2 = "No hay dispositivos en COM2"

	if puerto3 != "NO":
		print("Otro dispositivo encontrado en el puerto:", Puerto3)
		infoPuerto3 = "Otro dispositivo encontrado en el puerto:", Puerto2
		puerto3.close()
	else:
		infoPuerto3 = "No hay dispositivos en COM3"

	return(qwer, infoPuerto2, infoPuerto3)