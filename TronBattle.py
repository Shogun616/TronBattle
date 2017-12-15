import math
import sys

# Constants:
# Data structure: store the battlefield as a 2D array of size WIDTH x HEIGHT
# Set all cells to -1 to mark them as empty
def get_score(starts):
    graphs = {i: {} for i in range(other_player_x)}
    graphset = set(x for x in occupied)
    order = list(range(my_x, other_player_x)) + list(range(0, my_x))
    it = 1
    while True:
        full = True
        moves = {}
        for o in order:
            for x in starts[o]:
                for n in GRID[x]:
                    if n not in graphset or (n in moves and it == 1):
                        full = False
                        graphset.add(n)
                        moves[n] = o
        for k, v in moves.items():
            graphs[v][k] = it
        if full:
            break
        starts = [[k for k, v in moves.items() if v == i] for i in range(other_player_x)]
        it += 1
    num_my_tiles = len(graphs[my_x])
    num_enemy_tiles = sum([len(graphs[i]) for i in range(other_player_x) if i != my_x])
    enemies_dist = sum([sum(graphs[i].values()) for i in range(other_player_x) if i != my_x])
    return sum([num_my_tiles * 10000000, num_enemy_tiles * -100000, enemies_dist])

GRID = {}
WIDTH = 30
HEIGHT = 20
for i in range(WIDTH):
    for j in range(HEIGHT):
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
                          
# loop forever
occupied = {}
# n: total number of players (2 to 4).
# p: your player number (0 to 3).
while True:
    other_player_x, my_x = [int(i) for i in input().split()]
    curr_moves = []
    for i in range(other_player_x):
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        occupied[(x0, y0)] = i
        occupied[(x1, y1)] = i
        curr_moves.append((x1, y1))
    for i, cm in enumerate(curr_moves):
        if cm == (-1, -1):
            occupied = {k: v for k, v in occupied.items() if v != i}
    for p in range(other_player_x):
        x1, y1 = curr_moves[p]
        if p == my_x:
            me = (x1, y1)
            scores = []
            for grid in GRID[me]:
                if grid not in occupied:
                    player_starts = [[grid] for x in curr_moves.copy()]
                    player_starts[my_x] = [grid]
                    for i, cm in enumerate(curr_moves):
                        if cm == (-1, -1):
                            player_starts[i] = []
                    score = get_score(player_starts)
                    scores.append((score, grid))
    best_score_move = sorted(scores, key=lambda x: x[0], reverse=True)[0]
    
def movement():
    options = []
if (my_x + 1) < WIDTH and grid[my_x + 1][my_y] == -1:
    options.append("RIGHT")
if (my_x - 1) >= 0 and grid[my_x - 1][my_y] == -1:
    options.append("LEFT")
if (my_y + 1) < HEIGHT and grid[my_x][my_y + 1] == -1:
    options.append("DOWN")
if (my_y - 1) >= 0 and grid[my_x][my_y - 1] == -1:
    options.append("UP")
if len(options) == 0:
    print("SELF DESCTRUCT")
elif len(options) == 1:
    print(options[0])
else:   
    if (other_player_x + 1) < WIDTH and grid[other_player_x + 1][other_player_y] == -1:
        options.append("RIGHT")
    if (other_player_x - 1) >= 0 and grid[other_player_x - 1][other_player_y] == -1:
        options.append("LEFT")
    if (other_player_y + 1) < HEIGHT and grid[other_player_y][other_player_y + 1] == -1:
        options.append("DOWN")
    elif (other_player_y - 1) >= 0 and grid[other_player_x][other_player_y - 1] == -1:
        options.append("UP")
    else:
        print("RIGHT")
          # print("SELF DESTRUCT")

# Write out some debugging output to help us see what is going on:
print(movement(me, best_score_move[-1]))
print("Mitt nuvarande x position är {}".format(my_x), file=sys.stderr)
print("Mitt nurvarande y position är {}".format(my_y), file=sys.stderr)
print("Motståndarens nuvarande x position är {}".format(other_player_x), file=sys.stderr)
print("Motståndarens nuvarande y position är {}".format(other_player_y), file=sys.stderr)









