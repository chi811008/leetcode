board =[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
# check rows
for i in range(9): # fix position: y
    num_box = set()
    for j in range(9):
        ele = board[i][j] # fix y
        if ele == ".":
            continue
        if ele in num_box:
            print(False)
        else:
            num_box.add(board[i][j])

# check columns
for i in range(9): # fix position: x
    num_box = set()
    for j in range(9):
        ele = board[j][i] # fix x
        if ele == ".":
            continue
        if ele in num_box:
            print(False)
        else:
            num_box.add(board[j][i])

# check 9 * 9
