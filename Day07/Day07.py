
# Description

import os
import sys
from math import inf

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''16,1,2,0,4,2,7,1,2,14'''

def total_fuel_linear(ships):
    final = inf
    med = 0
    for i in range(min(ships), max(ships)+1):
        a = sum(map(lambda x: abs(i - x), ships))
        if a < final:
            final = a
            med = i
    return final, med

def total_fuel_triangular(ships):
    final = inf
    med = 0
    for i in range(min(ships), max(ships)+1):
        a = sum(map(lambda x: (abs(i - x) * (abs(i - x) + 1)) // 2, ships))
        if a < final:
            final = a
            med = i
    return final, med

if __name__ == "__main__":
    parse = list(map(int, input_str.split(',')))
    
    # Part 1
    print(total_fuel_linear(parse))

    # Part 2
    print(total_fuel_triangular(parse))