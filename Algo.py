import csv
import numpy as numpy
import pandas as pandas


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
    df = pandas.DataFrame(

    )

with open('Motoren.csv') as daten:
    reader = csv.reader(daten, delimiter=';')

    merkmal1()
