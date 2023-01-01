import csv

import statistics
import matplotlib.pyplot as plt
import math
import pandas as pandas
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plot
from numpy import mean, var

MerkmalReihe = 0  # um Merkmale aus der csv zu extrahieren
MerkmalNamenListe = list()  # Liste in der die Merkmanamen gespeichert werden
Merkmal0 = list()
Merkmal1 = list()
Merkmal2 = list()
Merkmal3 = list()
Merkmal4 = list()
Merkmal5 = list()
MerkmalAnzahl = 0

#Liest die csv-Datei ein und fügt sie zu einer Liste zusammen
with open('Motoren.csv') as daten:
    reader = csv.reader(daten, delimiter=';')
    for row in reader:
        if MerkmalReihe == 0:
            MerkmalNamenListe.append(row[0])
            MerkmalNamenListe.append(row[1])
            MerkmalNamenListe.append(row[2])
            MerkmalNamenListe.append(row[3])
            MerkmalNamenListe.append(row[4])
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
    diagramme = ["Tabelle", "Balkendiagramm", "Tortendiagramm"]
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

    # for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(stichprobenkennwerte)):
        radiobutton1 = Radiobutton(root, text=stichprobenkennwerte[index], variable=stichprobenkennwerteIndex, value=index)
        radiobutton1.pack(anchor=W)


    def get_number(string):
        try:
            return int(string)
        except ValueError:
            try:
                return float(string)
            except ValueError:
                return None

    del Merkmal0[0]
    del Merkmal1[0]
    del Merkmal2[0]
    del Merkmal3[0]
    del Merkmal4[0]
    del Merkmal5[0]
    # Filter out the integer values using the filter() function
    # Convert the iterator to a list
    float_strings0 = [x.replace(',', '.') for x in Merkmal0]
    float_strings2 = [x.replace(',', '.') for x in Merkmal2]
    float_strings3 = [x.replace(',', '.') for x in Merkmal3]
    float_strings4 = [x.replace(',', '.') for x in Merkmal4]
    float_strings5 = [x.replace(',', '.') for x in Merkmal5]
    filtered_Merkmal0 = [float(x) if '.' in x else int(x) for x in float_strings0]
    filtered_Merkmal2 = [float(x) if '.' in x else int(x) for x in float_strings2]
    filtered_Merkmal3 = [float(x) if '.' in x else int(x) for x in float_strings3]
    filtered_Merkmal4 = [float(x) if '.' in x else int(x) for x in float_strings4]
    filtered_Merkmal5 = [float(x) if '.' in x else int(x) for x in float_strings5]

    #berechnet den Durchschnitt
    def average(lst):
        return sum(lst) / len(lst)
    #berechnet den Median
    def median(lst):
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2

        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1]) / 2.0

    def quantile(lst, quantile):
        return quantile*0.01 * len(lst)

    #Gibt die Streuung zurück
    def streuung(lst):
        count = 0

        for i in range(len(lst)):
            variance = (lst[i] - average(lst)) ** 2
            count += variance
        return count/len(lst)

    #Gibt die Standardabweichung zurück indem aus der Streuung die Wurzel gezogen wird
    def standardabweichung(lst):
        return math.sqrt(streuung(lst))

    def haeufigkeitstabellen(lst):
        lists = {}
        for x in lst:
            if x in lists:
                lists[x] += 1
            else:
                lists[x] = 1
        return lists


    #Funktion die die Kennzahlen der csv-Datei auswertet.
    #Logische Auswahl der Indices läuft über die Radiobuttons die die jeweilige Kennzahl auswählt.
    def kennwertberechnung():

        if stichprobenkennwerteIndex.get() == 0: #Mittelwert
            text.insert(END, "Lebensdauer" + " " + str(average(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(average(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(average(filtered_Merkmal4)) + "\n"
                        )
        if stichprobenkennwerteIndex.get() == 1: #Median
            text.insert(END, "Lebensdauer" + " " + str(median(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(median(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(median(filtered_Merkmal4)) + "\n"
                        )
        if stichprobenkennwerteIndex.get() == 2: #Quantile
            text.insert(END, "Lebensdauer" + " 25% " + str(quantile(filtered_Merkmal2, 25)) + "\n" +
                        "Lebensdauer" + " 50% " + str(quantile(filtered_Merkmal2, 75)) + "\n" +
                        "Lebensdauer" + " 75% " + str(quantile(filtered_Merkmal2, 75)) + "\n" +
                        "T0" + " 25% " + str(quantile(filtered_Merkmal3, 25)) + "\n" +
                        "T0" + " 50% " + str(quantile(filtered_Merkmal3, 75)) + "\n" +
                        "T0" + " 75% " + str(quantile(filtered_Merkmal3, 75)) + "\n" +
                        "T30" + " 25% " + str(quantile(filtered_Merkmal4, 25)) + "\n" +
                        "T30" + " 50% " + str(quantile(filtered_Merkmal4, 75)) + "\n" +
                        "T30" + " 75% " + str(quantile(filtered_Merkmal4, 75)) + "\n"
                        )
        if stichprobenkennwerteIndex.get() == 3: #Modus
            text.insert(END, "kek")
        if stichprobenkennwerteIndex.get() == 4: #Spannweite
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 5: #Quartilsabstand
            text.insert(END, "kekW")
        if stichprobenkennwerteIndex.get() == 6: #Streuung
            text.insert(END, "Lebensdauer" + " " + str(streuung(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(streuung(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(streuung(filtered_Merkmal4))
                        )
        if stichprobenkennwerteIndex.get() == 7: #Standardabweichung
            text.insert(END, Merkmal2[0] + " " + str(standardabweichung(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(standardabweichung(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(standardabweichung(filtered_Merkmal4))
                        )

    def haeufigkeitstabellenerstellung():
        if haeufigkeitsIndex.get() == 0 and diagrammIndex.get() == 0:
            del Merkmal1[0]
            text.insert(END, Merkmal0[0] + " " + str(haeufigkeitstabellen(filtered_Merkmal0)) + "\n" +
                        "Fehler" + " " + str(haeufigkeitstabellen(Merkmal1)) + "\n" +
                        "Lebensdauer" + " " + str(haeufigkeitstabellen(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(haeufigkeitstabellen(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(haeufigkeitstabellen(filtered_Merkmal4)) + "\n" +
                        "Zuverl" + " " + str(haeufigkeitstabellen(filtered_Merkmal5)) + "\n"
                        )

    # Button zur Erstellung der Häufigkeitstabellen und Diagramme. Ruft die Funktion dafür auf.
    Button(root, text="Erstelle Häufigkeitstabelle!", command=haeufigkeitstabellenerstellung).pack()

    #Button zur Erstellung der Kennzahlen. Ruft die Funktion dafür auf.
    Button(root, text="Berechne Kennwert!", command=kennwertberechnung).pack(pady=10)

    #Hilfsfunktion und Anweisungen für einen "Clear" Button der das Textfeld löscht in dem der Output eingespeist wurde.
    def clear():
        text.delete(1.0, END)
    clear_button = Button(root, text="Text löschen", command=clear).pack()
    text=Text(root, width=40, height=5)
    text.pack()

    #Erstellt das Fenster für die Anwendung
    Canvas(root, width=200, height=50).pack()
    #Startet das Programm als Schleife
    root.mainloop()
