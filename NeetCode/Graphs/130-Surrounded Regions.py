board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","O"],["O","O"]]
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])
        
        visited = set()
        def dfs(r, c):
            if (
                r < 0 or
                c < 0 or
                r > rows - 1 or
                c > columns - 1 or
                (r, c) in visited or
                board[r][c] == "X"
            ):
                return 
            visited.add((r, c))
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. DFS capture unsurrounding regions (O -> T)
        for c in range(columns):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        for r in range(1, rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][columns - 1] == "O":
                dfs(r, columns - 1)
        
        # 2. capture surrounding regions (O -> X)
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"
                # 3. uncapture unsurrounding regions (O -> T)
                elif board[r][c] == "T":
                    board[r][c] = "O"
        return board
s = Solution().solve(board)
print(s)