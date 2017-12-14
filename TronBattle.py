import math
import sys

# Constants:
WIDTH = 30
HEIGHT = 20

# Data structure: store the battlefield as a 2D array of size WIDTH x HEIGHT
# Set all cells to -1 to mark them as empty
grid = {}
for i in range(WIDTH):
   x = []
   for j in range(HEIGHT):
       if i < 29:
           grid.append((i + 1, j))
       if i > 0:
           grid.append((i - 1, j))
       if j < 19:
           grid.append((i, j + 1))
       if j > 0:
           grid.append((i, j - 1))
   grid[(i, j)] = grid

# loop forever
while True:
   # n: total number of players (2 to 4).
   # p: your player number (0 to 3).
   n, p = [int(i) for i in input().split()]

   my_x = -1  # X position of my light cycle
   my_y = -1  # Y position of my light cycle

   # Read in data for where all players are right now:
   for i in range(n):
       x0, y0, x1, y1 = [int(j) for j in input().split()]
       grid[x1][y1] = i
       if i == p:
           my_x = x1
           my_y = y1
       else:
           other_player_x = x1
           other_player_y = y1
      

   # Write out some debugging output to help us see what is going on:
   print("Mitt nuvarande x position är {}".format(my_x), file=sys.stderr)
   print("Mitt nurvarande y position är {}".format(my_y), file=sys.stderr)
   print("Motståndarens nuvarande x position är {}".format(other_player_x), file=sys.stderr)
   print("Motståndarens nuvarande y position är {}".format(other_player_y), file=sys.stderr)

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
 
       












