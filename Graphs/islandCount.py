visited = set()

def islandCount(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'L' and (row, col) not in visited:
                count += 1
                dfs(grid, visited, row, col, rows, cols)
    return count

def dfs(grid, visited, row, col, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    if (row, col) in visited or grid[row][col] != 'L':
        return

    visited.add((row, col))

    dfs(grid, visited, row + 1, col, rows, cols)
    dfs(grid, visited, row - 1, col, rows, cols)
    dfs(grid, visited, row, col + 1, rows, cols)
    dfs(grid, visited, row, col - 1, rows, cols)
    
    return 



print(islandCount([
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]))