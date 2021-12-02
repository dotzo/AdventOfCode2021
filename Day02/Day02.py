
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


def move(instruction, current_pos):
    h,d = current_pos
    direction,amount = instruction.split(" ")
    amount = int(amount)
    if direction == "forward":
        h += amount
    elif direction == "up":
        d -= amount
    elif direction == "down": 
        d += amount
    
    return (h,d)

def aim(instruction, current_pos):
    h,d,a = current_pos
    direction,amount = instruction.split(" ")
    amount = int(amount)
    if direction == "forward":
        h += amount
        d += a*amount
    elif direction == "up":
        a -= amount
    elif direction == "down": 
        a += amount
    
    return (h,d,a)


if __name__ == "__main__":
    instructions = input_str.splitlines()
    
    # Part 1
    h,d = (0,0)
    for i in instructions:
        h,d = move(i,(h,d))
    print(str(h*d))

    # Part 2
    h,d,a = (0,0,0)
    for i in instructions:
        h,d,a = aim(i,(h,d,a))
    print(str(h*d))