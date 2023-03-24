import numpy as np

with open('wuerfel.txt', 'r') as file:
    text = file.read()
    array = text.split()
    wurfliste = [int(char) for char in list(array[0])]
    zustaende = [1, 2, 3, 4, 5, 6]

    # Definiere die Anfangswahrscheinlichkeiten
    anfangswahrscheinlichkeiten = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]])

    # Definiere die Übergangswahrscheinlichkeiten
    uebergangswahrscheinlichkeiten = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667], ])

    # Definiere die Emissionswahrscheinlichkeiten
    emissionswahrscheinlichkeiten = np.array([
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667],
        [0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667], ])

    """
    Return the MAP estimate of state trajectory of Hidden Markov Model.

    Parameters
    ----------
    wurfliste : array (T,)
        Observation state sequence. int dtype.
    uebergangswahrscheinlichkeiten : array (K, K)
        State transition matrix. See HiddenMarkovModel.state_transition  for
        details.
    emissionswahrscheinlichkeiten : array (K, M)
        Emission matrix. See HiddenMarkovModel.emission for details.
    anfangswahrscheinlichkeiten: optional, (K,)
        Initial state probabilities: Pi[i] is the probability x[0] == i. If
        None, uniform initial distribution is assumed (Pi[:] == 1/K).

    Returns
    -------
    x : array (T,)
        Maximum a posteriori probability estimate of hidden state trajectory,
        conditioned on observation sequence y under the model parameters A, B,
        Pi.
    T1: array (K, T)
        the probability of the most likely path so far
    T2: array (K, T)
        the x_j-1 of the most likely path so far
    """

    # Cardinality of the state space
    K = uebergangswahrscheinlichkeiten.shape[0]
    # Initialize the priors with default (uniform dist) if not given by caller
    anfangswahrscheinlichkeiten = anfangswahrscheinlichkeiten if anfangswahrscheinlichkeiten is not None else np.full(K, 1 / K)
    T = len(wurfliste)
    T1 = np.empty((K, T), 'd')
    T2 = np.empty((K, T), 'B')

    # Initialize the tracking tables from first observation
    T1[:, 0] = anfangswahrscheinlichkeiten * emissionswahrscheinlichkeiten[:, wurfliste[0]]
    T2[:, 0] = 0

    # Iterate through the observations updating the tracking tables
    for i in range(1, T):
        T1[:, i] = np.max(T1[:, i - 1] * uebergangswahrscheinlichkeiten.T * emissionswahrscheinlichkeiten[np.newaxis, :, wurfliste[i]].T, 1)
        T2[:, i] = np.argmax(T1[:, i - 1] * uebergangswahrscheinlichkeiten.T, 1)

    # Build the output, optimal model trajectory
    x = np.empty(T, 'B')
    x[-1] = np.argmax(T1[:, T - 1])
    for i in reversed(range(1, T)):
        x[i - 1] = T2[x[i], i]

print(wurfliste)
print(x)
print(T1)
print(T2)