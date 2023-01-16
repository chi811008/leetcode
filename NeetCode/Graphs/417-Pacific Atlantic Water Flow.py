class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows, columns = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = list()

        def dfs(r, c, visited, pre_height):
            if (
                r < 0 or
                c < 0 or
                r > rows - 1 or
                c > columns - 1 or
                (r, c) in visited or
                heights[r][c] < pre_height
            ):
                return 
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for c in range(columns):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, columns - 1, atl, heights[r][columns - 1])

        for position in pac:
            if position in atl:
                res.append(list(position))
        return res