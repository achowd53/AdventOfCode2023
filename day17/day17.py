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
import heapq 
from shapely.geometry import Polygon, Point # Geometry is FUN, Double Resolution + Floodfill baby
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING WEEEEEEEEEEEEEEE

def runPart1(filename):    
    lines = np.array([*map(list, open(filename).read().splitlines())])
    grid = {(x,y):int(lines[y,x]) for x in range(lines.shape[1]) for y in range(lines.shape[0])}
    q = [(0,(0,0),None)]
    heapq.heapify(q)
    seen = set()
    while q:
        cost, pos, dir = heapq.heappop(q)
        if pos == (lines.shape[1]-1, lines.shape[0]-1):
            return cost
        if (pos,dir) in seen:
            continue
        seen.add((pos,dir))
        for new_dir in [(0,1), (1,0), (0,-1), (-1,0)]:
            if dir and (new_dir == dir or new_dir == (dir[0]*-1,dir[1]*-1)):
                continue
            cost_inc = 0
            for dist in range(1,4):
                new_pos = (pos[0]+dist*new_dir[0], pos[1]+dist*new_dir[1])
                if -1<new_pos[0]<lines.shape[1] and -1<new_pos[1]<lines.shape[0]:  
                    cost_inc += grid[new_pos]
                    heapq.heappush(q, (cost+cost_inc,new_pos,new_dir))

def runPart2(filename):    
    lines = np.array([*map(list, open(filename).read().splitlines())])
    grid = {(x,y):int(lines[y,x]) for x in range(lines.shape[1]) for y in range(lines.shape[0])}
    q = [(0,(0,0),None)]
    heapq.heapify(q)
    seen = set()
    while q:
        cost, pos, dir = heapq.heappop(q)
        if pos == (lines.shape[1]-1, lines.shape[0]-1):
            return cost
        if (pos,dir) in seen:
            continue
        seen.add((pos,dir))
        for new_dir in [(0,1), (1,0), (0,-1), (-1,0)]:
            if dir and (new_dir == dir or new_dir == (dir[0]*-1,dir[1]*-1)):
                continue
            cost_inc = 0
            for dist in range(1,4):
                new_pos = (pos[0]+dist*new_dir[0], pos[1]+dist*new_dir[1])
                if -1<new_pos[0]<lines.shape[1] and -1<new_pos[1]<lines.shape[0]:  
                    cost_inc += grid[new_pos]
            for dist in range(4,11):
                new_pos = (pos[0]+dist*new_dir[0], pos[1]+dist*new_dir[1])
                if -1<new_pos[0]<lines.shape[1] and -1<new_pos[1]<lines.shape[0]:  
                    cost_inc += grid[new_pos]
                    heapq.heappush(q, (cost+cost_inc,new_pos,new_dir))
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))