import random

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np


def test():
    # Zufällige Koordinaten generieren
    x = [random.uniform(-100, 100) for _ in range(100)]
    y = [random.uniform(-100, 100) for _ in range(100)]
    # Diagramm erstellen
    fig, ax = plt.subplots()
    # Koordinaten plotten
    ax.scatter(x, y)
    # Diagramm anzeigen[
    plt.show()

cluster = []
datenpunkte = []
clusterx = []
clustery = []


def teil_a():


    #  zufällige wahl der Clusteranzahl
    k = random.randint(1, 10)

    # hier werden die zufälligen punkte ci erzeugt
    for i in range(k):
        x = [random.uniform(-100, 100)]
        y = [random.uniform(-100, 100)]
        anfangswert = [x, y]
        cluster.append(anfangswert)

    clusterx = [point[0] for point in cluster ]
    clustery = [point[1] for point in cluster]
    plt.scatter(clusterx,clustery)
    plt.show()

    for i in cluster:
        datenpunkte_add(k)

    datenx = [point[0] for point in datenpunkte]
    dateny = [point[1] for point in datenpunkte]
    plt.scatter(datenx,dateny)
    plt.show()

    print(datenpunkte)


def datenpunkte_add(k):
    print("hier")
    sigma = random.uniform(1, 3)
    ci = k
    for i in range(100):
        einerAusHundert = random.normalvariate(ci, sigma)
        einerAusHundert2 = random.normalvariate(ci, sigma)
        wert = [einerAusHundert, einerAusHundert2]
        datenpunkte.append(wert)


teil_a()


def teil_b():
    print("Wie viele Cluster soll es im K-MEAN ALGO geben ? ")
    anzahlCluster = int(input("Anzahl:"))
    print("Wie viele Daten soll es im K-MEAN ALGO geben ? ")
    anzahlDaten = int(input("Anzahl:"))
    data = []
    mittelwerte = []

    for i in range(anzahlDaten):
        zahl = random.randint(-30000, 30000)
        zahl2 = random.randint(-30000, 30000)
        y = [zahl, zahl2]
        data.append(y)

    plt.plot(data, "x")
    plt.show()
    plt.plot(mittelwerte, 'x')
    plt.show()

# test()

# teil_b()
#
# deviation = np.random.uniform(1, 3)

# X, y_true = make_blobs(
#    n_samples=100,
#    centers=100,
#    cluster_std=deviation,
#    random_state=None
# )

# ranCluster = np.random.randint(1, 10)
# kmeans = KMeans(
#   init="random",
# n_clusters=ranCluster,
#  n_init=10,
# max_iter=300,
# random_state=42
# )

# plt.scatter(X[:, 0], X[:, 1], s=50)
# plt.show()
