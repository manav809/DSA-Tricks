def hasPath_dfs(graph, src, dst): 
    if src == dst:
        return True
    for i in graph[src]:
        if (hasPath_dfs(graph, i, dst) == True):
            return True 
    return False


def hasPath_bfs(graph, src, dst):
    queue = [src]
    
    while queue:
        node  = queue.pop()
        if node ==  dst:
            return True
        for nei in graph[node]:
            queue.append(nei)
    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(hasPath_dfs(graph=graph, src='f', dst='k'))
print(hasPath_bfs(graph=graph, src='f', dst='k'))

