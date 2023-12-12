import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve, rot90 default axis=1 rotates left axis=0 would be right
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
from collections import defaultdict, Counter
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
    lines = [[line.split()[0],[*map(int,line.split()[1].split(","))]] for line in open(filename).read().splitlines()]
    @lru_cache(None)
    def dp(idx=0, grp_len=0, grp_match=0):
        if idx == len(line):
            return (grp_len == 0 and grp_match == len(groups)) or (grp_match == len(groups)-1 and grp_len == groups[grp_match])
        ret = 0
        if line[idx] in "#?":
            ret += dp(idx+1, grp_len+1, grp_match)
        if line[idx] in ".?":
            if grp_match < len(groups) and grp_len == groups[grp_match]:
                ret += dp(idx+1, 0, grp_match+1)
            elif grp_len == 0:
                ret += dp(idx+1, 0, grp_match)
        return ret
    ans = 0
    for line, groups in lines:
        ans += dp()
        dp.cache_clear()
    return ans  

def runPart2(filename):    
    lines = [[line.split()[0],[*map(int,line.split()[1].split(","))]] for line in open(filename).read().splitlines()]
    @lru_cache(None)
    def dp(idx=0, grp_len=0, grp_match=0):
        if idx == len(line):
            return (grp_len == 0 and grp_match == len(groups)) or (grp_match == len(groups)-1 and grp_len == groups[grp_match])
        ret = 0
        if line[idx] in "#?":
            ret += dp(idx+1, grp_len+1, grp_match)
        if line[idx] in ".?":
            if grp_match < len(groups) and grp_len == groups[grp_match]:
                ret += dp(idx+1, 0, grp_match+1)
            elif grp_len == 0:
                ret += dp(idx+1, 0, grp_match)
        return ret
    ans = 0
    for line, groups in lines:
        line = line+"?"+line+"?"+line+"?"+line+"?"+line
        groups = groups*5
        ans += dp()
        dp.cache_clear()
    return ans

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))