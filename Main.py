import random
import time
import math

from rich.progress import Progress
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

from MaxList import MaxList
from Plan import Plan

########################################
#             Parameters               #
########################################

# player_names = ["Mäthy","Alex","Leo","Leopold","Maxi","Takeshi","Kilian","Marlene","Paul","Paula","Pascal","Pauline","Thilo"]
num_players = IntPrompt.ask("How many [blue]Players")

player_names = []
for i in range(num_players):
    player_names.append(Prompt.ask("Player [blue]" + str(i+1)))

num_tables = IntPrompt.ask("How many [blue]Tables", default=math.floor(num_players/4))

num_rounds = IntPrompt.ask("How many [blue]Rounds", default=4)

num_results = 1

loops = IntPrompt.ask("How man [blue]Iterations", default=1000000)

########################################
#               Setup                  #
########################################

candidates = MaxList(num_results)

console = Console()

########################################
#             Monte Carlo              #
########################################

with Progress() as progress:

    task = progress.add_task("[red]Leo's brain smokes...", total=loops)

    while not progress.finished:
        rounds = [[ [] for j in range(num_tables) ] for i in range(num_rounds)]

        for r in range(num_rounds):
            round = list(range(num_players))
            random.shuffle(round)
            for t in range(num_tables * 4):
                rounds[r][math.floor(t / 4)].insert(math.floor(t / 4), round[t])

        candidates.insert(Plan(rounds, num_players))

        progress.update(task, advance=1)

    progress.update(task, visible=False)

########################################
#                Output                #
########################################

best = candidates.best()

table = Table(title="Best Plan")

table.add_column("#", justify="center")
for t in range(num_tables):
    table.add_column("Table " + str(t+1), justify="center")

for i, r in enumerate(best.rounds):
    tableStrings = [""] * num_tables
    for t in range(num_tables):
        for p in r[t]:
            tableStrings[t] += player_names[p] + " "

    table.add_row(str(i+1), *tableStrings)

console.print(table)