from serial import Serial

def BuscaSerial(x):
	try:
		PMaximo = x
		print("El número de puertos a buscar serán:", PMaximo)
		for x in range(1,PMaximo):
			Numero = '%s' % x
			Puerto = "COM" + Numero
			try:
				puerto = Serial('%s' %Puerto, 9600)
				puerto.close()
			except:
				continue
			finally:
				pass
			break

		if x != PMaximo-1:
			PuertoEncontrado1 = Puerto

			for y in range(x+1,PMaximo):
				Numero2 = '%s' % y
				Puerto2 = "COM" + Numero2
				try:
					puerto2 = Serial('%s' %Puerto2, 9600)
					puerto2.close()
				except:
					continue
				finally:
					pass
				break

			if y != PMaximo-1:
				PuertoEncontrado2 = Puerto2
				for z in range(y+1,PMaximo):
					Numero3 = '%s' %z
					Puerto3 = "COM" + Numero3
					try:
						puerto3 = Serial('%s' %Puerto3, 9600)
						puerto3.close()
					except:
						continue
					finally:
						pass
					break
				if z != PMaximo-1:
					PuertoEncontrado3 = Puerto3
			else:
				PuertoEncontrado2 = "No hay segundo puerto disponible"
				PuertoEncontrado3 = "No hay tercer puerto disponible"
		else: 
			PuertoEncontrado1 = "No hay puertos disponibles"
			PuertoEncontrado2 = "No hay segundo puerto disponible"
			PuertoEncontrado3 = "No hay tercer puerto disponible"
	except:
		pass
	finally:
		return PuertoEncontrado1, PuertoEncontrado2, PuertoEncontrado3
