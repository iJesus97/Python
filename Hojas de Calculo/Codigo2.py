from openpyxl import Workbook, load_workbook
from openpyxl.chart import title

try:
   NombreAlumno = input("Ingrese el nombre del alumno: ")
   if NombreAlumno == "":
      raise ValueError
   Matricula = input("Ingrese la matrícula del alumno: ")
   if Matricula == "":
      raise ValueError("No se introdujo ninguna matrícula: ")
   Carrera = input("Especialidad: ")
   if Carrera == "":
      raise ValueError("No se introdujo nombre de la carrera: ")


   libro2 = load_workbook("Amador.xlsx")
   escritura = libro2.get_sheet_by_name("PRECARGA")
   escritura["B5"] = NombreAlumno
   escritura["M5"] = Matricula
   escritura["B6"] = Carrera

   libro2.save(filename = "Amador.xlsx")
   


except ValueError:
   print("El último campo se llenó de forma incorrecta")
finally:
   print("Operación terminada")
