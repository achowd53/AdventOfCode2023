import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up, reduce
from math import log, prod, lcm
from string import ascii_uppercase, ascii_lowercase, ascii_letters #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from more_itertools import chunked, windowed #chunked, windowed
from scanf import scanf
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
import portion # Interval stuff
from z3 import Solver, Int, And
from sympy.ntheory.modular import crt
#Sets are {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def runPart1(filename):    
    inst = re.findall(r'(\w+)\n\n', open(filename).read())[0]
    nodes = re.findall(r'(\w+) = \((\w+), (\w+)\)', open(filename).read())
    nodes = {node[0]:{'L':node[1],'R':node[2]} for node in nodes}
    cur, idx, ans = "AAA", 0, 0
    while cur != "ZZZ":
        cur = nodes[cur][inst[idx]]
        idx = (idx+1)%len(inst)
        ans += 1
    return ans
    

def runPart2(filename):    
    inst = re.findall(r'(\w+)\n\n', open(filename).read())[0]
    nodes = re.findall(r'(\w+) = \((\w+), (\w+)\)', open(filename).read())
    nodes = {node[0]:{'L':node[1],'R':node[2]} for node in nodes}
    curs, ans = [node for node in nodes if node[-1]=="A"], []
    for cur in curs:
        path, idx = 0, 0
        while cur[-1] != "Z":
            cur = nodes[cur][inst[idx]]
            idx = (idx+1)%len(inst)
            path += 1
        ans.append(path)
    return lcm(*ans)
    

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example2.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))