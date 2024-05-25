import networkx as nx
from collections import deque


G = nx.DiGraph()

G.add_nodes_from(["human1", "human2", "human3", "human4", "human5", "human6"])
G.add_edges_from([("human1", "human2"), ("human1", "human5"),
                  ("human2", "human3"), ("human3", "human4"), ("human5", "human6"),
                  ("human6", "human1")])

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)

print("DFS шлях:")
dfs(G, "human1")
print("\nBFS шлях:")
bfs(G, "human1")




