
# Description

import os
import sys
from functools import reduce
import operator

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

def low_points(grid):
    cols = len(grid[0])
    rows = len(grid)
    lows = []
    
    for j in range(rows):
        for i in range(cols):
            target = grid[j][i]
            t_n = ('9' if j - 1 < 0 else grid[j-1][i]) > target
            t_s = ('9' if j + 1 >= rows else grid[j+1][i]) > target
            t_w = ('9' if i - 1 < 0 else grid[j][i-1]) > target
            t_e = ('9' if i + 1 >= cols else grid[j][i+1]) > target

            if t_n and t_s and t_w and t_e:
                lows.append((target, (i,j)))

    return lows


def get_basin_sizes(grid, lows):
    cols = len(grid[0])
    rows = len(grid)
    candidates = []
    for j in range(rows):
        for i in range(cols):
            if grid[j][i] != '9' and (i,j) not in lows:
                candidates.append((i,j))

    def test_adjacents(basin, p):
        x,y = p[0],p[1]
        #print("basin", basin)
        if (x-1,y) in candidates:
            candidates.remove((x-1,y))
            basin.append((x-1,y))
            test_adjacents(basin, (x-1,y))
        if (x+1,y) in candidates:
            candidates.remove((x+1,y))
            basin.append((x+1,y))
            test_adjacents(basin, (x+1,y))
        if (x,y-1) in candidates:
            candidates.remove((x,y-1))
            basin.append((x,y-1))
            test_adjacents(basin, (x,y-1))
        if (x,y+1) in candidates:
            candidates.remove((x,y+1))
            basin.append((x,y+1))
            test_adjacents(basin, (x,y+1))
        #print("fell through",x,y)
        return basin
    
    basins = []
    for i in range(len(lows)):
        a = [lows[i]]
        test_adjacents(a, lows[i])
        basins.append(a)

    return list(map(len,basins))
   
        

if __name__ == "__main__":
    input = input_str.splitlines()

    # Part 1
    #print(sum(map(lambda x: int(x) + 1, list(zip(*low_points(input)))[0])))

    # Part 2
    lows = list(list(zip(*low_points(input)))[1])
    bs = get_basin_sizes(input, lows)
    bs.sort()
    print(reduce(operator.mul, bs[-3:], 1))
