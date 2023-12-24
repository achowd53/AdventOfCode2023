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
def readNumpyGrid(filename):
    # np.pad (constant or wrap), np.rot90 (k=1 or k=-1), np.flip
    return np.array([*map(list, open(filename).read().splitlines())])
def findCharInGrid(numpyGrid, chars, as_complex=False):
    res = defaultdict(list)
    for y in range(numpyGrid.shape[0]):
        for x in range(numpyGrid.shape[1]):
            if numpyGrid[y,x] in chars:
                if as_complex:
                    res[numpyGrid[y,x]].append(x*1j+y)
                else:
                    res[numpyGrid[y,x]].append((x,y))
    return res
def readComplexGrid(numpyGrid, walls="#"):
    grid = {y+x*1j:numpyGrid[y][x] for y in range(len(numpyGrid)) for x in range(len(numpyGrid[0])) if numpyGrid[y][x] not in walls}
    return grid

# Graphing w/ NetworkX
import networkx as nx #Networkx for graph problems like connected components, simple paths, path_weight, shortest_path, simple_cycles
import geonetworkx as gnx #Use for coord compression graphs (two_degree_node_merge, get_edge_data(n1,n2)["weight"] = len(new_edges[(n1,n2)])))
def fourNeighbors(pos):
    return [pos+dir for dir in [1,-1,1j,-1j]]
def eightNeighbors(pos):
    return [pos+dir for dir in [1,1+1j,-1,-1+1j,1j,1j-1,-1j,-1j-1]]
def createNetworkXGraphFromGrid(complex_grid, neighbors=fourNeighbors, coord_compression=False, ignore_compress=(lambda x: x not in [])):
    edges = []
    for pos in complex_grid:
        for adj in neighbors(pos):
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
def createNetworkXGraphFromAdjacency(adjacency_dict, coord_compression=False, ignore_compress=(lambda x: x not in [])):
    edges = []
    for pos in adjacency_dict:
        for adj in adjacency_dict[pos]:
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
    start_state = 0
    end_cond = lambda c,s: s == 1
    q = [(0,start_state)] # Cost, State
    heapq.heapify(q)
    visited = set()
    while q:
        cost, state = heapq.heappop(q)
        if state in visited:
            continue
        visited.add(state)
        if end_cond(cost,state):
            # return cost
            continue
        for adj in neighbors(complex_grid, state):
            if adj in complex_grid:
                heapq.heappush(q, (cost+1,adj))
def bfs(complex_grid, neighbors=fourNeighbors, inp="THIS IS A SNIPPET NOT A FUNCTION"):
    start_state = 0
    end_cond = lambda c,s: s == 1
    q = deque([(0,start_state)]) # Cost, State
    visited = set()
    while q:
        cost, state = q.popleft(0)
        if state in visited:
            continue
        visited.add(state)
        if end_cond(cost,state):
            # return cost
            continue
        for adj in neighbors(complex_grid, state):
            if adj in complex_grid:
                q.append((cost+1,adj))
def dfs(complex_grid, neighbors=fourNeighbors, inp="THIS IS A SNIPPET NOT A FUNCTION"):
    start_state = 0
    end_cond = lambda c,s: s == 1
    q = [(0,start_state)] # Cost, State
    visited = set()
    while q:
        cost, state = q.pop()
        if state in visited:
            continue
        visited.add(state)
        if end_cond(cost,state):
            # return cost
            continue
        for adj in neighbors(complex_grid, state):
            if adj in complex_grid:
                q.append((cost+1,adj))

# Iteration Logic + Dynamic Programming + Memory Issue Solving
from itertools import product, chain, pairwise, combinations, permutations #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from functools import lru_cache, reduce
from copy import deepcopy #deepcopy() let's use copy a list without reference areas

# Math Functions
## Searching Numpy is always a safe bet for math functions
from math import log, prod, lcm
from sympy.ntheory.modular import crt
## Could more rarely be an issue of requiring a trait in input such as with polynomial pattern growth or cycle length (2023 day21)
def polynomialEvaluation(points, deg, x): # Solve n-degree polynomial from n+1 points and calc for X
    coef = np.polyfit(*zip(*points), deg)
    return round(np.polyval(coef, x))
from shapely.geometry import Polygon, Point, LineString # Geometry is FUN, Double Resolution + Floodfill baby
def latticePolygonArea(coords): # Shoelace + Pick's if closed coords set (a,b,c,a)
    # Generalized Pick's: https://math.stackexchange.com/questions/2773118/general-form-of-picks-theorem
    ## Self-Intersections for Generalized Picks: https://gis.stackexchange.com/questions/423351/identifying-self-intersections-in-linestring-using-shapely
    bounds = sum(abs(x2-x1)+abs(y2-y1) for (x1,y1),(x2,y2) in pairwise(coords))
    return int(Polygon(coords).area + bounds/2 + 1)
from z3 import Solver, Int, And #Solver.add, Solver.check, Solver.model, model.evaluate
def splitInterval(interval, split_point): #Split point either of form a) (int,int) or b) (char,int)
    if type(split_point[0]) == int: # Split on continuous range with interval
        (x1,x2),(y1,y2) = interval, split_point
        new_intervals = [(x1,min(x2,y1)),(max(x1,y1),min(x2,y2)),(max(x1,y2),x2)]
        return [(x,y) if y>x else None for x,y in new_intervals]
    else: # Split on discrete range with integer
        if (split_point[0]=='<' and split_point[1]>interval[1]) or (split_point[0]=='>' and split_point[1]<interval[0]):
            return [interval]
        if split_point[0]=='<':
            return [(interval[0],split_point[1]-1),(split_point[1],interval[1])]
        else:
            return [(interval[0],split_point[1]),(split_point[1]+1,interval[1])]
import portion # More Interval stuff