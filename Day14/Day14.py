
# Description

import os
import sys
from itertools import chain

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

def parse(str):
    initial, instructions = str.split('\n\n')
    instructions = instructions.split('\n')
    for i in range(len(instructions)):
        instructions[i] = tuple(instructions[i].split(' -> '))

    return initial, dict(instructions)

def do_insertions(input, instructions):
    gaps = ''
    for i in range(len(input) - 1):
        pair = input[i:i+2]
        if pair in instructions:
            gaps += instructions[pair]
        else:
            gaps += ' '
    
    gaps += ' '
    return (''.join(chain(*zip(input,gaps)))).replace(' ','')
    

def get_frequency(input):
    freq = {}
    for e in input:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1
    
    return freq

def commonality_difference(seed, instructions, iterations):
    pair_freq = dict(zip(instructions.keys(), [0]*len(instructions.keys())))
    elem_freq = dict(zip(instructions.values(), [0]*len(instructions.values())))
    

    # Seed the frequency tables
    for i in range(len(seed) - 1):
        pair_freq[seed[i:i+2]] += 1
    for e in seed:
        elem_freq[e] += 1
    # print("Starting Condition")
    # print(pair_freq)
    # print(elem_freq)
    # print()

    for i in range(iterations):
        insertions = dict(zip(instructions.keys(), [0]*len(instructions.keys())))
        for p,f in pair_freq.items():
            pair_freq[p] = 0
            e = instructions[p]
            left = p[0] + e
            right = e + p[1]
            insertions[left] += f
            insertions[right] += f
            elem_freq[e] += f
        # print("Insertions")
        # print(insertions)
        for p,f in insertions.items():
            pair_freq[p] += f
        # print("After ", i+1, " iterations:")
        # print(pair_freq)
        # print(elem_freq)
        # print()

    return max(elem_freq.values()) - min(elem_freq.values())
            

if __name__ == "__main__":
    start, instructions = parse(input_str)
    
    # Part 1
    string = start
    for _ in range(10):
        string = do_insertions(string, instructions)
    f = get_frequency(string)
    print(max(f.values()) - min(f.values()))
    

    # Part 2
    # Part 1 method does not work, the strings get too large
    print(commonality_difference(start, instructions, 40))