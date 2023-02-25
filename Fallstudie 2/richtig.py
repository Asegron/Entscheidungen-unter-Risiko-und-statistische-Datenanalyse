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
X_norm = scaler.fit_transform(data)

# Berechnung der Distanzmatrix
dist_matrix = linkage(X_norm, method='average', metric='euclidean')

# Erstellung des Dendrogramms
dend = dendrogram(dist_matrix)

# Anzeigen des Dendrogramms
plt.title("Dendrogram")
plt.xlabel("Datenpunkte")
plt.ylabel("Abstand")
plt.show()