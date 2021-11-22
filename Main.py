#!/usr/bin/env python

import random
import time
import math

from console import console

from rich.progress import Progress
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm

from MaxList import MaxList
from Plan import Plan
from Evaluation import maximalPlayerDiversity


console.clear()

player_emojis = [":smile:", ":face_with_tongue:", ":prince:", ":drooling_face:", ":kissing_heart:", ":joy:", ":innocent:", ":hugging_face:", ":grin:", ":grinning_face:", ":thinking_face:", ":nerd_face:", ":stuck_out_tongue:"]

########################################
#             Parameters               #
########################################

while True:
    player_names = ["Mäthy","Alex","Leo","Leopold","Maxi","Takeshi","Kilian","Marlene","Paul","Paula","Pascal","Pauline","Thilo"]
    num_players = len(player_names)

    num_players = IntPrompt.ask("How many [blue]Players")
    player_names = []

    i=0
    while i < num_players:
        player_name = Prompt.ask("Player " + str(i+1) + " " + random.choice(player_emojis))
        if player_name in player_names:
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
            rprint("Name schon vergeben "+ ":confused:")
        else:
            player_names.append(player_name)
            i+=1
    if ("Leo" in player_names):
        player_names.remove("Leo")
        player_names.append(":dolphin:")
    
    if ("leo" in player_names):
        player_names.remove("leo")
        player_names.append(":dolphin:")

    num_tables = IntPrompt.ask("How many [blue]Tables", default=math.floor(num_players/4))

    num_rounds = IntPrompt.ask("How many [blue]Rounds", default=4)

    num_results = 1

    loops = IntPrompt.ask("How man [blue]Iterations", default=1000000)

    if Confirm.ask("Start the Calculation?", default="y"):
        console.clear()
        break
    else:
        console.clear()
        continue

########################################
#               Setup                  #
########################################

candidates = MaxList(num_results)

########################################
#             Monte Carlo              #
########################################

try:
    with Progress() as progress:

        task = progress.add_task("[red]Leo's[/red] brain smokes :gear: ", total=loops)

        while not progress.finished:
            rounds = [[ [] for j in range(num_tables) ] for i in range(num_rounds)]

            for r in range(num_rounds):
                round = list(range(num_players))
                random.shuffle(round)
                for t in range(num_tables * 4):
                    rounds[r][math.floor(t / 4)].insert(math.floor(t / 4), round[t])
            p = Plan(rounds, num_players)
            p.evaluate()
            candidates.insert(p)

            progress.update(task, advance=1)

        progress.update(task, visible=False)
except KeyboardInterrupt:
    pass

########################################
#                Output                #
########################################

best = candidates.best()

table = Table()

table.add_column("#", justify="center")
for t in range(num_tables):
    table.add_column("Table " + str(t+1), justify="center")

for i, r in enumerate(best.rounds):
    tableStrings = [""] * num_tables
    for t in range(num_tables):
        for p in r[t]:
            tableStrings[t] += player_names[p] + " "
        tableStrings[t].strip()

    table.add_row(str(i+1), *tableStrings)

console.print(table)
console.print("\nmin: {} \t max: {} \t avg: {} ".format(best.score_primary, maximalPlayerDiversity(best), best.score_secondary/num_players))