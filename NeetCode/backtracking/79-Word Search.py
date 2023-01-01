class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        column, row = len(board[0]), len(board)

        def dfs(i, r, c):
            if r > len(board) - 1 or \
               c > len(board[0]) - 1 or \
               r < 0 or \
               c < 0 or \
               (r, c) in path or \
               word[i] != board[r][c]:
                   return
            elif i == len(word) - 1:
                return True

            path.add((r, c))
            res = dfs(i + 1, r, c + 1) or \
                dfs(i + 1, r, c - 1) or \
                    dfs(i + 1, r - 1, c) or \
                        dfs(i + 1, r + 1, c)
            path.remove((r, c))
            return res 
            
        for r in range(row):
            for c in range(column):
                path = set()
                if dfs(0, r, c):
                    return True
        return False
    
                
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
s = Solution().exist(board, word)
print(s)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or
                c < 0 or 
                r >= rows or 
                c >= columns or 
                word[i] != board[r][c] or 
                (r, c) in path):

                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False