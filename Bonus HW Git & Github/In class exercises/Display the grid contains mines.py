import random

mines = []
while len(mines) < 10 :
    mine = random.randint(0,80)
    if mine not in mines :
        mines.append(mine)

print(mines)

grid = []
i = 0
while i < 81 :
    if i in mines :
        grid.append("X")
    else :
        grid.append(".")

    i += 1
print(grid)

grid_str = ""
i = 0
while i < 81 :
    row = grid[i:i+9]
    grid_str += " ".join(row) + "\n"
    i += 9
print(grid_str)