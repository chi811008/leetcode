from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        area = 0

        def bfs(r, c, area):
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                if grid[r][c] == 1:
                    area += 1
                    if (r + 1, c) not in visited and r + 1 < len(grid):
                        q.append((r + 1, c))            
                        visited.add((r + 1, c))
                    if (r - 1, c) not in visited and r - 1 > -1:
                        q.append((r - 1, c))            
                        visited.add((r - 1, c))
                    if (r, c + 1) not in visited and c + 1 < len(grid[0]):
                        q.append((r, c + 1))
                        visited.add((r, c + 1))
                    if (r, c - 1) not in visited and c - 1 > -1:
                        q.append((r, c - 1))
                        visited.add((r, c - 1))
            return area

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = max(area, bfs(r, c, 0))
        return area
grid = [[0,0,0,0,0,0,0,0]]

# s = Solution().maxAreaOfIsland(grid)
# print(s)
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        area = 0
        def dfs(r, c):
            if (r > rows - 1 or
                c > columns - 1 or
                r < 0 or
                c < 0 or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
    
        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r, c))
        return area