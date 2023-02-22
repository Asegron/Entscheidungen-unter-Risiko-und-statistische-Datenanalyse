import numpy as np
import matplotlib.pyplot as plt
import random

clusters = []
# Anzahl der Cluster generieren.
k = random.randint(1, 10)

# Erstelle Daten
data = np.random.uniform(-100, 100, (k, 2))
data_normalized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Euklidische Distanz berechnet die direkte Entfernung zwischen zwei Punkten.
def euklidischer_abstand(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Berechnet die Distanz zwischen Clustern,
# indem der durchschnittliche Abstand zwischen allen Paaren von Punkten aus verschiedenen Clustern berechnet wird.
def average_linkage(cluster1, cluster2):
    durchschnittliche_entfernung = 0
    for a in cluster1:
        for b in cluster2:
            durchschnittliche_entfernung += euklidischer_abstand(a, b)
    durchschnittliche_entfernung /= len(cluster1) * len(cluster2)
    return durchschnittliche_entfernung

# der Algorithmus arbeitet "buttom-up".
# Das heißt, dass bei jeder Iteration ähnlichste Datenpunkte zu Clustern zusammengefasst werden,
# bis alle Datenpunkte Teil eines Clusters sind.
def agglomeratives_clustering(data, k):
    clusters = [[i] for i in range(len(data))]
    while len(clusters) > k:
        min_distance = np.inf
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                distance = average_linkage(data[clusters[i]], data[clusters[j]])
                if distance < min_distance:
                    min_distance = distance
                    merge_clusters = (i, j)
        clusters[merge_clusters[0]] += clusters[merge_clusters[1]]
        del clusters[merge_clusters[1]]
    clusterzugehoerigkeit = np.zeros(len(data), dtype=int)
    for i, cluster in enumerate(clusters):
        for j in cluster:
            clusterzugehoerigkeit[j] = i
    return clusterzugehoerigkeit

# Wende das Clusteringverfahren auf unsere Daten an
clusterzugehoerigkeit = agglomeratives_clustering(data_normalized, 2)

# Visuelle Darstellung
plt.scatter(data[:, 0], data[:, 1], c=clusterzugehoerigkeit)
plt.show()