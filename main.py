from graph_generator import generate_graph
from read_output import read_file
from draw_matching import draw_matching
from greedy_vc import greedy_vc
import pandas as pd
import time
n = 10
data = []
for m in range(10, 46, 5):
    generate_graph(n, m)
    graph = read_file(f"graph{m}.txt")
    start_time = time.perf_counter()
    cover, matching = greedy_vc(graph)
    end_time = time.perf_counter()
    draw_matching(graph, matching, cover)
    data.append({
        "n" : n,
        "m" : m,
        "size_of_vc" : len(cover),
        "size_of_matching" : len(matching),
        "approximation_factor" : 2,
        "running_time" : round(end_time - start_time, 10)
    })

df = pd.DataFrame(data)
csv_filename = "vertex_cover_results.csv"
df.to_csv(csv_filename, index=False)
print(data)
    

    