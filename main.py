import json
from gm import GM
from agents import Agent, Culprit

# Inizializza GM
gm = GM()
solution = gm.generate_world()

# Crea agenti
culprit = Culprit("C1")
investigators = [Agent("C2"), Agent("C3"), Agent("C4")]

# Log partita
log = []

# Loop 6 round
for round_num in range(1, 7):
    round_entry = {"round": round_num, "queries": [], "answers": []}
    
    # Ogni investigatore fa domanda
    for inv in investigators:
        q = inv.ask_question()
        a = gm.answer_query(inv.name, q)
        inv.update_belief(a)
        round_entry["queries"].append({"agent": inv.name, "question": q})
        round_entry["answers"].append({"agent": "GM", "answer": a})
    
    # Log beliefs
    beliefs_snapshot = {inv.name: inv.beliefs.copy() for inv in investigators}
    round_entry["beliefs"] = beliefs_snapshot
    log.append(round_entry)

# Salva log in JSON
with open("logs/first_match.json", "w") as f:
    json.dump(log, f, indent=4)

print("Partita completata! Log salvato in logs/first_match.json")
