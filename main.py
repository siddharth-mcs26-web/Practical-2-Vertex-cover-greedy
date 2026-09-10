from graph_generator import generate_graph
from read_output import read_file
from draw_matching import draw_matching
from greedy_vc import greedy_vc

n = 10
for m in range(10, 46, 5):
    generate_graph(n, m)
    graph = read_file(f"graph{m}.txt")
    cover, matching = greedy_vc(graph)
    draw_matching(graph, matching, cover)
    

    