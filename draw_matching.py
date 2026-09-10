import networkx as nx
import matplotlib.pyplot as plt

def draw_matching(edges, matching, cover):
    nodes = [0,1,2,3,4,5,6,7,8,9]
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(nodes)
    pos = nx.spring_layout(G, seed=42)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    #nx.draw(G, with_labels=True)
    edge_colors = []
    matching_set = set([(min(u,v), max(u, v)) for u,v in matching])
    for edge in G.edges():
        u, v = edge
        if((min(u,v), max(u,v)) in matching_set):
            edge_colors.append('red')
        else:
            edge_colors.append('lightblue')
            
    axes[0].set_title("Maximal Matching")
    nx.draw(G, edge_color=edge_colors, with_labels=True, ax=axes[0])
    node_colors = []
    for i in G.nodes():
        if i in cover:
            node_colors.append('red')
        else:
            node_colors.append('lightblue')

    axes[1].set_title("Computed Vertex Cover")
    nx.draw(G, node_color=node_colors, with_labels=True, ax=axes[1])
    plt.title("Matching and Vertex Cover Visulisation")
    plt.show()
    plt.savefig(f"graphpic{len(edges)}")
    plt.close()
    