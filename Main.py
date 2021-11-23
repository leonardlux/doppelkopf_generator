#!/usr/bin/env python

import random
import math

from console import console

from rich.prompt import Prompt, IntPrompt, Confirm
from rich.live import Live

from MaxList import MaxList
from Plan import Plan

from functions import outputTable, generate_plan, generate_table, get_panels


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
            print("Name schon vergeben "+ ":confused:")
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

    loops = IntPrompt.ask("How man [blue]Iterations", default=100000)

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

refreshs = 1000 #How often the console gets updated 

########################################
#             Monte Carlo              #
########################################

last_i = 0
try:
    with Live(get_panels((generate_plan(num_tables,num_rounds,num_players)),player_names,last_i), refresh_per_second=4000) as live:
        for i in range(loops):
            
            candidates.insert(generate_plan(num_tables,num_rounds,num_players))

            if int(i/loops*refreshs) > last_i:
                last_i = int(i/loops*refreshs)
                live.update(get_panels(candidates.best(), player_names,i/loops))
except KeyboardInterrupt:
    pass

########################################
#                Output                #
########################################

outputTable(candidates.best(),player_names)