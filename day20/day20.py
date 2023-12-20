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
    switches = reduce(lambda x,y: x|y, [{line.split(" -> ")[0][1:]:
                        ['b', 'b', line.split(" -> ")[1].split(", ")] if line.split(' -> ')[0][0]=='b' else
                        ['&', dict(), line.split(" -> ")[1].split(", ")] if line.split(' -> ')[0][0]=='&' else
                        ['%', 0, line.split(" -> ")[1].split(", ")]
                      } for line in open(filename).read().splitlines()])
    for key in switches:
        for exit in switches[key][2]:
            if exit in switches and switches[exit][0] == "&":
                switches[exit][1][key] = 0
    pulses = [0,0]
    for _ in range(1000):
        q = deque([("button","roadcaster",0)])
        while q:
            sig_frm, cur_mod, sig = q.popleft()
            pulses[sig] += 1
            if cur_mod not in switches:
                continue
            if switches[cur_mod][0] == "b":
                q.extend([(cur_mod,switch,0) for switch in switches[cur_mod][2]])
            elif switches[cur_mod][0] == "%":
                if sig == 0:
                    switches[cur_mod][1] = (switches[cur_mod][1]+1)%2
                    q.extend([(cur_mod,switch,switches[cur_mod][1]) for switch in switches[cur_mod][2]])
            else:
                switches[cur_mod][1][sig_frm] = sig
                send_sig = 0 if all(switches[cur_mod][1].values()) else 1
                q.extend([(cur_mod,switch,send_sig) for switch in switches[cur_mod][2]])
    return prod(pulses)

def runPart2(filename):    
    switches = reduce(lambda x,y: x|y, [{line.split(" -> ")[0][1:]:
                        ['b', 'b', line.split(" -> ")[1].split(", ")] if line.split(' -> ')[0][0]=='b' else
                        ['&', dict(), line.split(" -> ")[1].split(", ")] if line.split(' -> ')[0][0]=='&' else
                        ['%', 0, line.split(" -> ")[1].split(", ")]
                      } for line in open(filename).read().splitlines()])
    for key in switches:
        for exit in switches[key][2]:
            if exit in switches and switches[exit][0] == "&":
                switches[exit][1][key] = 0
            elif exit == "rx":
                track = key
    cycles, presses = {key:[] for key in switches[track][1]}, 0
    while True:
        presses += 1
        q = deque([("button","roadcaster",0)])
        while q:
            sig_frm, cur_mod, sig = q.popleft()
            if cur_mod == track and sig:
                cycles[sig_frm].append(presses)
            if cur_mod not in switches:
                continue
            if switches[cur_mod][0] == "b":
                q.extend([(cur_mod,switch,0) for switch in switches[cur_mod][2]])
            elif switches[cur_mod][0] == "%":
                if sig == 0:
                    switches[cur_mod][1] = (switches[cur_mod][1]+1)%2
                    q.extend([(cur_mod,switch,switches[cur_mod][1]) for switch in switches[cur_mod][2]])
            else:
                switches[cur_mod][1][sig_frm] = sig
                send_sig = 0 if all(switches[cur_mod][1].values()) else 1
                q.extend([(cur_mod,switch,send_sig) for switch in switches[cur_mod][2]])
        if all(len(cycle)>1 for cycle in cycles.values()):
            break
    return lcm(*[ed-st for st,ed in cycles.values()])

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))