# 這是一個字串處理問題，主要需要避免三個連續相同的字符。
# S 中的字符如果是 "?" 才需要從 elements 裡面挑選，否則直接加入 currStr。

# 這個問題可以用 backtracking 來解，這裡的 backtracking 函數有兩個參數，i 代表當前處理到的 S 的 index，currStr 代表當前的字串。
# 如果 currStr 的長度等於 S 的長度，就把 currStr 加入 res 中。
# 如果 S[i] 是 "?"，就把 elements 中的字符加入 currStr，然後繼續遞迴。
# 如果 S[i] 不是 "?"，就直接把 S[i] 加入 currStr，然後繼續遞迴。
# 還有限制就是不能有連續 3 個 a 或 3 個 b，所以在遞迴的時候要檢查 currStr 的最後三個字符是否有三個連續相同的字符，如果有就不繼續遞迴。
# 最後返回 res。


def solution(S):
    elements = ["a", "b"]
    res = []

    def backtracking(i, currStr):
        if len(currStr) >= 3 and currStr[-3] == currStr[-2] == currStr[-1]:
            return
        if len(currStr) == len(S):
            res.append(currStr)
            return

        if S[i] == "?":
            for c in elements:
                backtracking(i + 1, currStr + c)
        else:
            backtracking(i + 1, currStr + S[i])

    backtracking(0, "")
    return res[0]


# 測試案例
test_cases = [
    "a?bb",  # 應返回 "aabb"
    "??abb",  # 應返回 "ababb" 或 "bbabb" 或 "baabb"
    "a?b?aa",  # 應返回 "aabbaa"
    "aa??aa",  # 應返回 "aabbaa"
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {solution(test)}")
    print("---")
