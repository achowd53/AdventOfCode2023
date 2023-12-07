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
    hands = map(lambda x: [x.split()[0],int(x.split()[1])], open(filename).read().splitlines())
    def strength(hand):
        count = sorted([*collections.Counter(hand[0]).values()])
        st = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
        return (count[-1]*2+(len(count)>1 and count[-2]==2),)+tuple(st[c] for c in hand[0])+(hand[1],)
    hands = (sorted(hands, reverse=True, key=lambda x: strength(x)) + [[0,0]])[::-1]
    return sum(i*hands[i][1] for i in range(len(hands)))

def runPart2(filename):    
    hands = map(lambda x: [x.split()[0],int(x.split()[1])], open(filename).read().splitlines())
    def strength(hand):
        if (h:=hand[0]) != "JJJJJ":
            h = h.replace("J",next(c for c,_ in collections.Counter(h).most_common() if c!='J'))
        count = sorted([*collections.Counter(h).values()])
        st = {'A':14,'K':13,'Q':12,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'J':1}
        return (count[-1]*2+(len(count)>1 and count[-2]==2),)+tuple(st[c] for c in hand[0])+(hand[1],)
    hands = (sorted(hands, reverse=True, key=lambda x: strength(x)) + [[0,0]])[::-1]
    return sum(i*hands[i][1] for i in range(len(hands)))
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))