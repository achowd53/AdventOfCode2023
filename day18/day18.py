import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
from collections import defaultdict, Counter, deque
from functools import lru_cache, reduce
from math import log, prod, lcm
from sympy.ntheory.modular import crt
from string import ascii_uppercase, ascii_lowercase, ascii_letters #ascii_uppercase, ascii_lowercase, etc..
from itertools import product, chain, pairwise, combinations, permutations #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from scanf import scanf
import networkx as nx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
from shapely.geometry import Polygon, Point # Geometry is FUN, Double Resolution + Floodfill baby
import heapq 
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING WEEEEEEEEEEEEEEE

def runPart1(filename):    
    coords = [(0,0)]
    for line in open(filename).read().splitlines():
        dir,dist,_ = line.split()
        dirs = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
        coords.append((coords[-1][0]+int(dist)*dirs[dir][0], coords[-1][1]+int(dist)*dirs[dir][1]))
    bounds = sum(abs(x2-x1)+abs(y2-y1) for (x1,y1),(x2,y2) in zip(coords[:-1],coords[1:]))
    return int(Polygon(coords).area-bounds/2+1 + bounds)

def runPart2(filename):    
    coords = [(0,0)]
    for line in open(filename).read().splitlines():
        _,_,paint = line.split()
        dist = int(paint[2:7], 16)
        dir = {"0":"R","1":"D","2":"L","3":"U"}[paint[7]]
        dirs = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
        coords.append((coords[-1][0]+dist*dirs[dir][0], coords[-1][1]+dist*dirs[dir][1]))
    bounds = sum(abs(x2-x1)+abs(y2-y1) for (x1,y1),(x2,y2) in zip(coords[:-1],coords[1:]))
    return int(Polygon(coords).area-bounds/2+1 + bounds)

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))