def largestComponent(graph):
    visited = set()
    max_count = 0
    for node in graph:
        size = traverse(graph, node, visited)
        max_count = max(size, max_count)
    return max_count

def traverse(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for nei in graph[node]:
        size += traverse(graph , nei, visited)
    return size

print(largestComponent(
    graph={
        0: [8,1,5], 
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2,4],
        4: [3, 2]
    }
))