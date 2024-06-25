class Solution:
    def isPalindrome(self, s: str) -> bool:
        head, tail = 0, len(s) - 1
        while head < tail:
            while not is_alnum(s[head]) and head < tail:
                head += 1
            while not is_alnum(s[tail]) and tail > head:
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True

def is_alnum(s: str) -> bool:
    return ((ord("a") <= ord(s) <= ord("z")) or
            (ord("A") <= ord(s) <= ord("Z")) or
            (ord("0") <= ord(s) <= ord("9")))

def runTest():
    solution = Solution()
    test_cases = [
        # ("A man, a plan, a canal: Panama", True),
        # ("race a car", False),
        # ("", True),
        (".,", True),
        # ("0P", False)
    ]
    for s, expected in test_cases:
        result = solution.isPalindrome(s)
        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"{'Pass' if result == expected else 'Fail'}\n")

if __name__ == "__main__":
    runTest()