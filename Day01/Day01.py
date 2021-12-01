# Day 01

# To do this, count the number of times a depth measurement increases from 
# the previous measurement. (There is no measurement before the first measurement.)

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string





if __name__ == "__main__":
    depths = list(map(int, input_str.splitlines()))
    # Part 1
    increases = [x < y for (x,y) in zip(depths, depths[1:])]
    print(sum(increases))

    # Part 2
    windows = [x+y+z for (x,y,z) in zip(depths, depths[1:], depths[2:])]
    w_increases = [x < y for (x,y) in zip(windows, windows[1:])]
    print(sum(w_increases))
    

