from utils import *

def runPart1(filename):    
    lines = matchLines(filename, None)
        
    ans = None
    for line in lines:
        #a,b = line.split()
        pass
    return ans

def runPart2(filename):    
    lines = matchLines(filename, 'Ints')
        
    ans = None
    for line in lines:
        #a,b = line.split()
        pass
    return ans
        

print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print("Part 2:", runPart2("example.txt"))
#print("Part 2:", runPart2("example2.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))
print("Part 2:", runPart2("input.txt"))