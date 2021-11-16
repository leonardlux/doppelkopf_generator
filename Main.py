import random
import time
import math

from MaxList import MaxList
from Plan import Plan

########################################

# Parameters

player_names = ["Mäthy","Alex","Leo","Leopold","Maxi","Takeshi","Kilian","Marlene","Paul","Paula","Pascal","Pauline","Thilo"]

global num_players
num_players = len(player_names)

num_tables = 3

num_rounds = 4

num_results = 5
candidates = MaxList(num_results)

seed = int(random.random()*1000000)
random.seed(seed)

n = 100

# Monte Carlo

for k in range(n):
    rounds = [[ [] for j in range(num_tables) ] for i in range(num_rounds)]

    for r in range(num_rounds):
        round = list(range(num_players))
        random.shuffle(round)
        for t in range(num_tables * 4):
            rounds[r][math.floor(t / 4)].insert(math.floor(t / 4), round[t])

    candidates.insert(Plan(rounds, num_players))

for c in candidates.list:
    print(c.rounds)