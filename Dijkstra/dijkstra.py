import networkx as nx
import matplotlib.pyplot as plt

print("hello 1")

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 6), ('D', 1)],
    'C': [('A', 5), ('B', 6), ('D', 3)],
    'D': [('B', 1), ('C', 3)],
    'E': [('D', 4), ('B', 6)]
}

G = nx.Graph()

for node in graph:
    for neighbor, weight in graph[node]:
        G.add_edge(node, neighbor, weight=weight)







# # Generate layout for consistent positions
# pos = nx.spring_layout(G, seed=42)  

# # Draw nodes and edges
# nx.draw(
#     G, pos,
#     with_labels=True,
#     node_color='skyblue',
#     node_size=1500,
#     font_weight='bold'
# )

# # Draw edge weights
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# plt.title("Graph Visualization")
# plt.show()
