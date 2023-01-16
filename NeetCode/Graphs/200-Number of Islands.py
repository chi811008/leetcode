from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        island = set()
        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r > len(grid) - 1 or
                c > len(grid[0]) - 1 or
                grid[r][c] == "0" or
                (r, c) in island):
                island.add((r, c))
                return
            else:
                island.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
        
                if grid[r][c] == "0" or (r, c) in island:
                    continue
                else:
                    dfs(r, c)
                    res += 1
        return res

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                if grid[r][c] == "1":
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
            return

        island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        return island

grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
         
visited = set()

def dfs(r, c):
    q = deque([(r, c)])
    
    while q:
        r, c = q.pop()
        visited.add((r, c))
        if grid[r][c] == "1":
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
    return

island = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "1" and (r, c) not in visited:
            dfs(r, c)
            island += 1
print(island) 

