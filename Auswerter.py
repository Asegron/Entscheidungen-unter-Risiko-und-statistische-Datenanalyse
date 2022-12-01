import csv
from tkinter import *
from tkinter import filedialog

class Auswerter:
     def __init__(self):
        self.window = Tk()
        self.button1 = Button(self.window,text = "Wählen Sie eine CSV-Datei zur Analyse aus!", 
                            ).pack(pady=10)
        self.button2 = Button(self.window,text = "Möchten Sie eine Häufigkeitstabelle oder eine Klassenhäufigkeitstabelle erstellen?").pack(pady=10)
        self.button3 = Button(self.window,text = "Möchten Sie ein Balken- oder ein Tortendiagramm erstellen?").pack(pady=10)
        self.c = Canvas(self.window,
                            width = 400,
                            height = 200)
        self.c.pack()
        self.window.mainloop()

        #Ließt die CSV-Dateien ein
        def inputData():
            filedialog.askopenfilename(filetypes=("*.csv"))

        def create_window(self):
            self.window = Tk.Toplevel(self)

Auswerter()
