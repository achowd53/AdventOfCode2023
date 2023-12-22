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
    bricks = [[*map(int,re.findall(r"\d+", line))] for line in lines]
    bricks.sort(key = lambda x: x[2])
    def drop():
        bricks_copy = deepcopy(bricks)
        plane = defaultdict(int)
        for brick in bricks:
            drop_to = max(plane[(x,y)] for x,y in product(range(brick[0],brick[3]+1), range(brick[1],brick[4]+1)))
            drop_by = 0 if brick[2] == drop_to else brick[2]-drop_to-1
            brick[2] -= drop_by
            brick[5] -= drop_by
            for x,y in product(range(brick[0],brick[3]+1), range(brick[1],brick[4]+1)):
                plane[(x,y)] = brick[5]
        return sum(bricks_copy[i][2]!=bricks[i][2] for i in range(len(bricks)))
    drop()
    bricks_orig = bricks
    ans = 0
    for i in range(len(bricks)):
        bricks = [brick for idx,brick in enumerate(deepcopy(bricks_orig)) if idx!=i]
        if not drop():
            ans += 1
    return ans
    
def runPart2(filename):    
    lines = open(filename).read().splitlines()
    bricks = [[*map(int,re.findall(r"\d+", line))] for line in lines]
    bricks.sort(key = lambda x: x[2])
    def drop():
        bricks_copy = deepcopy(bricks)
        plane = defaultdict(int)
        for brick in bricks:
            drop_to = max(plane[(x,y)] for x,y in product(range(brick[0],brick[3]+1), range(brick[1],brick[4]+1)))
            drop_by = 0 if brick[2] == drop_to else brick[2]-drop_to-1
            brick[2] -= drop_by
            brick[5] -= drop_by
            for x,y in product(range(brick[0],brick[3]+1), range(brick[1],brick[4]+1)):
                plane[(x,y)] = brick[5]
        return sum(bricks_copy[i][2]!=bricks[i][2] for i in range(len(bricks)))
    drop()
    bricks_orig = bricks
    ans = 0
    for i in range(len(bricks)):
        bricks = [brick for idx,brick in enumerate(deepcopy(bricks_orig)) if idx!=i]
        ans += drop()
    return ans
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))