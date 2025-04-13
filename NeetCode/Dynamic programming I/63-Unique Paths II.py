class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        dp = [[0 for i in range(columns)] for i in range(rows)]
        dp[0][0] = 1
        for r in range(rows):
            for c in range(columns):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r - 1 >= 0:
                    dp[r][c] += dp[r - 1][c]
                if c - 1 >= 0:
                    dp[r][c] += dp[r][c - 1]
        return dp[-1][-1]