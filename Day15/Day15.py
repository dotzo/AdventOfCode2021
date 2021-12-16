
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

def parse(inp):
    s = inp.splitlines()
    for i in range(len(s)):
        s[i] = list(map(int, s[i]))
    return s

def get_walk_risk(grid, walk):
    risk = 0
    i, j = 0, 0
    # 1 goes right, 0 goes down
    for b in walk:
        if b == '1':
            i += 1
        else:
            j += 1
        risk += grid[j][i]

    return risk

def snoob(x):
    next = 0
    if(x):
        rightOne = x & -(x)
        nextHigherOneBit = x + int(rightOne)
        rightOnesPattern = x ^ int(nextHigherOneBit)
        rightOnesPattern = (int(rightOnesPattern) /
                            int(rightOne))
        rightOnesPattern = int(rightOnesPattern) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next
            
def lowest_risk(grid):
    # Seed the risk with a value equal to the lowest possible
    rights = len(grid[0]) - 1 # number of 1s
    downs = len(grid) - 1 # number of 0s
    total_bits = downs + rights
    walk = '0'*downs + '1'*rights # smallest number formed by binary of downs and walks
    risk = get_walk_risk(grid, walk)

    i = 0
    while walk != '1'*rights + '0'*downs:
        i += 1
        next = bin(snoob(int(walk,2)))[2:]
        walk = '0'*(total_bits - len(next)) + next
        #print(walk)
        risk = min(risk, get_walk_risk(grid, walk))
        if i % 10000 == 0:
            print(i)

    # edge case all rights, then all downs
    risk = min(risk, get_walk_risk(grid, '1'*rights + '0'*downs))

    return risk

if __name__ == "__main__":
    input = parse(input_str) 
    # Part 1
    #print(input)
    print(get_walk_risk(input, '0'*99 + '1'*99))
    print(bin(snoob(int('0'*99 + '1'*99, 2)))[2:])
    print(bin(950737950171172051122527404032))