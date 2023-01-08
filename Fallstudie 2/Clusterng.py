import random
import math

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np

cluster = []
datenpunkte = []
clusterx = []
clustery = []

k = random.randint(1, 10)



def teil_a():
    mittelwert = 0
    #  zufällige wahl der Clusteranzahl
    print(k)
    i = 0
    z=0
    for x in range(k):
        x= x+1
        z =z+x
        print(z)

    mittelwert= z/k

    print(mittelwert)
        # hier werden die zufälligen punkte ci erzeugt


    print(cluster)
    plt.scatter([point[0] for point in cluster], [point[1] for point in cluster])
    plt.show()

    schleifen_objekt = iter(cluster)

    while True:

        try:
            naechster_wert = next(schleifen_objekt)
        except StopIteration:
            break

        else:
            for i in range(10):
                sigma = random.uniform(1, 3)  # zufälligen Standardabweichung(sigma = 1, … , 3)
                x = [random.normalvariate(mittelwert,sigma)]
                y = [random.normalvariate(mittelwert,sigma)]
                datenwert = [x, y]
                datenpunkte.append(datenwert)

        print(datenpunkte)
        print('for fertig ')

    print(datenpunkte)
    plt.scatter([point[0] for point in datenpunkte], [point[1] for point in datenpunkte])
    plt.show()







def teil_b():
    mittelpunkte= []
    for i in range(k):
        auswahl = random.randint(1,len(datenpunkte)-1)
        mittelpunkte.append(datenpunkte[auswahl])

    print("-----------------------------------------")
    print(mittelpunkte)

    abstand(mittelpunkte[0],mittelpunkte[1])


def abstand (x, y):
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))



teil_a()
teil_b()
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
# maximale_sortier_wiederholungen=300,
# random_state=42
# )

# plt.scatter(X[:, 0], X[:, 1], s=50)
# plt.show()
