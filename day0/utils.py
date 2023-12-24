# General Python DS Tips
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Dicts work the same as sets in Python for operations (A|B updates A with B)

# Regex Reading
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
def matchFile(filename, regex=None):
    lines = open(filename).read()
    if regex:
        lines = re.findall(regex, lines)
    return lines
def matchLines(filename, regex='Ints'):
    lines = open(filename).read().splitlines()
    if regex == "int":
        lines = [[*map(int,re.findall(r'-?\d+', line))] for line in lines]
    elif regex:
        lines = [re.findall(regex, line) for line in lines]
    return lines           
def matchChunks(filename, regex=None):
    lines = open(filename).read().split('\n\n')
    if regex == "int":
        lines = [[*map(int,re.findall(r'-?\d+', line))] for line in lines]
    elif regex:
        lines = [re.findall(regex, line) for line in lines]
    return lines
        
# Grid Creation
import scipy.ndimage as sp #scipy.ndimage correlate and convolve
import numpy as np #np arrays are just nice in general, rot90 default axis=1 rotates left axis=0 would be right
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
def gridLimits(filename, walls="#"):
    grid = readComplexGrid(filename, walls)
    xs = sorted([c.real for c in grid])
    ys = sorted([c.imag for c in grid])
    return [[xs[0],ys[0]],[xs[1],ys[1]]]
def readNumpyGrid(filename):
    # np.pad (constant or wrap), np.rot90 (k=1 or k=-1), np.flip
    return np.array([*map(list, open(filename).read().splitlines())])
def readComplexGrid(filename, walls="#"):
    lines = open(filename).read().splitlines()
    grid = {y+x*1j:lines[y][x] for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] not in walls}
    return grid

# Graphing w/ NetworkX
import networkx as nx #Networkx for graph problems like connected components, simple paths, path_weight, shortest_path, simple_cycles
import geonetworkx as gnx #Use for coord compression graphs (two_degree_node_merge, get_edge_data(n1,n2)["weight"] = len(new_edges[(n1,n2)])))
def fourNeighbors(complex_grid, pos):
    return [pos+dir for dir in [1,-1,1j,-1j]]
def eightNeighbors(complex_grid, pos):
    return [pos+dir for dir in [1,1+1j,-1,-1+1j,1j,1j-1,-1j,-1j-1]]
def createNetworkXGraph(complex_grid, neighbors=fourNeighbors, coord_compression=False, ignore_compress=(lambda x: x not in [])):
    edges = []
    for pos in complex_grid:
        for adj in neighbors(complex_grid, pos):
            if adj in complex_grid:
                edges.append((pos,adj))
    if coord_compression:
        G = gnx.GeoGraph()
        G.add_weighted_edges_from([(u,v,1) for u,v in edges])
        new_edges = gnx.two_degree_node_merge(G, ignore_compress)
        for n1,n2 in new_edges:
            G.get_edge_data(n1,n2)["weight"] = len(new_edges[(n1,n2)])
    else:
        G = nx.DiGraph()
        G.add_edges_from(edges)
    return G

# DFS (Stack - List) / BFS (Queue - Deque) / Dijkstra (Priority Queue - HeapQ)
from collections import defaultdict, Counter, deque # Use a defaultdict to represent height of plane to simulate falling objects (2023 day22)
import heapq 
def dijkstra(complex_grid, neighbors=fourNeighbors, inp="THIS IS A SNIPPET NOT A FUNCTION"):
    start_state, end_state = 0, 0
    q = [(0,start_state)] # Cost, State
    heapq.heapify(q)
    visited = set()
    while q:
        cost, state = heapq.heappop(q)
        if state == end_state:
            return cost
        if state in visited:
            continue
        visited.add(state)
        for adj in neighbors(complex_grid, state):
            if adj in complex_grid:
                heapq.heappush(q, (cost+1,adj))

# Iteration Logic + Dynamic Programming + Memory Issue Solving
from itertools import product, chain, pairwise, combinations, permutations #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from functools import lru_cache, reduce
from copy import deepcopy #deepcopy() let's use copy a list without reference areas

# Math Functions
## Could more rarely be an issue of requiring a trait in input such as with polynomial pattern growth or cycle length (2023 day21)
from math import log, prod, lcm
from sympy.ntheory.modular import crt
def quadraticFromPoints(X, x0, y0, x1, y1, x2, y2): # Solve quadratic for X, with quadratic build from 3 points
    diff10,diff21 = (y1-y0)/(x1-x0), (y2-y1)/(x2-x1)
    a,b,c = (diff21-diff10)/(x2-x0), diff10, y0
    return int(a*(X-x1)*(X-x0)+b*(X-x0)+c)
from shapely.geometry import Polygon, Point, LineString # Geometry is FUN, Double Resolution + Floodfill baby, Shoelace+Pick's for point counting
def latticePolygonArea(coords): # Shoelace + Pick's if closed coords set (a,b,c,a)
    bounds = sum(abs(x2-x1)+abs(y2-y1) for (x1,y1),(x2,y2) in pairwise(coords))
    return int(Polygon(coords).area + bounds/2 + 1)
from z3 import Solver, Int, And #Solver.add, Solver.check, Solver.model, model.evaluate
def splitInterval(interval, split_point): #Split point either of form a) (int,int) or b) (char,int)
    if type(split_point[0]) == int:
        (x1,x2),(y1,y2) = interval, split_point
        new_intervals = [(x1,min(x2,y1)),(max(x1,y1),min(x2,y2)),(max(x1,y2),x2)]
        return [(x,y) if y>x else None for x,y in new_intervals]
    else:
        if (split_point[0]=='<' and split_point[1]>interval[1]) or (split_point[0]=='>' and split_point[1]<interval[0]):
            return [interval]
        if split_point[0]=='<':
            return [(interval[0],split_point[1]-1),(split_point[1],interval[1])]
        else:
            return [(interval[0],split_point[1]),(split_point[1]+1,interval[1])]
import portion # More Interval stuff