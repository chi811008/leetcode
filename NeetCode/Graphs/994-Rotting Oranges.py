from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, columns = len(grid), len(grid[0])
        
        time, fresh = 0, 0
        def rot(r, c, fresh):
            if (r > -1 and
                c > -1 and
                r < rows and
                c < columns and 
                grid[r][c] == 1):

                q.append([r, c])
                grid[r][c] = 2
                fresh -= 1
            return fresh

        # find rotten source
        q = deque(list())
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                # rot adjacent 
                fresh = rot(r + 1, c, fresh)
                fresh = rot(r - 1, c, fresh)
                fresh = rot(r, c + 1, fresh)
                fresh = rot(r, c - 1, fresh)
            time += 1
        
        return time if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
s = Solution().orangesRotting(grid)
print(s)