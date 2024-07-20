def dfs(graph, source):
    stack = [source]

    while stack:
        node = stack.pop()
        print(node)

        for nei in graph[node]: 
            stack.append(nei)
          
def dfs_recur(graph, source):
    print(source)
    for nei in graph[source]:
        dfs_recur(graph, nei)
         

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(dfs(graph=graph, source='a'))