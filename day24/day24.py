import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
from collections import defaultdict, Counter, deque
from functools import lru_cache, reduce
from math import log, prod, lcm
from sympy.ntheory.modular import crt
from string import ascii_uppercase, ascii_lowercase, ascii_letters #ascii_uppercase, ascii_lowercase, etc..
from itertools import product, chain, pairwise, combinations, permutations #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
import networkx as nx #Networkx for graph problems like connected components
import geonetworkx as gnx #Use for coord compression graphs (two_degree_node_merge, get_edge_data(n1,n2)["weight"] = len(new_edges[(n1,n2)])))
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
from shapely.geometry import Polygon, Point, LineString # Geometry is FUN, Double Resolution + Floodfill baby, Shoelace+Pick's for point counting
import heapq 
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING in order to reduce long running problems
## Could more rarely be an issue of requiring a trait in input such as with polynomial pattern growth or cycle length
# Use a defaultdict to represent height of plane to simulate falling objects
# Use pypy3 instead of python to run code

def runPart1(filename,s,e):    
    lines = [[*map(int,re.findall(r'-?\d+',line))] for line in open(filename).read().splitlines()]
    ans = 0
    for i in range(len(lines)):
        px,py,_,vx,vy,_ = lines[i]
        lines[i] = LineString([[px,py],[px+vx*e,py+vy*e]])
    for lineA, lineB in combinations(lines,2):
        intersection = lineA.intersection(lineB)
        if type(intersection)==Point and s <= intersection.x <= e and s <= intersection.y <= e:
            ans += 1
    return ans

def runPart2(filename):    
    lines = open(filename).read().splitlines()
    lines = [[*map(int,re.findall(r'-?\d+',line))] for line in lines]
    pos, vel = [Int('x'), Int('y'), Int('z')], [Int('a'), Int('b'), Int('c')]
    ts = {'t'+str(i):Int('t'+str(i)) for i in range(len(lines))}
    solv = Solver()
    for i,(px,py,pz,vx,vy,vz) in enumerate(lines):
        solv.add(pos[0]+vel[0]*ts['t'+str(i)] == px+vx*ts['t'+str(i)])
        solv.add(pos[1]+vel[1]*ts['t'+str(i)] == py+vy*ts['t'+str(i)])
        solv.add(pos[2]+vel[2]*ts['t'+str(i)] == pz+vz*ts['t'+str(i)])
    solv.check()
    mod = solv.model()
    return mod.evaluate(sum(pos))
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt",7,27))
print("Part 2:", runPart2("example.txt"))
#print("Part 2:", runPart2("example2.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt",200000000000000,400000000000000))
print("Part 2:", runPart2("input.txt"))