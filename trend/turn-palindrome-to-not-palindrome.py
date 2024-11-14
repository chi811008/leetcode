def isPalindrome(s: str) -> bool:
    head, tail = 0, len(s) - 1
    while head < tail:
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1
    return True


def solution(S):
    if not isPalindrome(S):
        return 0

    # 字串是回文的情況
    n = len(S)

    # 如果所有字符都相同，需要刪除所有字符
    if all(c == S[0] for c in S):
        return n

    # 一般的回文，刪除一個字符即可
    return 1


# 測試案例
test_cases = [
    "xyz",  # 應該返回 0，因為已經不是回文
    "kayak",  # 應該返回 1，刪除一個字符後變成 "ayak"
    "xxxx",  # 應該返回 3，需要刪到只剩一個 x
    "abba",  # 應該返回 1，刪除一個字符後不是回文
    "a",  # 應該返回 1，刪除一個字符後變成空字串
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {solution(test)}")
    print("---")
