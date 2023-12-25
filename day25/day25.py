from utils import *

def runPart1(filename):    
    lines = matchLines(filename, None)
    adj_list = {line.split(':')[0]:line.split(': ')[1].split() for line in lines}
    G = nx.Graph()
    for pos in adj_list:
        for adj in adj_list[pos]:
            G.add_edge(pos,adj,capacity=1.0)
    for x,y in combinations(adj_list.keys(), 2):
        cuts, partition = nx.minimum_cut(G,x,y)
        if cuts == 3:
            return prod(map(len,partition))


print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))