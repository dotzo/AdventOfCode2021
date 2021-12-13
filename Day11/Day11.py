
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

def parse_grid(str):
    str = str.splitlines()
    grid = {}
    for j in range(10):
        for i in range(10):
            grid[(i,j)] = int(str[j][i])
    return grid

def populate_adjacents():
    result = {}
    adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    for x,y in [(a,b) for a in range(10) for b in range(10)]:
        result[(x,y)] = []
        for i,j in adjacency:
            if 0 <= x + i < 10 and 0 <= y + j < 10:
                result[(x,y)].append((x+i,y+j))
    return result

ADJACENTS = populate_adjacents()    

def draw_grid(grid):
    for j in range(10):
        line = []
        for i in range(10):
            line.append(str(grid[(i,j)]))
        print(''.join(line))
    print()

def step(grid):
    # Increment and check flashes
    flashes = []
    for k,v in grid.items():
        grid[k] += 1
        if v == 9:
            flashes.append(k)
    
    # Propogate flashes
    flash_iter = flashes.copy()
    while flash_iter:
        n = flash_iter.pop()
        for i,j in ADJACENTS[n]:
            grid[(i,j)] += 1
            if grid[(i,j)] > 9 and (i,j) not in flashes:
                flash_iter.append((i,j))
                flashes.append((i,j))

    # Set flashed to 0
    for i,j in flashes:
        grid[(i,j)] = 0


    return len(flashes)
        



if __name__ == "__main__":
    input = parse_grid(input_str)
    # Part 1
    # print("Before steps:")
    # draw_grid(input)
    total_flashed = 0
    for n in range(100):
        #print(n+1," steps:")
        total_flashed += step(input)
        #draw_grid(input)
    print("Total flashes: ", total_flashed)

    # Part 2
    input = parse_grid(input_str)
    i = 0
    while step(input) < 100:
        i += 1
    print("All flashed on step: ", i+1)