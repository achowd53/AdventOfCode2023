import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
from collections import defaultdict, Counter
from functools import lru_cache, reduce
from math import log, prod, lcm
from sympy.ntheory.modular import crt
from string import ascii_uppercase, ascii_lowercase, ascii_letters #ascii_uppercase, ascii_lowercase, etc..
from itertools import product, chain, pairwise #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from scanf import scanf
import networkx as nx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
from shapely.geometry import Polygon, Point # Geometry is FUN
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def runPart1(filename):    
    lines = open(filename).read().splitlines()
    grid = {(x,y):lines[y][x] for y in range(len(lines)) for x in range(len(lines[0]))}
    graph = []
    for x,y in grid:
        for st, ed, ed_coords in [("S|JL","S|7F",(x,y-1)),("S|7F","S|JL",(x,y+1)),("S-J7","S-LF",(x-1,y)),("S-LF","S-J7",(x+1,y))]:
            if grid[(x,y)] in st and ed_coords in grid and grid[ed_coords] in ed:
                graph.append(((x,y), ed_coords))
    G = nx.DiGraph()
    G.add_edges_from(graph)
    max_loop = sorted(list(nx.simple_cycles(G)), key=lambda x: len(x))[-1]
    return int(len(max_loop)/2)
    
def runPart2(filename):    
    lines = open(filename).read().splitlines()
    grid = {(x,y):lines[y][x] for y in range(len(lines)) for x in range(len(lines[0]))}
    graph = []
    for x,y in grid:
        for st, ed, ed_coords in [("S|JL","S|7F",(x,y-1)),("S|7F","S|JL",(x,y+1)),("S-J7","S-LF",(x-1,y)),("S-LF","S-J7",(x+1,y))]:
            if grid[(x,y)] in st and ed_coords in grid and grid[ed_coords] in ed:
                graph.append(((x,y), ed_coords))
    G = nx.DiGraph()
    G.add_edges_from(graph)
    max_loop = sorted(list(nx.simple_cycles(G)), key=lambda x: len(x))[-1]
    poly = Polygon(max_loop)
    return sum(Point(x,y).within(poly) for x,y in grid if (x,y) not in max_loop)


print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example2.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))