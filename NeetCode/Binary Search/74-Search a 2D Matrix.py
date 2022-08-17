matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0
def find_row(head_row, tail_row):
    if head_row > tail_row:
        print(tail_row)
        return tail_row
    mid_row = (head_row + tail_row) // 2
    num = matrix[mid_row][0]
    if num == target:
        return mid_row
    elif num < target:
        return find_row(mid_row + 1, tail_row)
    elif num > target:
        return find_row(head_row, mid_row - 1)
ans_row = find_row(0, len(matrix) - 1)

def find_column(head_column, tail_colum):
    if head_column > tail_colum:
        return False
    mid_column = (head_column + tail_colum) // 2
    num = matrix[ans_row][mid_column]
    if num == target:
        return True
    elif num > target:
        return find_column(head_column, mid_column - 1)
    elif num < target:
        return find_column(mid_column + 1, tail_colum)
ans = find_column(0, len(matrix[0]) - 1)
print(ans)