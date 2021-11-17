def NumberOfDifferentPlayers(plan, player):
    playedAgainst = []

    for round in plan.rounds:
        for table in round:
            if player in table:
                for p in table:
                    if not (p in playedAgainst):
                        playedAgainst.append(p)
                break

    return len(playedAgainst) - 1

# fewest number of other players by one player
def minimalPlayerDiversity(plan):
    min = 10000

    for player in range(plan.num_players):
        n = NumberOfDifferentPlayers(plan, player)
        if n < min:
            min = n

    return min

def maximalPlayerDiversity(plan):
    max = 0

    for player in range(plan.num_players):
        n = NumberOfDifferentPlayers(plan, player)
        if n > max:
            max = n

    return max

# summed up number of different players by each player
def summedPlayerDiversity(plan):
    acu = 0

    for player in range(plan.num_players):
        acu += NumberOfDifferentPlayers(plan, player)

    return acu