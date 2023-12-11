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

def runPart1(filename):    
    grid = np.array([list(line) for line in open(filename).read().splitlines()])
    galaxies = np.argwhere(grid == "#")
    i_exp = set(i for i in range(grid.shape[0]) if np.all(grid[i]=="."))
    j_exp = set(j for j in range(grid.shape[1]) if np.all(grid[:,j]=="."))
    return sum(abs(y2-y1)+len(i_exp & set(range(min(y1,y2),max(y1,y2))))+
               abs(x2-x1)+len(j_exp & set(range(min(x1,x2),max(x1,x2))))
               for (y1,x1),(y2,x2) in combinations(galaxies, 2))

def runPart2(filename):    
    grid = np.array([list(line) for line in open(filename).read().splitlines()])
    galaxies = np.argwhere(grid == "#")
    i_exp = set(i for i in range(grid.shape[0]) if np.all(grid[i]=="."))
    j_exp = set(j for j in range(grid.shape[1]) if np.all(grid[:,j]=="."))
    return sum(abs(y2-y1)+999999*len(i_exp & set(range(min(y1,y2),max(y1,y2))))+
               abs(x2-x1)+999999*len(j_exp & set(range(min(x1,x2),max(x1,x2))))
               for (y1,x1),(y2,x2) in combinations(galaxies, 2))
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))