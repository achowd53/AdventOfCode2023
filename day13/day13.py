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
    ans = 0
    for lines in open(filename).read().split('\n\n'):
        grid = np.array([list(x) for x in lines.split('\n')])
        for j in range(1,grid.shape[1]):
            min_dist = min(j-1,grid.shape[1]-j-1)
            ans += j if np.all(np.flip(grid[:,j:j+min_dist+1], axis=1) == grid[:,j-1-min_dist:j]) else 0
        for i in range(1,grid.shape[0]):
            min_dist = min(i-1,grid.shape[0]-i-1)
            ans += 100*i if np.all(np.flip(grid[i:i+min_dist+1], axis=0) == grid[i-1-min_dist:i]) else 0
    return ans

def runPart2(filename):    
    ans = 0
    for lines in open(filename).read().split('\n\n'):
        grid = np.array([list(x) for x in lines.split('\n')])
        for j in range(1,grid.shape[1]):
            min_dist = min(j-1,grid.shape[1]-j-1)
            ans += j if np.sum(np.flip(grid[:,j:j+min_dist+1], axis=1) != grid[:,j-1-min_dist:j]) == 1 else 0
        for i in range(1,grid.shape[0]):
            min_dist = min(i-1,grid.shape[0]-i-1)
            ans += 100*i if np.sum(np.flip(grid[i:i+min_dist+1], axis=0) != grid[i-1-min_dist:i]) == 1 else 0
    return ans
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))