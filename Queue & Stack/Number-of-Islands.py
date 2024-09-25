class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r > rows - 1 or r < 0 or c > cols - 1 or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "0":
                    dfs(r, c)
                    count += 1

        return count
