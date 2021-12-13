
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

test3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

def parse_graph(str):
    inp = str.splitlines()
    edges = {"start":[]}
    for line in inp:
        a,b = line.split('-')
        # edge case for directed 
        if a == "start" or b == "start":
            if a == "start":
                edges["start"].append(b)
            if b == "start":
                edges["start"].append(a)
        else:
            if a in edges.keys():
                edges[a].append(b)
            else:
                edges[a] = [b]

            if b in edges.keys():
                edges[b].append(a)
            else:
                edges[b] = [a]
    edges.pop("end")
    return edges

def get_paths(graph1, repeats=False):
    paths = set()
    def path(graph, home, progress):
        g = graph.copy()
        # Graph is empty, meaming no valid edges left
        #print("Starting -- ", graph, home, progress)
        if home == "end":
            #print(progress)
            return paths.add(''.join(progress))
        if home not in g.keys():
            return []
        if home == "start" or home.islower():
            g.pop(home)
        for i in graph[home]:
            p = progress.copy()
            p.append(i)
            #print("next call: ", g, i, p)
            path(g, i, p)
    
    def path_with_repeat(graph, home, progress, repeating, count):
        g = graph.copy()
        #print("Starting -- ", graph, home, progress, repeating, count)
        if home == "end":
            #print(progress)
            #print(repeating, progress)
            return paths.add(''.join(progress))
        if home not in g.keys():
            return []
        if home == "start":
            g.pop(home)
        else:
            if home == repeating:
                #print("in repeating")
                count += 1
                if count == 2:
                    g.pop(home)
            elif home != repeating and home.islower():
                g.pop(home)
        for i in graph[home]:
            p = progress.copy()
            p.append(i)
            #print("next call: ", g, i, p)
            path_with_repeat(g, i, p, repeating, count)

    if repeats:
        ks = list(graph1.keys())
        ks.remove("start")
        for r in filter(lambda s: s.islower(), ks):
            #print(r)
            path_with_repeat(graph1, "start", ["start"], r, 0)
    else:
        path(graph1, "start", ["start"])

    return paths
    

if __name__ == "__main__":
    input = parse_graph(input_str)
    # Part 1
    print(len(get_paths(input)))

    # Part 2
    print(len(get_paths(input, True)))