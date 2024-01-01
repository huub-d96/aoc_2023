import copy
import sys
import matplotlib.pyplot as plt
import networkx as nx

data ='''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = [line for line in data.strip().splitlines()]

#Part 1
x_max = len(data[0])
y_max = len(data)

sys.setrecursionlimit(100000)

def printPath(path):
    for y in range(y_max):
        for x in range(x_max):

            if (x,y) in path:
                print('O', end='')
            else:
                print(data[y][x], end='')
        print()
    print()

def walk(path):

    current_tile = path[-1]

    if current_tile == end:
        return path

    paths = []
    longest = 0
    long_path = None
    for (nx,ny,slope) in [(0,1,'v'), (0,-1, '^'), (1,0, '>'), (-1,0,'<')]:
        next_tile = (current_tile[0]+nx, current_tile[1]+ny)

        #Do not backtrack
        if next_tile in path:
            continue

        #Stay within bounds
        if not (0 <= next_tile[0] < x_max) or not( 0 <= next_tile[1] < y_max):
            continue

        #Cannot go trough forest
        if data[next_tile[1]][next_tile[0]] == '#':
            continue

        #Can only go one way trough slopes
        if data[next_tile[1]][next_tile[0]] in ['v', '^', '<', '>'] and data[next_tile[1]][next_tile[0]] != slope:
            continue

        new_path = walk(path + [next_tile])

        if len(new_path) > longest:
            longest = len(new_path)
            long_path = new_path

    if not long_path:
        return []
 
    return long_path


start = (1,0)
end = (x_max-2, y_max-1)
path = [start]

path = walk(path)
print('Part 1 - Longest Path:', len(path)-1)

# Part 2

#Build a weighted graph based on the map recursively
network = {}
def scout(prev_loc, loc, from_loc, dist):

    next_tiles = []
    for (nx,ny) in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_tile = (loc[0]+nx, loc[1]+ny)
    
            #Do not backtrack
            if next_tile == prev_loc:
                continue
    
            #Stay within bounds
            if not (0 <= next_tile[0] < x_max) or not( 0 <= next_tile[1] < y_max):
                continue
    
            #Cannot go trough forest
            if data[next_tile[1]][next_tile[0]] == '#':
                continue
    
            next_tiles.append(next_tile)

    routes = len(next_tiles)

    if routes == 0 and not loc == end:
        return 
        
    if routes == 1:
        return scout(loc, next_tiles[0], from_loc, dist+1)

    node1 = f'{from_loc}-{loc}'
    node2 = f'{loc}-{from_loc}'
    
    if node1 in network.keys() or node2 in network.keys():
        return
    
    network[node1] = dist+1
    
    for tile in next_tiles:
        scout(loc, tile, loc, 0)
    
    return

#Build the network
scout(start, start, start, 0)


# Generate graph for analysis
G = nx.Graph()

for k,v, in network.items():
    a,b = k.split('-')

    G.add_edge(a,b,weight=v)

#Cut down runtime by not including the endpoint the path genarator, as it only has one neighbour
almost_end = [n for n in G.neighbors(f'{end}')][0]

#Find the longest path by checking every possibility
longest = 0
for path in nx.all_simple_edge_paths(G, f'{start}', f'{almost_end}'):
    total = 0
    for e1, e2 in path:
        e = f'{e1}-{e2}'
        if e not in network.keys():
            e = f'{e2}-{e1}'

        total += network[e]

    if total > longest:
        longest = total
        
print('Part 2:',longest-1 + G[f'{end}'][almost_end]['weight'])


#Print the graph for visualization
pos = nx.spring_layout(G, seed=200)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=200)

# edges
nx.draw_networkx_edges(G, pos,  width=6)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", verticalalignment='top', font_color='red')

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
