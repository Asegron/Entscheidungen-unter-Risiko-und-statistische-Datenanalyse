import random

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np


def teil_a():
    #  zufällige wahl der Clusteranzahl
    k = random.randint(1, 10)
    # Liste in der cluster
    clusters = []
    # Für jedes Cluster einen Ausgangspunkt generieren
    for i in range(k):
        ausgangspunkt = np.random.randint(-100, 100)
        clusters.append(ausgangspunkt)
    # Für jedes Cluster die zufälligen Datenpunkte generieren
    data = []
    for ausgangspunkt in clusters:
        # generieren
        # Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes high).
        # In other words, any value within the given interval is equally likely to be drawn by uniform.
        sigma = random.uniform(1, 3)

        # Unter beachtung der Standart abweichung werden die 100 datenounkte dem daten array hinzugefügt
        point = np.random.normal(ausgangspunkt, sigma,
                                 size=(100, 1))  # size gibt an wie viele daten punkte angelegt werden sollen
        data.append(point)
    # Alle Datenpunkte in einem Array zusammenführen
    data = np.concatenate(data)
    # plottest erst die ausgangspunkte und nach dem schließen die daten custer
    # plt.plot(clusters, 'x')
    # plt.show()
    # plottet die cluster
    plt.plot(data, 'x')
    plt.show()


teil_a()

print("Wie viele Cluster soll es im K-MEAN ALGO geben ? ")
anzahlCluster = int(input("Anzahl:"))




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
