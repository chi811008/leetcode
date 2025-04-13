class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        def dfs(i, j):
            if (i < 0) or \
            (j < 0) or \
            (i > rows - 1) or \
            (j > columns - 1) or \
            (grid[i][j] == "0"):
                return 0
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i , j - 1)
            return 1

        count = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    count += dfs(r, c)
        return count