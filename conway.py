# Conway's game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    time.sleep(1)

    # for x in range(WIDTH):
    #     for y in range(HEIGHT):
