class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = list()

        board = [["."] * n for i in range(n)]
        
        column = set()
        negativeDia = set()
        positiveDia = set()
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return 
            for c in range(n):
                if (c in column or
                    (r - c) in negativeDia or
                    (r + c) in positiveDia):
                    continue 
                else:
                    column.add(c)
                    negativeDia.add(r - c)
                    positiveDia.add(r + c)
                    board[r][c] = "Q"
            
                    # next row
                    dfs(r + 1)

                    column.remove(c)
                    negativeDia.remove(r - c)
                    positiveDia.remove(r + c)
                    board[r][c] = "."
        
        dfs(0)
        return res

s = Solution().solveNQueens(4)
print(s)