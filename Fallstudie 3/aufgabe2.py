import random
import numpy as np
import matplotlib.pyplot as plt

feldgröße =10
# feld = feld da 10 x 10 ist un initial mit 0 gefüllt wird
feld = np.zeros((feldgröße, feldgröße))
xachse=random.randint(0, 9)
yachse=0

feld[yachse][xachse]=1


def feldmalen():
    global yachse,xachse,mach


    if xachse>0 and xachse < 9 and yachse<9:
        wert = random.random()
        if wert < 0.26:
            print("rechts")
            yachse=yachse
            xachse=xachse+1

            feld[yachse][xachse]=1


        if wert < 0.51 and wert > 0.25:
            print("links")
            yachse = yachse
            xachse = xachse -1

            feld[yachse][xachse] = 1

        if wert < 0.76 and wert > 0.50:
            print("gleich")
            yachse = yachse
            xachse = xachse

            feld[yachse][xachse] = 1

        if wert <= 1 and wert > 0.75:
            print("drunter")
            yachse = yachse+1
            xachse = xachse

            feld[yachse][xachse] = 1
        mach =mach+1

    if xachse==0 and yachse<9:
        wert = random.random()
        if wert < 0.34:
            print("rechts2")
            yachse = yachse
            xachse = xachse + 1

            feld[yachse][xachse] = 1

        if wert < 0.67 and wert >0.33:
            print("drunter2")
            yachse = yachse+1
            xachse = xachse

            feld[yachse][xachse] = 1

        if wert <= 1 and wert >0.66:
            print("gleich2")
            yachse = yachse
            xachse = xachse

            feld[yachse][xachse] = 1
    mach=mach+1

    if xachse==9 and yachse<9:
        wert = random.random()
        if wert < 0.34:
            print("links3")
            yachse = yachse
            xachse = xachse -1

            feld[yachse][xachse] = 1

        if wert < 0.67 and wert >0.33:
            print("drunter3")
            yachse = yachse+1
            xachse = xachse

            feld[yachse][xachse] = 1

        if wert <= 1 and wert >0.66:
            print("gleich3")
            yachse = yachse
            xachse = xachse

            feld[yachse][xachse] = 1
    mach=mach+1

    if yachse== 9:
        if xachse==0:
            wert = random.random()

            if wert < 0.67 and wert > 0.33:
                print("rechts2")
                yachse = yachse
                xachse = xachse + 1

                feld[yachse][xachse] = 1

            if wert <= 1 and wert > 0.66:
                print("gleich3")
                yachse = yachse
                xachse = xachse

                feld[yachse][xachse] = 1
        mach = mach + 1

        if xachse==9:
            wert = random.random()
            if wert < 0.34:
                print("links3")
                yachse = yachse
                xachse = xachse - 1

                feld[yachse][xachse] = 1

            if wert <= 1 and wert > 0.66:
                print("gleich3")
                yachse = yachse
                xachse = xachse

                feld[yachse][xachse] = 1
        mach = mach + 1


        if xachse>0 and xachse<9:

            wert = random.random()
            if wert < 0.34:
                print("links3")
                yachse = yachse
                xachse = xachse - 1

                feld[yachse][xachse] = 1

            if wert < 0.67 and wert >0.33:
                print("rechts2")
                yachse = yachse
                xachse = xachse + 1

                feld[yachse][xachse] = 1



            if wert <= 1 and wert > 0.66:
                print("gleich3")
                yachse = yachse
                xachse = xachse

                feld[yachse][xachse] = 1
        mach = mach + 1


def feldausgeben():
    global feld
    plt.imshow(feld, cmap='hot')
    plt.show()


# anzeigen des ersten initialen punktes
feldausgeben()
#---------------------------------------
#start des algos
mach = 1

while mach<1000000:
 feldmalen()
 print(yachse,xachse)



feldausgeben()