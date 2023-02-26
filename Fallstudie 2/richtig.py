import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import math
import random
import numpy as np
import matplotlib.pyplot as plt

clusters = []
data = []
# Anzahl der Cluster
k = random.randint(1, 10)

# Legt die Datenpunkte an für k zwischen 1 und 10 an
def datenerzeugung():
    global clusters, data
    # Cluster anfangspunkte erzeugen
    # ((minimale wertgröße)(maximale wert größe )(k= anzahl der wert )(2 -> es sind tupel -> 2 dimensionaltät ))
    clusters = np.random.uniform(-100, 100, (k, 2))

    for punkte in clusters:
        # der mittelwert it der vorher generierte ausgangspunkt des clusters
        mittelwert = punkte
        sigma = random.randint(1, 3)
        # ((mittelwert (oben generiert ))(sigma ist zufällig zwischen 1 und 3 (vorgabe))(100= anzahl der wert )(2 -> es sind tupel -> 2 dimensionaltät ))
        cluster = np.random.normal(mittelwert, sigma, (100, 2))
        data.append(cluster)
    # Fügt alle arrays die an der keweiligen stellle in data gespeicher sind zu einem größen aray zusammen
    data = np.concatenate(data)
    plt.scatter(data[:, 0], data[:, 1])
    plt.title("DATENPUNKTE")
    plt.show()
# Beispiel-Daten
datenerzeugung()

# Normalisierung der Daten
scaler = StandardScaler()
x_norm = scaler.fit_transform(data)

# Berechnung des euklidischen Abstands
def euklidischeDistanz(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

#Berechnet den average-linkage für 2 cluster
def averageLinkage(cluster1, cluster2):
    abstand = 0
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            abstand += euklidischeDistanz(cluster1[i], cluster2[j])
    return abstand / (len(cluster1) * len(cluster2))

#Fehlerhafter/unvollständiger Code für das Clustering. Solange es mehr Cluster als k gibt werden Cluster mit größter
#Ähnlichkeit zusammengeführt bis nur noch k Cluster übrig bleiben.
def averageLinkageClustering():
    while len(clusters) > k:
        distances = []
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                distances.append((averageLinkage(clusters[i], clusters[j]), i, j))
            distances.sort()
            min_distance, i, j = distances[0]
            merged_cluster = clusters[i] + clusters[j]
            clusters.pop(j)
            clusters.pop(i)
            clusters.append(merged_cluster)
        return clusters

# Berechnung der Distanzmatrix
dist_matrix = linkage(x_norm , method='average', metric='euclidean')

# Erstellung des Dendrogramms
dend1 = dendrogram(dist_matrix)
# Anzeigen des Dendrogramms
plt.title("Dendrogram")
plt.xlabel("Datenpunkte")
plt.ylabel("Abstand")
plt.show()