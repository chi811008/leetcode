class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(m)] for i in range(n)]

        rows = n
        columns = m
        grid[0][0] = 1
        for r in range(rows):
            for c in range(columns):
                if r - 1 >= 0:
                    grid[r][c] += grid[r - 1][c]
                if c - 1 >= 0:
                    grid[r][c] += grid[r][c - 1]
        return grid[-1][-1]