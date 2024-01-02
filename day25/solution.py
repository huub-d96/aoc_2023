import copy
import sys
import matplotlib.pyplot as plt
import networkx as nx

data ='''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()


# Generate graph for analysis
G = nx.Graph()

for line in data.strip().splitlines():
    f, tt = line.split(': ')

    for t in tt.strip().split(' '):
        G.add_edge(f,t)

cut_edges = nx.minimum_edge_cut(G)

for e in cut_edges:
    G.remove_edge(*e)

sub_sizes = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
print('Part 1:', sub_sizes[0]*sub_sizes[1])

#Print the graph for visualization
pos = nx.spring_layout(G, seed=200)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=200)

# edges
nx.draw_networkx_edges(G, pos,  width=2)

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
