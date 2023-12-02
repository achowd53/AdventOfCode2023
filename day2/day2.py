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
    ans = 0
    for line in lines:
        id = int(re.findall(r'Game (\d+):', line)[0])
        if all([int(match)<=limit for color,limit in[("red",12),("green", 13),("blue",14)]for match in re.findall(rf'(\d+) {color}',line)]):
            ans += id
    return ans

def runPart2(filename):    
    lines = open(filename).read().splitlines()
    ans = 0
    for line in lines:
        ans += prod(max(int(match)for match in re.findall(rf'(\d+) {color}',line))for color in["red", "green", "blue"])
    return ans
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))