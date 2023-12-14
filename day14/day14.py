import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
from collections import defaultdict, Counter
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
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING WEEEEEEEEEEEEEEE

def runPart1(filename): 
    grid = np.array([*map(list, open(filename).read().splitlines())])
    grid = np.pad(grid, 1, 'constant', constant_values='#')
    num_rocks = 0
    for col,row in product(range(grid.shape[1]), range(grid.shape[0]-1,-1,-1)):
        if grid[row,col] == "O":
            grid[row,col] = "."
            num_rocks += 1
        elif grid[row,col] == "#":
            grid[row+1:row+1+num_rocks,col] = "O"
            num_rocks = 0
    return sum(grid.shape[0]-row-1 for col,row in product(range(grid.shape[1]),range(grid.shape[0])) if grid[row,col]=="O")

def runPart2(filename):    
    grid = np.array([*map(list, open(filename).read().splitlines())])
    grid = np.pad(grid, 1, 'constant', constant_values='#')
    def tilt():
        num_rocks = 0
        for col,row in product(range(grid.shape[1]), range(grid.shape[0]-1,-1,-1)):
            if grid[row,col] == "O":
                grid[row,col] = "."
                num_rocks += 1
            elif grid[row,col] == "#":
                grid[row+1:row+1+num_rocks,col] = "O"
                num_rocks = 0
    seen, end_cycle = {}, None
    for cycle in range(1000000000):
        for _ in range(4):
            tilt()
            grid = np.rot90(grid, k=-1)
        if cycle == end_cycle:
            return sum(grid.shape[0]-row-1 for col,row in product(range(grid.shape[1]),range(grid.shape[0])) if grid[row,col]=="O")
        if not end_cycle:
            hash = grid.tobytes()
            if hash in seen:
                end_cycle = cycle+(100000000-seen[hash])%(cycle-seen[hash])+3
            else:
                seen[hash] = cycle

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))