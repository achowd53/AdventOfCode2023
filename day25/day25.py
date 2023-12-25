from utils import *

def runPart1(filename):    
    lines = matchLines(filename, r'\w+')
    adj_list = {line[0]:line[1:] for line in lines}
    G = createNetworkXGraphFromAdjacency(adj_list)
    cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(cuts) 
    return prod(map(len,nx.connected_components(G)))


print("Running example.txt...")
print("Part 1:", runPart1("example.txt"))
print()
print("Running input.txt...")
print("Part 1:", runPart1("input.txt"))