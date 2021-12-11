
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

GRAMMER = {'(': ')',
    '{': '}',
    '[': ']',
    '<': '>'}



def syntax_check(line):
    stack = []
    opens = GRAMMER.keys()
    closers = GRAMMER.values()
    SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for c in line:
        if c in opens:
            stack.append(c)
        elif c in closers:
            last = stack.pop()
            if c != GRAMMER[last]:
                return (stack, SCORE[c])
    
    return (stack, -1)

def score_part_2(s):
    closing_stack = reversed(list(map(lambda x: GRAMMER[x], s)))
    points = 0
    SCORE = {')': 1, ']': 2, '}': 3, '>': 4}
    for c in closing_stack:
        points *= 5
        points += SCORE[c]
    return points

if __name__ == "__main__":
    input = input_str.splitlines()
    # Part 1
    print(sum(list(zip(*filter(lambda x: x[1] != -1, map(syntax_check, input))))[1]))

    # Part 2
    a = list(map(score_part_2, list(list(zip(*filter(lambda x: x[1] == -1, map(syntax_check, input))))[0])))
    a.sort()
    print(a[len(a)//2])
