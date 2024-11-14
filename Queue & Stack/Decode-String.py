class Solution:
    def decodeString(self, s: str) -> str:
        numStack, eleStack = [], []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                tmp = ""
                while s[i].isnumeric():
                    tmp += s[i]
                    i += 1
                numStack.append(int(tmp))
            elif s[i] == "]":
                tmp = []
                while eleStack[-1] != "[":
                    tmp.append(eleStack.pop())
                eleStack.pop()
                eleStack.append("".join(tmp[::-1]) * numStack.pop())
                i += 1
            else:
                eleStack.append(s[i])
                i += 1

        return "".join(eleStack)


def runTests():
    s = Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc", "Test case 1 failed"
    assert s.decodeString("3[a2[c]]") == "accaccacc", "Test case 2 failed"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", "Test case 3 failed"
    assert s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz", "Test case 4 failed"
    assert s.decodeString("100[leetcode]") == "leetcode" * 100, "Test case 5 failed"
    assert (
        s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
        == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    ), "Test case 6 failed"
    print("All test cases pass")


if __name__ == "__main__":
    runTests()
