
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string





if __name__ == "__main__":
    pass