from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        grid = defaultdict(set)
        for i in range(len(board)):
            rowNum, colNum = set(), set()
            for j in range(len(board[i])):
                # check rows
                if board[i][j].isdigit() & (board[i][j] in rowNum):
                    return False
                # check column
                if board[j][i].isdigit() & (board[j][i] in colNum):
                    return False
                # check 3*3
                key = (i//3, j//3)
                if board[i][j].isdigit() & (board[i][j] in grid[key]):
                    return False
                rowNum.add(board[i][j])
                colNum.add(board[j][i])
                grid[key].add(board[i][j])
                
        return True

def runTest():
    s = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))

if __name__ == "__main__":
    runTest()