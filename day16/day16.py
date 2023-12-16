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
from shapely.geometry import Polygon, Point # Geometry is FUN, Double Resolution + Floodfill baby
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))
# DYNAMIC PROGRAMMING WEEEEEEEEEEEEEEE

def runPart1(filename):    
    grid = np.array([*map(list, open(filename).read().splitlines())])
    grid = {complex(i,j):grid[i,j] for i in range(len(grid)) for j in range(len(grid[0]))}
    beams = [(-1j,1j)]
    beams_seen = set()
    while beams:
        beam, dir = beams.pop()
        beam += dir
        if (beam,dir) in beams_seen or beam not in grid:
            continue
        beams_seen.add((beam, dir))
        match grid[beam]:
            case "|":
                beams.extend([(beam,1),(beam,-1)] if dir.real==0 else [(beam,dir)])
            case "-":
                beams.extend([(beam,1j),(beam,-1j)] if dir.imag==0 else [(beam,dir)])
            case "/":
                if dir.real == 0:
                    beams.append((beam,-1) if dir.imag==1 else (beam,1))
                else:
                    beams.append((beam,-1j) if dir.real==1 else (beam,1j))
            case "\\":
                if dir.real == 0:
                    beams.append((beam,1) if dir.imag==1 else (beam,-1))
                else:
                    beams.append((beam,1j) if dir.real==1 else (beam,-1j))
            case ".":
                beams.append((beam,dir))
    return len(set(beam for beam,_ in beams_seen))

def runPart2(filename):    
    lines = np.array([*map(list, open(filename).read().splitlines())])
    grid = {complex(i,j):lines[i,j] for i in range(len(lines)) for j in range(len(lines[0]))}
    start_beams = [(i-1j,1j) for i in range(len(lines))] + [(-1+i*1j,1) for i in range(len(lines[0]))] + [(i+len(lines[0])*1j,-1j) for i in range(len(lines))] + [(len(lines)+i*1j,-1) for i in range(len(lines[0]))]
    ans = []
    for start_beam in start_beams:
        beams = [start_beam]
        beams_seen = set()
        while beams:
            beam, dir = beams.pop()
            beam += dir
            if (beam,dir) in beams_seen or beam not in grid:
                continue
            beams_seen.add((beam, dir))
            match grid[beam]:
                case "|":
                    beams.extend([(beam,1),(beam,-1)] if dir.real==0 else [(beam,dir)])
                case "-":
                    beams.extend([(beam,1j),(beam,-1j)] if dir.imag==0 else [(beam,dir)])
                case "/":
                    if dir.real == 0:
                        beams.append((beam,-1) if dir.imag==1 else (beam,1))
                    else:
                        beams.append((beam,-1j) if dir.real==1 else (beam,1j))
                case "\\":
                    if dir.real == 0:
                        beams.append((beam,1) if dir.imag==1 else (beam,-1))
                    else:
                        beams.append((beam,1j) if dir.real==1 else (beam,-1j))
                case ".":
                    beams.append((beam,dir))
        ans.append(len(set(beam for beam,_ in beams_seen)))
    return max(ans)
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))