def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())

def hasPath(graph, source, destination, visited):
    if source in visited: return False
    if source == destination: return True
    
    visited.add(source)

    for nei in graph[source]:
        if hasPath(graph, nei, destination, visited):
            return True
    return False

def buildGraph(edges):  
    graph = {}

    for edge in edges:
        a, b = edge
        if a != graph:
            graph[a] = []
        if b != graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)