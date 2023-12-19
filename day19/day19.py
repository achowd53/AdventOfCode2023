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
    workflows = re.findall(r"(\w+){(.+),(\w+)}", open(filename).read())
    workflows = {workflow[0]:[re.findall(r"([\w\d<>]+):(\w+)", workflow[1]), workflow[2]] for workflow in workflows}
    parts = [[*map(int, part)] for part in re.findall(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", open(filename).read())]
    ans = 0
    for x,m,a,s in parts:
        workflow = "in"
        while workflow not in "AR":
            for rule in workflows[workflow][0]:
                if eval(rule[0]):
                    workflow = rule[1]
                    break
            else:
                workflow = workflows[workflow][1]
        if workflow == "A":
            ans += x+m+a+s
    return ans

def runPart2(filename):    
    workflows = re.findall(r"(\w+){(.+),(\w+)}", open(filename).read())
    workflows = {workflow[0]:[re.findall(r"([\w\d<>]+):(\w+)", workflow[1]), workflow[2]] for workflow in workflows}
    def recurse(workflow="in", constraints={'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}):
        if workflow == "R": return 0
        if workflow == "A": return prod(x[1]-x[0]+1 for x in constraints.values())
        workflow_accept = 0
        for rule in workflows[workflow][0]:
            var, gt, val = rule[0][0], (rule[0][1] == ">"), int(rule[0][2:])
            if gt:
                workflow_accept += recurse(rule[1], constraints | {var: (val+1, constraints[var][1])})
                constraints |= {var: (constraints[var][0], val)}
            else:
                workflow_accept += recurse(rule[1], constraints | {var: (constraints[var][0], val-1)})
                constraints |= {var: (val, constraints[var][1])}
        return workflow_accept + recurse(workflows[workflow][1], constraints)
    return recurse()
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))