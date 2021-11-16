from Evaluation import minimalPlayerDiversity as eval_primary
from Evaluation import summedPlayerDiversity as eval_secondary

class Plan:
    rounds = None
    score_primary = 0
    score_secondary = 0
    num_players = 0

    def __init__(self, rounds, num_players):
        self.rounds = rounds
        self.num_players = num_players

    def evaluate(self):
        self.score_primary = eval_primary(self)
        self.score_secondary = eval_secondary(self)