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
    lines = open(filename).read().split(",")
    ans = 0
    for line in lines:
        cur_val = 0
        line = [ord(x) for x in line]
        for char in line:
            cur_val = ((cur_val+char)*17)%256
        ans += cur_val
    return ans

def runPart2(filename):    
    lines = open(filename).read().split(",")
    boxes = [[] for _ in range(256)]
    for line in lines:
        box = 0
        if "-" in line:
            ascii = [ord(x) for x in line[:-1]]
            for char in ascii:
                box = ((box+char)*17)%256
            boxes[box] = [x for x in boxes[box] if x[0] != line[:-1]]
        else:
            label, power = line.split("=")
            power = int(power)
            ascii = [ord(x) for x in label]
            for char in ascii:
                box = ((box+char)*17)%256
            if any(x[0] == label for x in boxes[box]):
                boxes[box] = [x if x[0] != label else (label,power) for x in boxes[box]]
            else:
                boxes[box].append((label,power))
    ans = 0
    for box_num, box in enumerate(boxes):
        for idx, item in enumerate(box):
            ans += (box_num+1)*(idx+1)*item[1]
    return ans

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))