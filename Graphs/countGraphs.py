def connectComponents(graph):
    visited = set()
    count = 0
    for node in graph:
        if traverse(graph, node, visited): 
            count += 1
    return count
def traverse(graph, node, visited):
    if node in visited:
        return False
    visited.add(node)

    for nei in graph[node]:
        traverse(graph, nei, visited)
    
    return True