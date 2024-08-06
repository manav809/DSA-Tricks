def shortestPath(edges, start, end):
    graph = convert(edges)
    queue = [(start, 0)]
    while queue:
        node, dist = queue.pop(0)
        if node == end:
            return dist
        for nei in graph[node]:
            queue.append((nei, dist + 1))
    return None

def convert(edges):
    graph = {}

    for edge in edges:
        x, y = edge
        if x not in graph: graph[x] = []
        if y not in graph: graph[y] = []
        graph[x].append(y)
        graph[y].append(x)
    
    return graph

edges = [
    ['w', 'x'],
    ['x', 'y'], 
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

print(shortestPath(edges=edges, start='w', end='z'))