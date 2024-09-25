class Solution:
    def isValid(self, s: str) -> bool:
        left = []

        for ele in s:
            if ele == "(" or ele == "{" or ele == "[":
                left.append(ele)
                continue

            if not left:
                return False

            if ele == ")" and left.pop() != "(":
                return False
            elif ele == "}" and left.pop() != "{":
                return False
            elif ele == "]" and left.pop() != "[":
                return False

        return False if left else True


def runTest():
    s = Solution()
    r = s.isValid("(]")
    print(r)


if __name__ == "__main__":
    runTest()
