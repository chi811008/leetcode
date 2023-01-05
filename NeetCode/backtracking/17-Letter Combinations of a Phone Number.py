class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        res = list()

        def dfs(i, combination):
            if len(combination) == len(digits):
                res.append(combination)
                return

            for c in num_char[digits[i]]:
                dfs(i + 1, combination + c)
        if digits:
            dfs(0, "")
        return res