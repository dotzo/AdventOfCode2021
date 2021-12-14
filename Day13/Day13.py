
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string


test = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

def parse(str):
    s = str.split('\n\n')
    points = set()
    folds = []
    for point in s[0].splitlines():
        x,y = point.split(',')
        points.add((int(x), int(y)))

    for fold in s[1].splitlines():
        s,t = fold.replace('fold along ','').split('=')
        folds.append((s,int(t)))

    return points, folds

def do_fold(points, fold):
    if fold[0] == 'y':
        f = fold[1]
        to_add = []
        to_remove = []
        for x,y in points:
            if y < f:
                #print("unaffected point: ", x, y)
                continue
            else:
                #print("affected point: ", x, y, " - new point: ", x, f - (y - f))
                to_add.append( (x , f - (y - f)) )
                to_remove.append((x,y))
        points.difference_update(to_remove)
        points.update(to_add)
    else:
        f = fold[1]
        to_add = []
        to_remove = []
        for x,y in points:
            if x < f:
                #print("unaffected point: ", x, y)
                continue
            else:
                #print("affected point: ", x, y, " - new point: ", f - (x - f), y)
                to_add.append((f - (x - f), y))
                to_remove.append((x,y))
        points.difference_update(to_remove)
        points.update(to_add)


def print_points(points):
    max_x = max(list(zip(*points))[0])
    max_y = max(list(zip(*points))[1])
    #print("extremes", max_x, max_y)

    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            if (x,y) in points:
                line += '#'
            else:
                line += '.'
            line += ' '
        print(line)

    print()


if __name__ == "__main__":
    
    # Part 1
    points, folds = parse(input_str)
    do_fold(points, folds[0])
    print("Visible points after 1 fold - ", len(points))
    print()

    # Part 2
    points, folds = parse(input_str)
    for f in folds:
        do_fold(points, f)
    print_points(points)