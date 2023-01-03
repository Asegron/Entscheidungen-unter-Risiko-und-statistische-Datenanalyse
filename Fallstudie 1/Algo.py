import csv
import numpy as numpy
import pandas as pandas
MerkmalReihe =0 # um merkmale aus der csv zu extrahieren
MerkmalNamenListe = list() #liste in der sie Merkmal namen Gespeichert werden
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
        MerkmalReihe = MerkmalReihe +1

        if MerkmalReihe >= 1:
            Merkmal0.append(row[0])
            Merkmal1.append(row[1])
            Merkmal2.append(row[2])
            Merkmal3.append(row[3])
            Merkmal4.append(row[4])
            Merkmal5.append(row[5])
        MerkmalReihe = MerkmalReihe +1
    MerkmalReihe= MerkmalReihe -2




    print(MerkmalNamenListe)
    print(Merkmal0)
    print(Merkmal1)
    print(Merkmal2)
    print(Merkmal3)
    print(Merkmal4)
    print(Merkmal5)
    print(MerkmalReihe)




   #merkmal1()
    #merkmal2()
