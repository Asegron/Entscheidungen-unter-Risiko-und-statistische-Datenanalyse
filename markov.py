import numpy as np

# Benutzereingaben für die Übergangsmatrix, zb 0.5,0.5,0;0.25,0.5,0.25;0.25,0,0.75
matrixString = input("Geben Sie die Werte der Übergangsmatrix ein (getrennt mit Kommas und Semikolons):\n")
matrixListe = matrixString.split(';')
matrixWerte = []
for row in matrixListe:
    row_values = [float(val) for val in row.split(',')]
    matrixWerte.append(row_values)
transition_matrix = np.array(matrixWerte)

print("Die Übergangsmatrix ist:\n", transition_matrix)

# Benutzereingaben für die initiale Zustandsverteilung, zb 1,0,0
initialString = input("Geben Sie die initiale Zustandsverteilung ein (getrennt mit Kommas):\n")
initialeWerte = [float(val) for val in initialString .split(',')]
initialeVerteilung = np.array(initialeWerte)

print("Die initiale Zustandsverteilung ist:\n", initialeVerteilung)

# Funktion um die Wahrscheinlichkeiten auszurechnen
def wahrscheinlichkeit(state, n):
    endgueltigeVerteilung = np.dot(state, np.linalg.matrix_power(transition_matrix, n))
    return endgueltigeVerteilung

# Printe die Wahrscheinlichkeiten fuer n = 1, 2, 3, ..., 100, 200, 300, ...
for n in range(0, 301):
    if n in [1, 2, 3, 4, 10, 20, 30, 100, 200, 300]:
        print("Wahrscheinlichkeiten für n = {}: {}".format(n, wahrscheinlichkeit(initialeVerteilung, n)))
