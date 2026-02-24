import random

class GM:
    def __init__(self, seed=None):
        self.seed = seed or 42
        random.seed(self.seed)
        self.methods = ["HackA", "HackB", "HackC"]
        self.nodes = ["Node1", "Node2", "Node3"]
        self.culprit = None
        self.solution = {}

    def generate_world(self):
        self.culprit = "C1"
        method = random.choice(self.methods)
        node = random.choice(self.nodes)
        self.solution = {"culprit": self.culprit, "method": method, "node": node}
        return self.solution

    def answer_query(self, agent_name, query):
        if agent_name == self.culprit:
            return f"You know: {self.solution}"
        else:
            key = random.choice(list(self.solution.keys()))
            return {key: self.solution[key]}
