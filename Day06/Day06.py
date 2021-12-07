
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''3,4,3,1,2'''

def state_advance(state):
    zs = state[0]
    for i in range(1,9):
        state[i-1] = state[i]
    state[8] = zs
    state[6] += zs

def parse(str):
    d = dict(zip(range(9), [0]*9))
    for a in list(map(int, str.split(','))):
        d[a] += 1
    return d

if __name__ == "__main__":
    # Part 1
    initial_test = parse(test)
    initial = parse(input_str)
    for i in range(80):
        state_advance(initial)
    print(sum(initial.values()))

    # Part 2
    initial_test = parse(test)
    initial = parse(input_str)
    for i in range(256):
        state_advance(initial)
    print(sum(initial.values()))