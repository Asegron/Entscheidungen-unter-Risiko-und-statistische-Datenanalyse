import numpy as np

# Benutzereingaben für die Uebergangsmatrix, zb 0.5,0.5,0;0.25,0.5,0.25;0.25,0,0.75
matrixString = input("Geben Sie die Werte der Übergangsmatrix ein (getrennt mit Kommas und Semikolons):\n")
matrixListe = matrixString.split(';')
matrixWerte = []
for row in matrixListe:
    row_values = [float(val) for val in row.split(',')]
    matrixWerte.append(row_values)
uebergangsmatrix = np.array(matrixWerte)

print("Die Übergangsmatrix ist:\n", uebergangsmatrix)

# Benutzereingaben für die initiale Zustandsverteilung, zb 1,0,0
initialString = input("Geben Sie die initiale Zustandsverteilung ein (getrennt mit Kommas):\n")
initialeWerte = [float(val) for val in initialString .split(',')]
initialeVerteilung = np.array(initialeWerte)

# Print the initial distribution
print("Die initiale Zustandsverteilung ist:\n", initialeVerteilung)


# Funktion um die Wahrscheinlichkeiten auszurechnen
def berechneWahrscheinlichkeit(initialeVerteilung, uebergangsmatrix, n):
    aktuelleVerteilung = initialeVerteilung
    for i in range(n):
        new_distribution = []
        for j in range(len(initialeVerteilung)):
            neueWahrscheinlichkeit = 0
            for k in range(len(initialeVerteilung)):
                neueWahrscheinlichkeit += aktuelleVerteilung[k] * uebergangsmatrix[k][j]
            new_distribution.append(neueWahrscheinlichkeit)
        aktuelleVerteilung = new_distribution
    return aktuelleVerteilung

# Printe die Wahrscheinlichkeiten fuer n = 1, 2, 3, ..., 100, 200, 300, ...
for n in range(0, 301):
    if n in [1, 2, 3, 4, 10, 20, 30, 100, 200, 300]:
        aktuelleVerteilung = berechneWahrscheinlichkeit(initialeVerteilung, uebergangsmatrix, n)
        print(f"Zeitpunkt {n}: {aktuelleVerteilung}")