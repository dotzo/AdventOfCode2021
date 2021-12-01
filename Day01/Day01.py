# Day 01

# To do this, count the number of times a depth measurement increases from 
# the previous measurement. (There is no measurement before the first measurement.)

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


def increases(a,b):
    return sum(map(lambda x,y: x < y, a, b))


if __name__ == "__main__":
    depths = list(map(int, input_str.splitlines()))
    # Part 1
    print(increases(depths,depths[1:]))

    # Part 2
    windows = list(map(lambda x,y,z: x+y+z, depths, depths[1:], depths[2:]))
    print(increases(windows,windows[1:]))
    

