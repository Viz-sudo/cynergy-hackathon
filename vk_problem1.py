# find the number of islands
# approach dfs + backtracking
def numOfIslands(grid):
    row = len(grid)
    col = len(grid[0])
    islands = 1
    visit = set()

    def dfs(r,c):
        if not(0<=r<row) or not(0<=c<col) or grid[r][c] == "0" or (r,c) in visit:
            return False
        visit.add((r,c))
        if dfs(r + 1, c): return True
        if dfs(r - 1, c): return True
        if dfs(r, c + 1): return True
        if dfs(r, c - 1): return True
        visit.remove((r,c))
        # removing so that in next iteration we can check the same grid element again

    for i in range(row):
        for j in range(col):
            if dfs(i,j):
                islands += 1
    return islands

grid= [ ["1", "0", "0", "1"],
        ["1", "1", "0", "0"],
        ["0", "1", "0", "0"],
        ["0", "0", "0", "0"] ]
print(numOfIslands(grid))

