import random
import numpy as np
import matplotlib.pyplot as plt

def ausmalenDesFeldes():
    global mach,letzteReihe
    if letzteSplate >0 and letzteReihe<9:
        print("mitte")

        keineSeite()
    if letzteSplate== 0:
        print("links")
        linkeSeite()

    if letzteSplate== 9:
        print("rechts")

        rechteSeite()

    mach= mach+1


def keineSeite():
    global feld, mach, letzteSplate, letzteReihe
    möglichePunkte = []
    # einsetzten des letzten punkts
    punktGleich = (letzteReihe, letzteSplate)
    möglichePunkte.append(punktGleich)
    if letzteReihe < 9:
        punkDrunter = (letzteReihe + 1, letzteSplate)
        möglichePunkte.append(punkDrunter)
    if letzteSplate > 0:
        punktLinks = (letzteReihe, letzteSplate - 1)
        möglichePunkte.append(punktLinks)
    if letzteSplate < 9:
        punktRechts = (letzteReihe, letzteSplate + 1)
        möglichePunkte.append(punktRechts)
    print(möglichePunkte)
    wert = random.random()
    if wert < 0.26:
        letzteReihe = möglichePunkte[0][0]
        letzteSplate = möglichePunkte[0][1]
    if wert < 0.51 and wert > 0.25:
        letzteReihe = möglichePunkte[1][0]
        letzteSplate = möglichePunkte[1][1]
    if wert < 0.76 and wert > 0.50:
        letzteReihe = möglichePunkte[2][0]
        letzteSplate = möglichePunkte[2][1]
    if wert < 1 and wert > 0.75 and len(möglichePunkte)>3:
        letzteReihe = möglichePunkte[3][0]
        letzteSplate = möglichePunkte[3][1]
    feld[letzteReihe][letzteSplate] = 1

def linkeSeite():
    global feld, mach, letzteSplate, letzteReihe
    möglichePunkte = []
    punktNeu = 0
    # einsetzten des letzten punkts
    punktGleich = (letzteReihe, letzteSplate)
    möglichePunkte.append(punktGleich)
    if letzteReihe < 9:
        punkDrunter = (letzteReihe + 1, letzteSplate)
        möglichePunkte.append(punkDrunter)
    if letzteSplate < 9:
        punktRechts = (letzteReihe, letzteSplate + 1)
        möglichePunkte.append(punktRechts)
    print(möglichePunkte)
    wert = random.random()
    if wert < 0.34:
        letzteReihe = möglichePunkte[0][0]
        letzteSplate = möglichePunkte[0][1]
    if wert < 0.67 and wert > 0.33:
        letzteReihe = möglichePunkte[1][0]
        letzteSplate = möglichePunkte[1][1]
    if wert < 1 and wert > 0.66:
        letzteReihe = möglichePunkte[2][0]
        letzteSplate = möglichePunkte[2][1]


def rechteSeite():
    global feld, mach, letzteSplate, letzteReihe
    möglichePunkte = []
    punktNeu = 0
    # einsetzten des letzten punkts
    punktGleich = (letzteReihe, letzteSplate)
    möglichePunkte.append(punktGleich)
    if letzteReihe < 9:
        punkDrunter = (letzteReihe + 1, letzteSplate)
        möglichePunkte.append(punkDrunter)
    if letzteSplate > 0:
        punktLinks = (letzteReihe, letzteSplate - 1)
        möglichePunkte.append(punktLinks)

    print(möglichePunkte)
    wert = random.random()
    if wert < 0.34:
        letzteReihe = möglichePunkte[0][0]
        letzteSplate = möglichePunkte[0][1]
    if wert < 0.67 and wert > 0.33:
        letzteReihe = möglichePunkte[1][0]
        letzteSplate = möglichePunkte[1][1]
    if wert < 1 and wert > 0.66:
        letzteReihe = möglichePunkte[2][0]
        letzteSplate = möglichePunkte[2][1]


feldgroeße = 10  # np zeros nimmt die 10 ,10 für die größe nicht

# feld = feld da 10 x 10 ist un initial mit 0 gefüllt wird
feld = np.zeros((feldgroeße, feldgroeße))
startingxvalue = random.randint(0, 9)
feld[0][startingxvalue] = 1
letzteReihe = 0
letzteSplate = startingxvalue



mach = 1
count =0
while mach<200 :
    ausmalenDesFeldes()
    count=count+1
    print(count)
plt.imshow(feld, cmap='hot')
plt.show()











