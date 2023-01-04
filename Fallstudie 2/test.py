import random
import numpy as np
import matplotlib.pyplot as plt
clusters=[]
data = []
#Anzahl der Cluster
k = random.randint(1, 11)

# Legt die Ausganspunkte der k Cluster an welche dann als Mittelwert dienen
def a_schritt1():
    global clusters, data
    # Cluster anfangspunkte erzeugen
    # ((minimale wertgröße)(maximale wert größe )(k= anzahl der wert )(2 -> es sind tupel -> 2 dimensionaltät ))
    clusters = np.random.uniform(-100, 100, (k, 2))
    # falls numpy hier nicht ok , dann kann man auch so die punkte anlegen
    # for i in range(k):
    #    x = [random.uniform(-100, 100)]
    #    y = [random.uniform(-100, 100)]
    #    clusters.append([x,y])
    print(clusters)
    # zip zieht jeweils die x und die y werte auseinander um sie anschließend darzustellen
    x, y = zip(*clusters)
    plt.scatter(x, y)
    plt.show()






def a_schritt2():
    global data
    for punkte in clusters:
        # der mittelwert it der vorher generierte ausgangspunkt des clusters
        mittelwert = punkte
        sigma = random.randint(1, 3)
        # ((mittelwert (oben generiert ))(sigma ist zufällig zwischen 1 und 3 (vorgabe))(100= anzahl der wert )(2 -> es sind tupel -> 2 dimensionaltät ))
        cluster = np.random.normal(mittelwert, sigma, (100, 2))
        data.append(cluster)
    # Fügt alle arrays die an der keweiligen stellle in data gespeicher sind zu einem größen aray zusammen
    data = np.concatenate(data)

a_schritt1()
a_schritt2()
print(f"Number of clusters: {k}")
print("Clusters:")
print(clusters)
print("Data points:")
print(data)

