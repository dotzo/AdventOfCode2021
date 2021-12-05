
# Description

import os
import sys
from itertools import chain

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

def parse(inp):
    a = inp.splitlines()
    for i in range(len(a)):
        a[i] = list(map(int, a[i].replace(' -> ',',').split(',')))
        a[i] = (tuple(a[i][0:2]), tuple(a[i][2:]))
    return a

def sign(x):
    return 1 if x > 0 else -1

def vert_or_hori(a,b):
    return a[0] == b[0] or a[1] == b[1]  

def points_on_vert(a,b):
    s = min(a[1],b[1])
    e = max(a[1],b[1])

    return list(zip([a[0]]*(e - s + 1),range(s,e+1)))

def points_on_hori(a,b):
    s = min(a[0],b[0])
    e = max(a[0],b[0])

    return list(zip(range(s,e+1),[a[1]]*(e - s + 1)))

def points_on_diag(a,b):
    s1, s2 = a[0], a[1]
    e1, e2 = b[0], b[1]

    d1, d2 = sign(e1 - s1), sign(e2 - s2)
    r = []
    for i in range(abs(e1 - s1) + 1):
        r.append((s1+i*d1, s2+i*d2))
    return r

def get_points(a,b):
    if a[0] == b[0]:
        return points_on_vert(a,b)
    elif a[1] == b[1]:
        return points_on_hori(a,b)
    else:
        return points_on_diag(a,b)

def get_frequency(ps):
    d = {}
    for p in ps:
        if p in d.keys():
            d[p] += 1
        else:
            d[p] = 1
    return d

def get_overlap_count(d):
    return len(list(filter(lambda x: x > 1, d.values())))

if __name__ == "__main__":
    # Part 1
    vh = list(filter(lambda x: vert_or_hori(*x), parse(input_str)))
    ps = list(chain(*map(lambda x: get_points(*x), vh)))
    f = get_frequency(ps)
    o = get_overlap_count(f)
    print(o)

    # Part 2
    segments = parse(input_str)
    points = list(chain(*map(lambda x: get_points(*x), segments)))
    print(get_overlap_count(get_frequency(points)))