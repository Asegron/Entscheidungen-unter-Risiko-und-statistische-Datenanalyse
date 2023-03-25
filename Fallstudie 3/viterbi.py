import numpy as np

with open('wuerfel.txt', 'r') as file:
    text = file.read()
    array = text.split()
    wurfliste = [int(char) for char in list(array[0])]
    zustaende = [1, 2, 3, 4, 5, 6]
    """
    :param obs: eine Liste von Beobachtungen
    :param A: Übergangsmatrix
    :param B: Emissionsmatrix
    :param pi: Anfangsverteilung
    :return: Die wahrscheinlichste Zustandsfolge und die Wahrscheinlichkeit dieser Folge
    """

    anfangsmatrix = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]])

    uebergangsmatrix = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667], ])

    # Definiere die Emissionswahrscheinlichkeiten
    emissionsmatrix = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667], ])

    # O: Beobachtungssequenz
    # S: Zustände
    # A: Zustandsübergangswahrscheinlichkeiten
    # B: Beobachtungswahrscheinlichkeiten

    T = len(wurfliste)  # Länge der Beobachtungssequenz
    N = len(zustaende)  # Anzahl der Zustände

    # Initialisierung
    delta = np.zeros((T, N))
    psi = np.zeros((T, N), dtype=int)
    delta[0] = emissionsmatrix[:, wurfliste[0]] * 1  # 1 ist das neutrale Element der Multiplikation

    # Rekursion
    for t in range(1, T):
        for j in range(N):
            prob = delta[t - 1] * uebergangsmatrix[:, j] * emissionsmatrix[j, wurfliste[t]]
            delta[t, j] = np.max(prob)
            psi[t, j] = np.argmax(prob)

    # Traceback
    path = np.zeros(T, dtype=int)
    path[T - 1] = np.argmax(delta[T - 1])
    for t in range(T - 2, -1, -1):
        path[t] = psi[t + 1, path[t + 1]]


print(path)
print(prob)