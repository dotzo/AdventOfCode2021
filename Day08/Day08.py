
# Description

import os
import sys
from itertools import chain
from types import CodeType

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string 

test = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'''

def parse_line(l):
    return tuple(a.split(' ') for a in l.split(' | '))

def str_sub(a,b):
    s = a
    for c in b:
        s = s.replace(c,'')
    return s

def decode(wires):
    sixes = []
    fives = []
    for g in wires:
        if len(g) == 2:
            one = g
        elif len(g) == 4:
            four = g
        elif len(g) == 3:
            seven = g
        elif len(g) == 7:
            eight = g
        elif len(g) == 6:
            sixes.append(g)
        else:
            fives.append(g)

    # Uniquely determine the top segment by 7 - 1
    seg_a = str_sub(seven, one)

    # Use the 6 segment numbers (0, 6, 9) to get the 'd', 'c', and 'e' segments
    missing_sixes = ''.join(map(lambda x: str_sub(eight, x), sixes.copy()))
    # Subtract 4 from the candidates, leaving only 'e' segment
    seg_e = str_sub(missing_sixes, four)
    # 'd' and 'c' segment candidates
    missing_sixes = str_sub(missing_sixes, seg_e)
    # Uniquely determine 'd' by subtracting 1
    seg_d = str_sub(missing_sixes, one)
    # Only one left is 'c'
    seg_c = str_sub(missing_sixes, seg_d)
    # one is just 'f' and 'c' segments, subtract 'c'
    seg_f = str_sub(one, seg_c)

    # Has 'a', 'c', 'd', 'e', 'f'
    seg_b = str_sub(four, seg_c + seg_d + seg_f)
    seg_g = str_sub(eight, seg_a + seg_b + seg_c + seg_d + seg_e + seg_f)

    return {seg_a: 'a', seg_b: 'b', seg_c: 'c', seg_d: 'd', seg_e: 'e', seg_f: 'f', seg_g: 'g'}

def build_digit(code, str):
    seg_to_num = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 
        'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
    
    d = sorted(list(map(lambda x: code[x], str)))
    d = ''.join(d)

    return seg_to_num[d]

def get_digits(t):
    cypher = decode(t[0])
    n = 0
    for (i,d) in enumerate(map(lambda x: build_digit(cypher, x), t[1])):
        n += d * pow(10, 3 - i)
    return n

if __name__ == "__main__":
    input = list(map(parse_line, input_str.splitlines()))
    testi = list(map(parse_line, test.splitlines()))
    # Part 1
    print(len(list(filter(lambda x: len(x) in (2, 4, 3, 7),chain(*list(zip(*input))[1])))))

    # Part 2
    values = map(get_digits, input)
    print(sum(values))