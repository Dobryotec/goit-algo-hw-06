import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(["human1", "human2", "human3", "human4", "human5", "human6"])
G.add_edges_from([("human1", "human2", {"weight": 2}), ("human1", "human5", {"weight": 6}), 
                  ("human2", "human3", {"weight": 7}), ("human3", "human4", {"weight": 3}), 
                  ("human5", "human6", {"weight": 5}), ("human6", "human1", {"weight": 12})])

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3500, node_color="orange")

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attributes in graph[current_vertex].items():
            distance = distances[current_vertex] + attributes["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)

    return distances

print(dijkstra(G, "human1"))

