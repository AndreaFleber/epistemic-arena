import random

class Agent:
    def __init__(self, name):
        self.name = name
        self.beliefs = {"C1": 0.25, "C2": 0.25, "C3": 0.25, "C4": 0.25}

    def ask_question(self):
        return "Which method did the culprit use?"

    def update_belief(self, info):
        for culprit in self.beliefs:
            if culprit in info.values():
                self.beliefs[culprit] += 0.5
            else:
                self.beliefs[culprit] *= 0.75

        total = sum(self.beliefs.values())
        for k in self.beliefs:
            self.beliefs[k] /= total

class Culprit(Agent):
    pass
