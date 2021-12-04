
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

def most_common_bits(inp):
    l = len(inp[0])
    tracker = [0]*len(inp[0])
    for b in inp:
        for i in range(len(b)):
            if b[i] == '0':
                tracker[i] -= 1
            else:
                tracker[i] += 1
    
    return list(map(lambda x: 1 if x > 0 else 0, tracker))

def oxygen_mask(inp):
    l = len(inp[0])
    tracker = [0]*len(inp[0])
    for b in inp:
        for i in range(len(b)):
            if b[i] == '0':
                tracker[i] -= 1
            else:
                tracker[i] += 1
    
    return list(map(lambda x: 1 if x >= 0 else 0, tracker))

def CO2_mask(inp):
    l = len(inp[0])
    tracker = [0]*len(inp[0])
    for b in inp:
        for i in range(len(b)):
            if b[i] == '0':
                tracker[i] -= 1
            else:
                tracker[i] += 1
    
    return list(map(lambda x: 0 if x >= 0 else 1, tracker))

def bits_to_int(l):
    c = 0
    for (i,b) in enumerate(l[::-1]):
        c += b * (2 ** i)

    return c

def filter_sample(values, pos, value):
    r = []
    for v in values:
        if int(v[pos]) == int(value):
            r.append(v)

    return r

if __name__ == "__main__":
    input = input_str.splitlines()
    input_test = test.splitlines()
    # Part 1
    t = bits_to_int(most_common_bits(input))
    s = (2**len(input[0])) - 1
    print(t * (s ^ t))

    # Part 2
    osample = input
    csample = input
    for i in range(len(input[0])):
        omask = oxygen_mask(osample)
        osample = list(filter(lambda x: int(x[i]) == int(omask[i]), osample))
        if len(osample) == 1:
            break
    
    for i in range(len(input[0])):
        cmask = CO2_mask(csample)
        csample = list(filter(lambda x: int(x[i]) == int(cmask[i]), csample))
        if len(csample) == 1:
            break

    print(int(osample[0],2) * int(csample[0],2))
