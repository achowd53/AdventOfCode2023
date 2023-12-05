import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up, reduce
from math import log, prod
from string import ascii_uppercase, ascii_lowercase, ascii_letters #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from scanf import scanf
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def runPart1(filename):    
    lines = open(filename).read().split('\n\n')
    seeds, transforms = [*map(int,[*re.findall(r'\d+', lines[0])])], lines[1:]
    for i in range(7):
        transforms[i] = transforms[i].split('\n')[1:]
        for j in range(len(transforms[i])):
            transforms[i][j] = [*map(int,transforms[i][j].split())]
    ans = float("inf")
    for seed in seeds:
        for layer in transforms:
            for drs, srs, rl in layer:
                if srs <= seed < srs+rl:
                    seed = drs+seed-srs
                    break
        ans = min(ans, seed)
    return ans

def runPart2(filename):    
    lines = open(filename).read().split('\n\n')
    seeds, transforms = [*map(int,[*re.findall(r'\d+', lines[0])])], lines[1:]
    for i in range(7):
        transforms[i] = transforms[i].split('\n')[1:]
        for j in range(len(transforms[i])):
            transforms[i][j] = [*map(int,transforms[i][j].split())]
    ans = float("inf")
    for seed_start, length in [*zip(seeds[::2],seeds[1::2])]:
        R = [(seed_start, seed_start+length)] # Ranges
        for layer in transforms: # For each transform layer
            UR = R[:] # Untransformed Range
            TR = [] # Transformed Range
            for drs, srs, rl in layer: # Split range on interval
                sre = srs+rl
                NUR = [] # New Untransformed Range
                while UR:
                    (urs,ure) = UR.pop()
                    left = (urs, min(ure,srs))
                    mid = (max(urs,srs), min(ure,sre))
                    right = (max(urs,sre), ure)
                    if left[1] > left[0]: NUR.append(left)
                    if right[1] > right[0]: NUR.append(right)
                    if mid[1] > mid[0]: TR.append((mid[0]+drs-srs,mid[1]+drs-srs))
                UR = NUR
            R = UR + TR
        ans = min(min(R)[0], ans)
    return ans     
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
#print("Part 2:", runPart2("example2.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))