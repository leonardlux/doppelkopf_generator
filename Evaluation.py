# fewest number of other players by one player
def minimalPlayerDiversity(plan):
    min = 10000

    for player in range(plan.num_players):
        n = NumberOfDifferentPlayers(plan, player)
        if n < min:
            min = n

    return min

# summed up number of different players by each player
def summedPlayerDiversity(plan):
    acu = 0

    for player in range(plan.num_players):
        acu += NumberOfDifferentPlayers(plan, player)

    return acu

def NumberOfDifferentPlayers(plan, player):
    notPlayed = range(plan.num_players)

    for round in plan.rounds:
        for table in round:
            if player in table:
                for p in table:
                    notPlayed.remove(p)
                break

    return plan.num_players - len(notPlayed)