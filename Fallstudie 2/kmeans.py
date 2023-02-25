import math
import random
import numpy as np
import matplotlib.pyplot as plt

clusters = []
data = []
# Anzahl der Cluster
k = random.randint(1, 10)


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


def k_means():
    global k, data
    # array wird kopiert um daten bei zu behalten und dabei standartiesiert
    data_kmeans =  (data - np.mean(data)) / np.std(data)
    print("Standatiesierte Daten ")
    print(data_kmeans)
    # Maximale wiederholungen des verfahrens
    maximale_sortier_wiederholungen = 100
    # Anzahl der Cluster ist aktuell einf wert von k
    k = k

    # zufällige wahl der  ersten cluster mittelpunkte in data[]
    # mischt die indexe des arrays zufällig durch und wählt die ersten k davon aus
    mittelpunkt_cluster = data_kmeans[np.random.permutation(len(data_kmeans))[:k]]
    anfang= 0

    for i in range(maximale_sortier_wiederholungen):
        # Berechnet die distanz zwischen den Datenpunkten und den Cluster Mittelpunkten
        # (Wurzel ziehen (np.sum gibt die summer der 2 quadrierten subtraktionen zurück ))
        # form : [[distanz1 zu mitte1, distanz1 zu mitte2 ......... ]
        #        [distanz1 zu mitte1, distanz1 zu mitte2.........]]
        # -1 ist die dimension
        distances = np.sqrt(np.sum((data_kmeans[:, np.newaxis] - mittelpunkt_cluster) ** 2, axis=-1))

        # weist jeden punkt dem cluster zu dem er die niedrigste distanz hat
        # in dem er in der dimesnsion -1 für jeden wert prüdft wo der kleinste wert steht
        labels = np.argmin(distances, axis=-1)

        #  berechnet für jedes "label"(teilcluster) auf basis der zugeordneten wert den neuen mittelwert
        mittelpunkte_neu = np.array([data_kmeans[labels == i].mean(axis=0) for i in range(k)])

        # prüft ob die cluster sich geändert haben :
        # cas 1: ja dann geht die iteration weiter
        # case2: nein das break bricht die for schleife ab und plottet die cluster

        if np.allclose(mittelpunkt_cluster, mittelpunkte_neu):
            break  # wenn sich die zuordnungen nicht mehr ändern wird das programm beendet

        mittelpunkt_cluster = mittelpunkte_neu
        if anfang ==0:
            plt.scatter(data_kmeans[:, 0], data_kmeans[:, 1], c=labels, cmap='plasma')
            plt.scatter(mittelpunkt_cluster[:, 0], mittelpunkt_cluster[:, 1], c='red', s=10, alpha=0.5)
            plt.show()
            anfang =1

        # Plot the data
    plt.scatter(data_kmeans[:, 0], data_kmeans[:, 1], c=labels, cmap='plasma')
    plt.scatter(mittelpunkt_cluster[:, 0], mittelpunkt_cluster[:, 1], c='black', s=10)
    plt.show()
    #------------------------------------------Symbolische MAin area für die aufrufe _____________________________

a_schritt1()
a_schritt2()
print(f"Number of clusters: {k}")
print("Clusters:")
print(clusters)
print("Data points:")
print(data)
k_means()

