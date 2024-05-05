# Implement Greedy search algorithm for: Minimum Spanning Tree in python
import heapq

def prim_mst(graph):
    n = len(graph)
    visited = [False] * n
    mst = []
    heap = []

    def visit(vertex):
        visited[vertex] = True
        for neighbor, weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(heap, (weight, vertex, neighbor))

    visit(0)

    while heap:
        weight, u, v = heapq.heappop(heap)
        if not visited[v]:
            mst.append((u, v, weight))
            visit(v)

    return mst

# Example graph represented as an adjacency list
graph = [
    [(1, 4), (2, 5)],
    [(0, 4), (2, 2), (3, 3)],
    [(0, 5), (1, 2), (3, 1)],
    [(1, 3), (2, 1)]
]

# Find the Minimum Spanning Tree using Prim's algorithm
mst = prim_mst(graph)
print("Minimum Spanning Tree (Prim's algorithm):")
for edge in mst:
    print(edge)
