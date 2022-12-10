import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np

deviation = np.random.uniform(1, 3)

X, y_true = make_blobs(
    n_samples=100,
    centers=100,
    cluster_std=deviation,
    random_state=None
)


ranCluster = np.random.randint(1, 10)
kmeans = KMeans(
    init="random",
    n_clusters=ranCluster,
    n_init=10,
    max_iter=300,
    random_state=42
)

plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()
