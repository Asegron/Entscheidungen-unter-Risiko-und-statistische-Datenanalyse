import csv
import numpy as numpy
import pandas as pandas
from tkinter import *
from PIL import ImageTk, Image

MerkmalReihe = 0  # um merkmale aus der csv zu extrahieren
MerkmalNamenListe = list()  # liste in der sie Merkmal namen Gespeichert werden
Merkmal0 = list()
Merkmal1 = list()
Merkmal2 = list()
Merkmal3 = list()
Merkmal4 = list()
Merkmal5 = list()
MerkmalAnzahl = 0


def merkmal1():
    datencounter = 0
    testlist = list()
    for row in reader:

        if datencounter >= 1:
            testlist.append(row[0])

        datencounter = datencounter + 1
    datencounter = datencounter - 1
    print(datencounter)
    print(testlist)
    counter0 = testlist.count("0")
    counter1 = testlist.count("1")
    print(counter0)
    print(counter1)
    wahrscheinlichkeit0 = (100 / datencounter) * counter0
    wahrscheinlichkeit1 = (100 / datencounter) * counter1
    print(wahrscheinlichkeit0)
    print(wahrscheinlichkeit1)


def merkmal2():
    datencounter2 = 0
    testlist2 = list()
    for row in reader:

        if datencounter2 >= 1:
            testlist2.append(row[1])

        datencounter = datencounter + 1

    datencounter2 = datencounter2 - 1
    print(datencounter2)
    print(testlist2)
    counterA = testlist2.count("A")
    counterB = testlist2.count("B")
    counterC = testlist2.count("C")
    print(counterA)
    print(counterB)
    print(counterC)
    wahrscheinlichkeitA = (100 / datencounter2) * counterA
    wahrscheinlichkeitB = (100 / datencounter2) * counterB
    wahrscheinlichkeitC = (100 / datencounter2) * counterC
    print(wahrscheinlichkeitA)
    print(wahrscheinlichkeitB)
    print(wahrscheinlichkeitC)

#Liest die csb-Datei ein und fügt sie zu einer Liste zusammen
with open('Motoren.csv') as daten:
    reader = csv.reader(daten, delimiter=';')
    for row in reader:
        if MerkmalReihe == 0:
            MerkmalNamenListe.append(row[0])
            MerkmalNamenListe.append(row[1])
            MerkmalNamenListe.append(row[2])
            MerkmalNamenListe.append(row[3])
            MerkmalNamenListe.append(row[3])
            MerkmalNamenListe.append(row[5])
        MerkmalReihe = MerkmalReihe + 1

        if MerkmalReihe >= 1:
            Merkmal0.append(row[0])
            Merkmal1.append(row[1])
            Merkmal2.append(row[2])
            Merkmal3.append(row[3])
            Merkmal4.append(row[4])
            Merkmal5.append(row[5])
        MerkmalReihe = MerkmalReihe + 1
    MerkmalReihe = MerkmalReihe - 2

    #Erstellt Fenster mit Titel
    root = Tk()
    root.title('Statistische Auswertungen')

    #Variabeln zum Aufruf der verschiedenen Auswahlmöglichkeiten
    haeufigkeitsIndex = IntVar()
    diagrammIndex = IntVar()
    stichprobenkennwerteIndex = IntVar()

    #Auswahlmöglichkeiten im Array gespeichert
    haeufigkeitstabellen = ["Häufigkeitstabelle", "Klassenhäufigkeitstabelle"]
    diagramme = ["Balkendiagramm", "Tortendiagramm"]
    stichprobenkennwerte = ["Mittelwert", "Median", "Quantile", "Modus", "Spannweite", "Quartilsabstand", "Streuung",
                        "Standardabweichung"]

    #Radiobuttons die dem Benutzer ermöglichen eine Auswahl zu tätigen
    #for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(haeufigkeitstabellen)):
        radiobutton1 = Radiobutton(root, text=haeufigkeitstabellen[index], variable=haeufigkeitsIndex, value=index)
        radiobutton1.pack(anchor=W)
    for index in range(len(diagramme)):
        radiobutton2 = Radiobutton(root, text=diagramme[index], variable=diagrammIndex, value=index, padx=25)
        radiobutton2.pack(anchor=W)

    #Funktion zur Erstellung der Häufigkeitstabellen. Unfertig und returned null.
    def haeufigkeitstabellenerstellung():
        return None


    #Button zur Erstellung der Häufigkeitstabellen. Ruft die Funktion dafür auf.
    button1 = Button(root, text="Erstelle Häufigkeitstabelle!").pack(pady=10)

    # for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(stichprobenkennwerte)):
        radiobutton1 = Radiobutton(root, text=stichprobenkennwerte[index], variable=stichprobenkennwerteIndex, value=index)
        radiobutton1.pack(anchor=W)

    #Funktion die die Kennzahlen der csv-Datei auswertet.
    #Logische Auswahl der Indices läuft über die Radiobuttons die die jeweilige Kennzahl auswählt.
    def kennwertberechnung():
        if (stichprobenkennwerteIndex.get() == 0):
            datencounter = 0
            testlist = list()
            for row in reader:

                if datencounter >= 1:
                    testlist.append(row[1])

                datencounter = datencounter + 1

        text.insert(END, str(Merkmal0)) #Mittelwert welcher Werte?
        if (stichprobenkennwerteIndex.get() == 1):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 2):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 3):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 4):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 5):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 6):
            text.insert(END, "kekW")
        if (stichprobenkennwerteIndex.get() == 7):
            text.insert(END, "kekW")

    #Button zur Erstellung der Kennzahlen. Ruft die Funktion dafür auf.
    Button(root, text="Berechne Kennwert!", command=kennwertberechnung).pack(pady=10)

    #Helfsmethode und Anweisungen für einen "Clear" Button der das Textfeld löscht indem der Output eingespeist wurde.
    def clear():
        text.delete(1.0, END)
    clear_button = Button(root, text="Text löschen", command=clear).pack()
    text=Text(root, width=40, height=5)
    text.pack()
    
    #Erstellt das Fenster für die Anwendung
    Canvas(root, width=200, height=50).pack()

    #Startet das Programm als Schleife
    root.mainloop()
# print(MerkmalNamenListe)
# print(Merkmal0)
# print(Merkmal1)
# print(Merkmal2)
# print(Merkmal3)
# print(Merkmal4)
# print(Merkmal5)
# print(MerkmalReihe)


# merkmal1()
# merkmal2()
