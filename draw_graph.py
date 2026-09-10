import matplotlib.pyplot as plt
import networkx as nx
def draw_graph(edges, cover):
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(range(10))
    colors = []
    for node in G.nodes():
        if node in cover:
            colors.append('red')
        else:
            colors.append('lightblue')
    nx.draw(G,node_color=colors, with_labels=True)
    print(len(edges))
    plt.savefig(f"graphpic{len(edges)}")
    plt.close()