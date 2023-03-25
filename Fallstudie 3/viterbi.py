class Viterbi:
    #initialisiert die Klasse mit den Parametern.
    def __init__(self, observations, states, start_p, trans_p, emit_p):
        self.observations = observations
        self.states = states
        self.start_p = start_p
        self.trans_p = trans_p
        self.emit_p = emit_p

    #Viterbi-Algorithmus
    def viterbiAlgorithmus(self):
        V = [{}]
        for st in self.states:
            V[0][st] = {"prob": self.start_p[st] * self.emit_p[st][self.observations[0]], "prev": None}

         # iteriert durch die Beobachtungen
        for t in range(1, len(self.observations)):
            V.append({})
            for st in self.states:
                max_tr_prob = V[t - 1][self.states[0]]["prob"] * self.trans_p[self.states[0]][st] #Multipliziert den aktuellen Zustand mit der Uebergangsmatrix
                prev_st_selected = self.states[0]
                for prev_st in self.states[1:]:
                    tr_prob = V[t - 1][prev_st]["prob"] * self.trans_p[prev_st][st] #Multipliziert den vorherigen Zustand mit der Uebergangsmatrix
                    if tr_prob > max_tr_prob:
                        max_tr_prob = tr_prob
                        prev_st_selected = prev_st

                max_prob = max_tr_prob * self.emit_p[st][self.observations[t]]
                V[t][st] = {"prob": max_prob, "prev": prev_st_selected}
        for line in self.dptable(V):
            print(line)

        opt = []
        max_prob = 0.0
        best_st = None

        for st, data in V[-1].items():
            if data["prob"] > max_prob:
                max_prob = data["prob"]
                best_st = st
        opt.append(best_st)
        previous = best_st

        for t in range(len(V) - 2, -1, -1):
            opt.insert(0, V[t + 1][previous]["prev"])
            previous = V[t + 1][previous]["prev"]

        print ("Die Schritte der Zustaende sind " + " ".join(opt) + " mit der hoechsten Wahrscheinlichkeit von %s" % max_prob)

    #Erstellt eine DP-Tabelle für die Pfade als visuelle Dastellung
    def dptable(self, V):
        yield " ".join(str(i).rjust(7) for i in range(len(V)))
        for state in V[0]:
            yield f"{state:.7s}: " + " ".join(f"{v[state]['prob']:.{len(str(v[state]['prob']))}}".rjust(7) for v in V)

with open('wuerfel.txt', 'r') as file:
    text = file.read()
    array = text.split()
    num_str = array[0]
    observations = [int(char) for char in list(array[0])]
    #observations = [1,1,1]
    states = ["1", "2", "3", "4", "5", "6"]

    eingabe = input("Geben Sie 1 für fair oder 2 für gezinkt ein: ")
    zahl = int(eingabe)

    if zahl == 1:
        start_p = {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667}

        trans_p = {
            "1": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667},
            "2": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667},
            "3": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667},
            "4": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667},
            "5": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667},
            "6": {"1": 0.1667, "2": 0.1667, "3": 0.1667, "4": 0.1667, "5": 0.1667, "6": 0.1667}
        }

        emit_p = {
            "1": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667},
            "2": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667},
            "3": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667},
            "4": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667},
            "5": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667},
            "6": {1: 0.1667, 2: 0.1667, 3: 0.1667, 4: 0.1667, 5: 0.1667, 6: 0.1667}
        }
    if zahl == 2:
        start_p = {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1}

    trans_p = {
        "1": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
        "2": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
        "3": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
        "4": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
        "5": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
        "6": {"1": 0.5, "2": 0.1, "3": 0.1, "4": 0.1, "5": 0.1, "6": 0.1},
    }

    emit_p = {
        "1": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
        "2": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
        "3": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
        "4": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
        "5": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
        "6": {1: 0.5, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1},
    }

viterbi = Viterbi(observations, states, start_p, trans_p, emit_p)
viterbi.viterbiAlgorithmus()
