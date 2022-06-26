class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        square = defaultdict(set)
        for i in range(9): # fix position: y
            num_box = set()
            for j in range(9):
                ele = board[i][j] # fix y
                if ele == ".":
                    continue
                if ele in num_box:
                    return False
                else:
                    num_box.add(board[i][j])
                # check 3 * 3
                k = i // 3
                l = j // 3
                if ele in square[(k, l)]:
                    return False
                else:
                    square[(k, l)].add(ele)

        # check columns
        for i in range(9): # fix position: x
            num_box = set()
            for j in range(9):
                ele = board[j][i] # fix x
                if ele == ".":
                    continue
                if ele in num_box:
                    return False
                else:
                    num_box.add(board[j][i])
        return True


# check 3 * 3
# for i in range(9):
#     for j in range(9):
#         ele = board[i][j] 
#         if ele == ".":
#             continue
#         k = i // 3
#         l = j // 3
#         if ele in square[(k, l)]:
#             print(False)
#         else:
#             square[(k, l)].add(ele)