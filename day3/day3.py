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
    lines = open(filename).read().splitlines()
    return sum(sum(int(lines[r][num[0]:num[1]]) # Num value
                for num in [m.span() for m in re.finditer(r'(\d+)', lines[r])] # Each number in line
                if any((-1<y<len(lines) and -1<x<len(lines[0]) and lines[y][x] not in "0123456789.") # If symbol
                    for y in range(r-1,r+2) 
                    for x in range(num[0]-1,num[1]+1)))
            for r in range(len(lines))) # Each line

def runPart2(filename):    
    gear_boxes = collections.defaultdict(list)
    lines = open(filename).read().splitlines()
    for r in range(len(lines)):
        for num in [m.span() for m in re.finditer(r'(\d+)', lines[r])]:
            for gear in [(x,y) for y in range(r-1,r+2) for x in range(num[0]-1,num[1]+1)
                         if (-1<y<len(lines) and -1<x<len(lines[0]) and lines[y][x] == "*")]:
                gear_boxes[gear].append(int(lines[r][num[0]:num[1]]))
    return sum(prod(gear_boxes[gear]) for gear in gear_boxes if len(gear_boxes[gear]) == 2)
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))