from rich.table import Table

from console import console

from Evaluation import maximalPlayerDiversity

from Plan import Plan

from rich import print, box
from rich.console import group
from rich.panel import Panel

import random
import time
import math

def generate_table(plan,player_names):
    num_tables = len(plan.rounds[0])
    table = Table()

    table.add_column("#", justify="center")

    for t in range(num_tables):
        table.add_column("Table " + str(t+1), justify="center")

    for i, r in enumerate(plan.rounds):
        tableStrings = [""] * num_tables
        for t in range(num_tables):
            for p in r[t]:
                tableStrings[t] += player_names[p] + " "
            tableStrings[t].strip()

        table.add_row(str(i+1), *tableStrings)
    return table

def outputTable(plan,player_names):
    table = generate_table(plan,player_names)
    console.print(table)
    console.print("\nmin: {} \t max: {} \t avg: {} ".format(plan.score_primary, maximalPlayerDiversity(plan), plan.score_secondary/len(player_names)))
    return

def generate_plan(num_tables,num_rounds,num_players):
    rounds = [[ [] for j in range(num_tables) ] for i in range(num_rounds)]
    for r in range(num_rounds):
        round = list(range(num_players))
        random.shuffle(round)
        for t in range(num_tables * 4):
            rounds[r][math.floor(t / 4)].insert(math.floor(t / 4), round[t])
    p = Plan(rounds, num_players)
    p.evaluate()
    return p

@group()
def get_panels(plan,player_names,prozent):
    yield Panel(generate_table(plan,player_names),box=box.ASCII,title="Momentan bester Spielplan")
    yield Panel("min: [bright_cyan]{}[/bright_cyan]  max: [bright_cyan]{}[/bright_cyan] avg: [bright_cyan]{:.3f}[/bright_cyan] ".format(plan.score_primary, maximalPlayerDiversity(plan), plan.score_secondary/len(player_names)),box=box.ASCII,title="Evaluation")
    yield Panel(str("[green]*[/green]"*int(100*prozent)+"[red]*[/red]"*(99-int(100*prozent)))+ " {0:.0f}% der Berechnung abgeschlossen".format(prozent*100),box=box.ASCII,title="Progress")
