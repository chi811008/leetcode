def solution(moves):
    # 確保字串長度在 1 到 100 之間
    if not 1 <= len(moves) <= 100:
        return False

    # 確保只有 ^, v, <, > 四種字元
    if not all(c in "^v<>" for c in moves):
        return False

    # 確保每個方向的移動至少出現一次
    if not (">" in moves and "<" in moves and "^" in moves and "v" in moves):
        return False

    # 追蹤位置
    x = y = 0
    visited = {(0, 0)}

    # 記錄每個方向的移動位置
    y1 = y2 = None
    x1 = x2 = None

    for move in moves:
        # 更新位置
        if move == ">":
            x += 1
            if y2 is None:
                y2 = y
            elif y2 != y:
                return False
        elif move == "<":
            x -= 1
            if y1 is None:
                y1 = y
            elif y1 != y:
                return False
        elif move == "^":
            y += 1
            if x1 is None:
                x1 = x
            elif x1 != x:
                return False
        else:  # move == 'v'
            y -= 1
            if x2 is None:
                x2 = x
            elif x2 != x:
                return False

        # 檢查重複訪問
        if (x, y) in visited and (x, y) != (0, 0):
            return False

        # 檢查是否提前回到原點
        if (x, y) == (0, 0) and len(visited) < len(moves):
            return False

        visited.add((x, y))

    # 檢查最終位置
    if (x, y) != (0, 0):
        return False

    return True


# 測試案例
test_cases = [
    ">>vv<<^^",  # True
    ">vv<<^^>",  # True
    ">>vv<<^",  # False
    ">v<^",  # True
    ">>vv<<",  # False
    ">v>v<<^^",  # False
    "><",  # False
]

for test in test_cases:
    print(f"{test}: {solution(test)}")
