import tkinter

master = tkinter.Tk()

w = tkinter.Scale(master, from_=0, to=100)
w.pack()

w = tkinter.Scale(master, from_=0, to=200, orient=tkinter.HORIZONTAL)
w.pack()
print(w.get())
master.mainloop()
