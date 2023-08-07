from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
	pagina =  """<html>
	<body>
	<h1>Un texto cualquiera<h1>
	</body>
	<html>
	"""
	return HttpResponse(pagina)

def otraFuncion(request):
	return HttpResponse("Probando una nueva vista")

def fechaHora(request):
	fecha_actual = datetime.datetime.now()
	pagina =  """<html>
	<body>
	<h3>Fecha y hora actuales %s<h3>
	</body>
	<html>
	""" % fecha_actual
	return HttpResponse(pagina)

def funcionRecepcion(request, anio):
	edadActual = 18
	periodo = anio - 2019
	edadFutura = edadActual + periodo
	pagina =  """<html>
	<body>
	<h3>En el año %s tendrás %s años<h3>
	</body>
	<html>
	""" % (anio, edadFutura)
	return HttpResponse(pagina)

def funcionRecepciondos(request, edad, anio):
	periodo = anio - 2019
	edadFutura = edad + periodo
	pagina =  """<html>
	<body>
	<h3>En el año %s tendrás %s años<h3>
	</body>
	<html>
	""" % (anio, edadFutura)
	return HttpResponse(pagina)