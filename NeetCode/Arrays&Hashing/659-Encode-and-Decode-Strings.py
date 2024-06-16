class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + f"#{s}")
        return res
            
    def decode(self, s: str) -> list[str]:
        res = []
        head, i = 0, 0
        while i < len(s):
            if s[i].isdigit():
                i += 1
            if s[i] == "#":
                wordLen = int(s[head:i])
                word = s[i+1:i+1+wordLen]
                res.append(word)
                i += 1+wordLen
                head = i
        return res

def runTest():
    s = Solution()
    l=["we","say",":","yes","!@#$%^&*()"]
    r = s.encode(l)
    print(r)
    print(s.decode(r))

if __name__ == "__main__":
    runTest()