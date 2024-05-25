import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(["human1", "human2", "human3", "human4", "human5", "human6"])

G.add_edges_from([("human1", "human2"), ("human1", "human5"),
                  ("human2", "human3"), ("human3", "human4"), ("human5", "human6"),
                  ("human6", "human1")])
pos = nx.circular_layout(G)
nx.draw(G, with_labels=True, node_size = 3500, node_color="orange")

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

plt.figure(figsize=(8, 6))
plt.title("Network of people")
plt.text(0.05, 0.95, f"Кількість вершин: {num_nodes}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f"Кількість ребер: {num_edges}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())
degree_info = "\n".join([f"{node}: вхідний - {in_degrees[node]}, вихідний - {out_degrees[node]}" for node in G.nodes()])

plt.text(0.05, 0.70, "Ступені вершин:", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.65, degree_info, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

plt.show()