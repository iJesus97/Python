class Colores():
   def __init__(self):                 #Edo inicial
      self.__Color1 = "#000000"
      self.__Color2 = "#FFFFFF"

   def Cambio(self):
      self.__Color1 = "#FFFFFF"
      self.__Color2 = "#000000"

   def __Encapsulado(self):            #Metodo encapsulado, no puedes acceder a el desde fuera de la clase
      pass

   def MostrarColores(self):
      print(self.__Color1)
      print(self.__Color2)

   def ObtenerColores(self):
      return self.__Color1, self.__Color2

   def CambioNombre(self, x, y):
      x = self.__Color1
      y = self.__Color2
      return x, y






