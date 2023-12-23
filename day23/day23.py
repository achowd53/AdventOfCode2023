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
import geonetworkx as gnx
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
from shapely.geometry import Polygon, Point # Geometry is FUN, Double Resolution + Floodfill baby, Shoelace+Pick's for point counting
import heapq 
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING in order to reduce long running problems
## Could more rarely be an issue of requiring a trait in input such as with polynomial pattern growth or cycle length
# Use a defaultdict to represent height of plane to simulate falling objects

def runPart1(filename):    
    lines = open(filename).read().splitlines()
    start, end = 1j, len(lines)-1+len(lines[0])*1j-2j    
    grid = {y+x*1j:lines[y][x] for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] != '#'}
    edges = []
    for pos in grid:
        if grid[pos] == ".":
            for dir in [1,-1,1j,-1j]:
                if pos+dir in grid:
                    edges.append((pos,pos+dir))
        else:
            for char,dir in [("^",-1),(">",1j),("<",-1j),("v",1)]:
                if grid[pos] == char:
                    if pos+dir in grid:
                        edges.append((pos,pos+dir))
    G = nx.DiGraph()
    G.add_edges_from(edges)
    return max(len(p) for p in nx.all_simple_paths(G,start,end))-1

def runPart2(filename):    
    lines = open(filename).read().splitlines()
    start, end = 1j, len(lines)-1+len(lines[0])*1j-2j    
    grid = {y+x*1j:lines[y][x] for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] != '#'}
    edges = [(pos,pos+dir,1) for pos,dir in product(grid,[1,-1,1j,-1j]) if pos+dir in grid]
    G = gnx.GeoGraph()
    G.add_weighted_edges_from(edges)
    new_edges = gnx.two_degree_node_merge(G)
    for n1,n2 in new_edges:
        G.get_edge_data(n1,n2)["weight"] = len(new_edges[(n1,n2)])
    return max(nx.path_weight(G, p, weight="weight") for p in nx.all_simple_paths(G, start, end))

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))