class Agent:
    def __init__(self, name):
        self.name = name
        self.beliefs = {"C1": 0.25, "C2": 0.25, "C3": 0.25, "C4": 0.25}  # probabilità iniziale

    def update_belief(self, info):
        # aggiornamento semplice: incrementa la probabilità del colpevole indicato
        for culprit in self.beliefs:
            if culprit in info:
                self.beliefs[culprit] += 0.25
            else:
                self.beliefs[culprit] -= 0.08
        # normalizza
        total = sum(self.beliefs.values())
        for k in self.beliefs:
            self.beliefs[k] /= total

    def ask_question(self):
        return "Which method did the culprit use?"

class Culprit(Agent):
    def ask_question(self):
        return None  # il colpevole non fa domande, solo risponde
