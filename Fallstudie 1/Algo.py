import csv
from collections import Counter
import numpy
import statistics
import matplotlib.pyplot as plt
import math
from prettytable import PrettyTable
import pandas as pandas
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plot
from numpy import mean, var

MerkmalReihe = 0  # um Merkmale aus der csv zu extrahieren
MerkmalNamenListe = list()  # Liste in der die Merkmalnamen gespeichert werden
Merkmal0 = list()
Merkmal1 = list()
Merkmal2 = list()
Merkmal3 = list()
Merkmal4 = list()
Merkmal5 = list()
MerkmalAnzahl = 0

# Liest die csv-Datei ein und fügt sie zu einer Liste zusammen
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

    # Erstellt Fenster mit Titel
    root = Tk()
    root.title('Statistische Auswertungen')

    # Variabeln zum Aufruf der verschiedenen Auswahlmöglichkeiten
    haeufigkeitsIndex = IntVar()
    diagrammIndex = IntVar()
    stichprobenkennwerteIndex = IntVar()
    werteIndex = IntVar()

    # Auswahlmöglichkeiten im Array gespeichert
    haeufigkeitstabellen = ["Häufigkeitstabelle", "Klassenhäufigkeitstabelle"]
    diagramme = ["Tabelle", "Balkendiagramm", "Tortendiagramm"]
    stichprobenkennwerte = ["Mittelwert", "Median", "Quantile", "Modus", "Spannweite", "Quartilsabstand", "Streuung",
                            "Standardabweichung"]
    werte = ["MOD", "Fehler", "Lebensdauer", "T0", "T30", "Zuverl"]

    # Radiobuttons die dem Benutzer ermöglichen eine Auswahl zu tätigen
    # for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(haeufigkeitstabellen)):
        radiobutton1 = Radiobutton(root, text=haeufigkeitstabellen[index], variable=haeufigkeitsIndex, value=index)
        radiobutton1.pack(anchor=W)
    for index in range(len(diagramme)):
        radiobutton2 = Radiobutton(root, text=diagramme[index], variable=diagrammIndex, value=index, padx=25)
        radiobutton2.pack(anchor=W)

    # for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(werte)):
        radiobutton3 = Radiobutton(root, text=werte[index], variable=werteIndex, value=index)
        radiobutton3.pack(anchor=W)

    # for-Loop läuft über die Arrays mit gespeicherten Auswahlmöglichkeiten
    for index in range(len(stichprobenkennwerte)):
        radiobutton4 = Radiobutton(root, text=stichprobenkennwerte[index], variable=stichprobenkennwerteIndex,
                                   value=index, padx=25)
        radiobutton4.pack(anchor=W)

    del Merkmal0[0]
    del Merkmal1[0]
    del Merkmal2[0]
    del Merkmal3[0]
    del Merkmal4[0]
    del Merkmal5[0]
    # Filtert die Zahlen und wandelt sie in floats um.
    # Konvertiert dann die String-Listen in Zahlen-Listen.
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


    # berechnet den Durchschnitt
    def average(lst):
        berechnung = sum(lst) / len(lst)
        rounded = round(berechnung, 2)
        return rounded


    # berechnet den Median
    def median(lst):
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2

        if (lstLen % 2):
            berechnung1 = sortedLst[index]
            rounded1 = round(berechnung1, 2)
            return rounded1
        else:
            berechnung2 = (sortedLst[index] + sortedLst[index + 1]) / 2.0
            rounded2 = round(berechnung2, 2)
            return rounded2


    # berechnet die Quantile. Erster Parameter die Liste, zweiter Parameter das gewünschte Quantil, z.B. 0.25 für das untere Quantil.
    def quantile(lst, p):
        lst = sorted(lst)
        n = len(lst)
        q = p * (n - 1)
        i = int(q)
        if i == n - 1:
            return list[i - 1]
        else:
            return lst[i - 1] + (q - i) * (lst[i] - lst[i - 1])


    # Berechnet den Modus, das heißt das Element das am meisten in der Spalte eines Merkmals vorkommt.
    def modus(lst):
        counter = {}
        for i in lst:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        # Sucht nach dem Schlüssel mit den meisten Elementen.
        max_count = max(counter.values())
        for key, value in counter.items():
            if value == max_count:
                return key
            if len(counter.keys()) == 1:
                raise ValueError('Alle Werte haben die gleiche Häufigkeit!')


    # Berechnet die Spannweite in dem das kleinste Element einer liste von dem größten Element einer Liste subtrahiert wird.
    def spannweite(lst):
        berechnung = max(lst) - min(lst)
        rounded = round(berechnung, 2)
        return rounded


    # Berechnet den Quartilsabstand in dem man das erste Quartil vom dritten Quartil subtrahiert.
    def quartilsabstand(lst):
        quantil25 = quantile(lst, 0.25)
        quantil75 = quantile(lst, 0.75)
        berechnung = quantil75 - quantil25
        rounded = round(berechnung, 2)
        return rounded


    # Gibt die Streuung zurück
    def streuung(lst):
        formel = sum([(x - average(lst)) ** 2 for x in lst]) / len(lst)
        return formel


    # Gibt die Standardabweichung zurück in dem aus der Streuung die Wurzel gezogen wird.
    def standardabweichung(lst):
        return math.sqrt(streuung(lst))


    def haeufigkeitstabelle(lst):
        haeufigkeitstabelle = {}
        for i in lst:
            if i in haeufigkeitstabelle:
                haeufigkeitstabelle[i] += 1
            else:
                haeufigkeitstabelle[i] = 1
        return haeufigkeitstabelle


    def haeufigkeitstabellenerstellung(haeufigkeitstabelle):
        table = PrettyTable()
        table.field_names = ["Wert", "Häufigkeit"]
        for word, frequency in haeufigkeitstabelle.items():
            table.add_row([word, frequency])
        return table


    def balkendiagramm(lst):
        counter = Counter(lst)
        keys = list(counter.keys())
        values = list(counter.values())

        plt.bar(keys, values)
        plt.title('Balkendiagramm')
        plt.show()


    def tortendiagramm(lst):
        counter = Counter(lst)
        keys = list(counter.keys())
        values = list(counter.values())

        plt.pie(values, labels=keys)
        plt.title('Tortendiagramm')
        plt.show()


    # Funktion, die die Kennzahlen der csv-Datei auswertet.
    # Logische Auswahl der Indices läuft über die Radiobuttons das die jeweilige Kennzahl auswählt.
    def kennwertberechnung():

        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 0:  # Mittelwert
            text.insert(END, "Lebensdauer" + " " + str(average(filtered_Merkmal2)))
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 0:  # Mittelwert
            text.insert(END, "T0" + " " + str(average(filtered_Merkmal3)))
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 0:  # Mittelwert
            text.insert(END, "T30" + " " + str(average(filtered_Merkmal4)))

        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 1:  # Median
            text.insert(END, "Lebensdauer" + " " + str(median(filtered_Merkmal2)))
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 1:  # Median
            text.insert(END, "T0" + " " + str(median(filtered_Merkmal3)))
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 1:  # Median
            text.insert(END, "T30" + " " + str(median(filtered_Merkmal4)))

        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 2:  # Quantile
            text.insert(END, "Lebensdauer" + " 25% " + str(quantile(filtered_Merkmal2, 0.25)) + "\n" +
                        "Lebensdauer" + " 50% " + str(quantile(filtered_Merkmal2, 0.50)) + "\n" +
                        "Lebensdauer" + " 75% " + str(quantile(filtered_Merkmal2, 0.75)) + "\n"
                        )
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 2:  # Quantile
            text.insert(END, "T0" + " 25% " + str(quantile(filtered_Merkmal3, 0.25)) + "\n" +
                        "T0" + " 50% " + str(quantile(filtered_Merkmal3, 0.50)) + "\n" +
                        "T0" + " 75% " + str(quantile(filtered_Merkmal3, 0.75)) + "\n"
                        )
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 2:  # Quantile
            text.insert(END, "T30" + " 25% " + str(quantile(filtered_Merkmal2, 0.25)) + "\n" +
                        "T30" + " 50% " + str(quantile(filtered_Merkmal2, 0.50)) + "\n" +
                        "T30" + " 75% " + str(quantile(filtered_Merkmal2, 0.75)) + "\n"
                        )
        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 3:  # Modus
            text.insert(END, "Lebensdauer" + " " + str(modus(filtered_Merkmal2)))
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 3:  # Modus
            text.insert(END, "T0" + " " + str(modus(filtered_Merkmal3)))
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 3:  # Modus
            text.insert(END, "T30" + " " + str(modus(filtered_Merkmal4)))

        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 4:  # Quartilsabstand
            text.insert(END, "Lebensdauer" + " " + str(spannweite(filtered_Merkmal2))
                        )
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 4:  # Quartilsabstand
            text.insert(END, "T0" + " " + str(spannweite(filtered_Merkmal3))
                        )
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 4:  # Quartilsabstand
            text.insert(END, "T30" + " " + str(spannweite(filtered_Merkmal4))
                        )

        if werteIndex.get() == 2 and stichprobenkennwerteIndex.get() == 5:  # Quartilsabstand
            text.insert(END, "Lebensdauer" + " " + str(quartilsabstand(filtered_Merkmal2))
                        )
        if werteIndex.get() == 3 and stichprobenkennwerteIndex.get() == 5:  # Quartilsabstand
            text.insert(END, "T0" + " " + str(quartilsabstand(filtered_Merkmal3))
                        )
        if werteIndex.get() == 4 and stichprobenkennwerteIndex.get() == 5:  # Quartilsabstand
            text.insert(END, "T30" + " " + str(quartilsabstand(filtered_Merkmal4))
                        )

        if stichprobenkennwerteIndex.get() == 6:  # Streuung
            text.insert(END, "Lebensdauer" + " " + str(streuung(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(streuung(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(streuung(filtered_Merkmal4))
                        )
        if stichprobenkennwerteIndex.get() == 7:  # Standardabweichung
            text.insert(END, "Lebensdauer" + " " + str(standardabweichung(filtered_Merkmal2)) + "\n" +
                        "T0" + " " + str(standardabweichung(filtered_Merkmal3)) + "\n" +
                        "T30" + " " + str(standardabweichung(filtered_Merkmal4))
                        )


    def haeufigkeitstabellenerstellung():
        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 0 and diagrammIndex.get() == 0:  # Mod
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )

        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 1 and diagrammIndex.get() == 0:  # Fehler
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )
        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 2 and diagrammIndex.get() == 0:  # Lebensdauer
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )

        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 3 and diagrammIndex.get() == 0:  # T0
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )

        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 4 and diagrammIndex.get() == 0:  # T30
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )

        if haeufigkeitsIndex.get() == 0 and werteIndex.get() == 5 and diagrammIndex.get() == 1:  # Zuverl
            text.insert(END, "T0" + " " + str(haeufigkeitstabellenerstellung((haeufigkeitstabelle(filtered_Merkmal0))))
                        )

        if werteIndex.get() == 0 and diagrammIndex.get() == 1:  # Mod
            balkendiagramm(filtered_Merkmal0)

        if werteIndex.get() == 1 and diagrammIndex.get() == 1:  # Fehler
            balkendiagramm(Merkmal1)

        if werteIndex.get() == 2 and diagrammIndex.get() == 1:  # Lebensdauer
            balkendiagramm(filtered_Merkmal2)

        if werteIndex.get() == 3 and diagrammIndex.get() == 1:  # T0
            balkendiagramm(filtered_Merkmal3)

        if werteIndex.get() == 4 and diagrammIndex.get() == 1:  # T30
            balkendiagramm(filtered_Merkmal4)

        if werteIndex.get() == 5 and diagrammIndex.get() == 1:  # Zuverl
            balkendiagramm(filtered_Merkmal5)

        if werteIndex.get() == 0 and diagrammIndex.get() == 2:  # Mod
            tortendiagramm(filtered_Merkmal0)

        if werteIndex.get() == 1 and diagrammIndex.get() == 2:  # Fehler
            tortendiagramm(Merkmal1)

        if werteIndex.get() == 2 and diagrammIndex.get() == 2:  # Lebensdauer
            tortendiagramm(filtered_Merkmal2)

        if werteIndex.get() == 3 and diagrammIndex.get() == 2:  # T0
            tortendiagramm(filtered_Merkmal3)

        if werteIndex.get() == 4 and diagrammIndex.get() == 2:  # T30
            tortendiagramm(filtered_Merkmal4)

        if werteIndex.get() == 5 and diagrammIndex.get() == 2:  # Zuverl
            tortendiagramm(filtered_Merkmal5)


    # Button zur Erstellung der Häufigkeitstabellen und Diagramme. Ruft die Funktion dafür auf.
    Button(root, text="Erstelle Häufigkeitstabelle!", command=haeufigkeitstabellenerstellung).pack()

    # Button zur Erstellung der Kennzahlen. Ruft die Funktion dafür auf.
    Button(root, text="Berechne Kennwert!", command=kennwertberechnung).pack(pady=10)


    # Hilfsfunktion und Anweisungen für einen "Clear" Button der das Textfeld löscht in dem der Output eingespeist wurde.
    def clear():
        text.delete(1.0, END)


    clear_button = Button(root, text="Text löschen", command=clear).pack()
    text = Text(root, width=40, height=5)
    text.pack()

    # Erstellt das Fenster für die Anwendung
    Canvas(root, width=200, height=50).pack()
    # Startet das Programm als Schleife
    root.mainloop()
