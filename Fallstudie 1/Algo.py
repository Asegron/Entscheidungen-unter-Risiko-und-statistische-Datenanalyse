import csv
import numpy as numpy
import pandas as pandas
from tkinter import *
from PIL import ImageTk, Image
from statistics import mean

MerkmalReihe = 0  # um merkmale aus der csv zu extrahieren
MerkmalNamenListe = list()  # liste in der sie Merkmal namen Gespeichert werden
Merkmal0 = list()
Merkmal1 = list()
Merkmal2 = list()
Merkmal3 = list()
Merkmal4 = list()
Merkmal5 = list()
MerkmalAnzahl = 0

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

        # Filter out the integer values using the filter() function
        filtered_Merkmal2 = filter(lambda x: x.isdigit(), Merkmal2)
        # Convert the iterator to a list
        filtered_Merkmal2 = list(filter(lambda x: x.isdigit(), Merkmal2))
        float_list2 = [float(i) for i in filtered_Merkmal2]

        # Filter out the integer values using the filter() function
        filtered_Merkmal3 = filter(lambda x: x.isdigit(), Merkmal3)
        # Convert the iterator to a list
        filtered_Merkmal3 = list(filter(lambda x: x.isdigit(), Merkmal3))
        float_list3 = [float(i) for i in filtered_Merkmal3]

        # Filter out the integer values using the filter() function
        filtered_Merkmal4 = filter(lambda x: x.isdigit(), Merkmal4)
        # Convert the iterator to a list
        filtered_Merkmal4 = list(filter(lambda x: x.isdigit(), Merkmal4))
        float_list4 = [float(i) for i in filtered_Merkmal4]

        if stichprobenkennwerteIndex.get() == 0:
            text.insert(END, "Lebensdauer" + " " + str(mean(float_list2)) + "\n" +
                        "T0" + " " + str(mean(float_list3)) + "\n" +
                        "T30" + " " + str(mean(float_list4)) + "\n"
                        )
        if stichprobenkennwerteIndex.get() == 1:
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 2:
            text.insert(END, "kek")
        if stichprobenkennwerteIndex.get() == 3:
            text.insert(END, "kek")
        if stichprobenkennwerteIndex.get() == 4:
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 5:
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 6:
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 7:
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
