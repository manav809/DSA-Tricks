visited = set()

def islandCount(grid):
    smallest = float("inf")

    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            
                count = dfs(grid, visited, row, col, rows, cols) 
                if count == 0:
                    continue 
                
                smallest = min(smallest, count)
    return smallest

def dfs(grid, visited, row, col, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return 0
    if (row, col) in visited:
        return 0
    if grid[row][col] != 'L':
        return 0
    visited.add((row, col))
    count = 1

    count += dfs(grid, visited, row + 1, col, rows, cols)
    count += dfs(grid, visited, row - 1, col, rows, cols)
    count += dfs(grid, visited, row, col + 1, rows, cols)
    count += dfs(grid, visited, row, col - 1, rows, cols)
    
    return count 



print(islandCount([
    ['W', 'L', 'L', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]))