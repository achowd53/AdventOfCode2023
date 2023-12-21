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
from shapely.geometry import Polygon, Point # Geometry is FUN, Double Resolution + Floodfill baby, Shoelace+Pick's for point counting
import heapq 
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING WEEEEEEEEEEEEEEE

def runPart1(filename):    
    lines = open(filename).read().splitlines()
    grid = {x+y*1j:lines[y][x] for y in range(len(lines)) for x in range(len(lines[0]))}
    for key in grid:
        if grid[key]=='S':
            grid[key] = '.'
            start = key
    stack = [(start,0)]
    end = set()
    visited = set()
    while stack:
        pos, steps = stack.pop()
        if steps == 64:
            end.add(pos)
            continue
        for dir in [1,-1,1j,-1j]:
            if dir+pos in grid and grid[dir+pos]=='.':
                if (dir+pos,steps+1) not in visited:
                    visited.add((dir+pos,steps+1))
                    stack.append((dir+pos,steps+1))
    return len(end)

def runPart2(filename):    
    lines = np.array([*map(list, open(filename).read().splitlines())])
    grid = np.pad(lines, 2*lines.shape[0], 'wrap')
    grid = {x+y*1j:grid[y][x] for y in range(grid.shape[0]) for x in range(grid.shape[1])}
    for key in grid:
        if grid[key]=='S':
            grid[key] = '.'
            start = key
    start -= 2*lines.shape[0]+2j*lines.shape[1]
    stack = [(start,0)]
    first = 26501365%lines.shape[0]
    end = {first:set(),first+lines.shape[0]:set(),first+2*lines.shape[0]:set()}
    visited = set()
    while stack:
        pos, steps = stack.pop()
        if steps in end:
            end[steps].add(pos)
        if steps == first+2*lines.shape[0]:
            continue
        for dir in [1,-1,1j,-1j]:
            if dir+pos in grid and grid[dir+pos]=='.':
                if (dir+pos,steps+1) not in visited:
                    visited.add((dir+pos,steps+1))
                    stack.append((dir+pos,steps+1))
    x0,x1,x2 = [x for x in end]
    y0,y1,y2 = [len(x) for x in end.values()]
    diff10,diff21 = (y1-y0)/(x1-x0), (y2-y1)/(x2-x1)
    a,b,c = (diff21-diff10)/(x2-x0), diff10, y0
    return int(a*(26501365-x1)*(26501365-x0)+b*(26501365-x0)+c)
    
    
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))