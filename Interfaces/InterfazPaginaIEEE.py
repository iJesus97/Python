from tkinter import Tk, Label, StringVar, OptionMenu, Button, Frame, Entry

elementsToEdit = ["Inicio", "Acerca de", "Membresía", "Contacto"]

root = Tk()
root.title("IEEE")
root.config(bg = "#002855")
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))

menuSelection = StringVar()
menuSelection.set("Inicio")
newTitles = StringVar()
newDates = StringVar()
newAutor = StringVar()
newParagraphs = StringVar()

def printSelection():
    print(menuSelection.get())
    mainContainer.destroy()
    if menuSelection.get() == elementsToEdit[0]:
        entryFrame = Frame(root)
        entryFrame.pack()
        titlePost = Entry(entryFrame, textvariable = )
    else:
        mainContainer.destroy()

mainContainer = Frame(root)
mainContainer.config(padx = 10, pady = 20)
mainContainer.pack()

labelSelection = Label(mainContainer, text = "Seleccione el archivo a editar:")
labelSelection.grid(row = 0, column = 0, columnspan = 2)

fileMenuSelection = OptionMenu(mainContainer, menuSelection, elementsToEdit[0], elementsToEdit[1], elementsToEdit[2], elementsToEdit[3])
fileMenuSelection.grid(row = 1, column = 0)

okButton = Button(mainContainer, text = "Ok", command = lambda:printSelection())
okButton.grid(row = 1, column = 1)

root.mainloop()

def editFile():
    f = open('holamundo.html','w')

    mensaje = """<html>
    <head></head>
    <body><p>Hola Mundo!</p></body>
    </html>"""

    f.write(mensaje)
    f.close()