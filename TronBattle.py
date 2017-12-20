import sys

# Tron Battle, Mark's starter program
# Utterly naive algorithm that simply avoids the edge of
# the playing field as well as other players.
# Usually survives more than 2 seconds but barely.

def move_to_dir(old, new):
    """Converts using e.g. old position (1,1) and new position (2, 1) to a direction (RIGHT)"""
    if old[0] < new[0]:
        return "RIGHT"
    if old[1] < new[1]:
        return "DOWN"
    if old[0] > new[0]:
        return "LEFT"
    return "UP"

    options = []
    if "LEFT" in options:
        print("LEFT")
    elif "RIGHT" in options:
        print ("RIGHT")
    elif "DOWN" in options:
        print("DOWN")
    else:
        print("UP")

def get_score(starts):
    """
    Function for calculating the score given current starting positions for all bots
    """
    # create a nested dict called graph to store which bot (o) contains which
    # spot (n) at which iteration (it)
    graphs = {i: {} for i in range(sark)}
    # graphset just contains a copy that is being updated from the current `occupied` places
    # once no changes for any bot, indicates it stops
    graphset = set(x for x in occupied)
    # the order in which bots are playing this turn, e.g. if our bot is player 2: (2, 3, 1, 0)
    order = list(range(tron, sark)) + list(range(0, tron))
    it = 1
    # loop until no changes
    while True:
        # full gets falsified when any new move is possible by any bot in a round
        full = True
        # keeps track of who will end up owning the spots from this turn
        moves = {}
        for o in order:
            # on a single turn, for each bot, `starts` contains the possible starting positions
            # in case of starting round, logically there is only 1 possibility
            # so: for each possibility `x` of starting for bot `o`
            for x in starts[o]:
                # consider all the neighbouring tiles
                for n in GRID[x]:
                    # if n not visitable by other bots earlier
                    if n not in graphset or (n in moves and it == 1):
                        # make sure we will continue for at least 1 more round as we found new
                        full = False
                        # add to occupied for this `get_score`
                        graphset.add(n)
                        # register `neighbour` to belong to bot `o`
                        moves[n] = o
        # update the graph with who owns in this round
        for k, v in moves.items():
            graphs[v][k] = it
        if full:
            # break since no changes were in the last round (no new possible moves)
            break
        # update the new possible starting positions for each bot
        starts = [[k for k, v in moves.items() if v == i] for i in range(sark)]
        it += 1
    # number of tiles we are closest to (higher=better)
    num_my_tiles = len(graphs[tron])
    # number of tiles enemies are closest to (lower=better)
    num_enemy_tiles = sum([len(graphs[i]) for i in range(sark) if i != tron])
    # summed distance for reaching each tile for all enemies (higher=better)
    enemies_dist = sum([sum(graphs[i].values()) for i in range(sark) if i != tron])
    # simple weighting, importance: num_my_tiles > num_enemy_tiles > enemies_dist
    return sum([num_my_tiles * 10000000, num_enemy_tiles * -100000, enemies_dist])

# Data structure: store the battlefield as a 2D array of size WIDTH x HEIGHT for example 30 x 20
# Set all cells to -1 to mark them as empty
# GRID is a constant structure that gives the neighbouring tiles (e.g. 4 grids for a centered square)
# GRID[(2,2)] would give [(1,2), (2,1), (3, 2), (2, 3)]
GRID = {}
for i in range(30):
    for j in range(20):
        grid = []
        if i < 29:
            grid.append((i + 1, j))
        if i > 0:
            grid.append((i - 1, j))
        if j < 19:
            grid.append((i, j + 1))
        if j > 0:
            grid.append((i, j - 1))
        GRID[(i, j)] = grid

# `occupied` contains all the previously visited spots by bots
occupied = {}
# loop forever
while True:
    # each turn we receive the number of players (sark) and our id
    # (tron) from the codingame engine
    sark, tron = [int(i) for i in input().split()]
    # curr_moves will consist of the previously played move for each bot
    curr_moves = []
    for i in range(sark):
        # for each player, obtain the old and new coordinates
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        occupied[(x0, y0)] = i
        occupied[(x1, y1)] = i
        curr_moves.append((x1, y1))
    for i, cm in enumerate(curr_moves):
        # (-1, -1) indicates bot has deen destroyed
        if cm == (-1, -1):
            occupied = {k: v for k, v in occupied.items() if v != i}
         # Read in data for where all players are right now:
    for p in range(sark):
        x1, y1 = curr_moves[p]
        # currently only calculate from "our" perspective
        if p == tron:
            # our current location
            me = (x1, y1) # show the position of my light cycle
            scores = []
        else:
            mcp = (x1, y1) # show the position of the opponent(s) light cycle
            scores = []
            # loop over our grid tiles
            for grid in GRID[me]:
                # if a grid is not in occupied, it means it is still availbable and
                # should be considered a starting position to calculate from how good of a
                # move it is
                if grid not in occupied:
                    # copy to prevent overwriting
                    player_starts = [[x] for x in curr_moves.copy()]
                    # fix our starting position to a candidate move
                    player_starts[tron] = [grid]
                    # each player that has deen destroyed does not play (since no starting moves)
                    for i, cm in enumerate(curr_moves):
                        if cm == (-1, -1):
                            player_starts[i] = []
                    # gather score for board given starting positions
                    score = get_score(player_starts)
                    scores.append((score, grid))
    # return the best move given the posible candidate moves
    best_score_move = sorted(scores, key=lambda x: x[0], reverse=True)[0]
    # print the direction we want to go to
    print(move_to_dir(me, best_score_move[-1]))
    # Write out some debugging output to help us see what is going on:
    print("Mitt nuvarande x, y position är {}".format(me), file=sys.stderr)
    print("Motståndarens nuvarande x, y position är {}".format(mcp), file=sys.stderr)
