def bfs(graph, source): 
    queue = [source]
    while queue:
        node = queue.pop(0)
        print(node)
        for nei in graph[node]:
            queue.append(nei)
    

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(bfs(graph=graph, source='a'))