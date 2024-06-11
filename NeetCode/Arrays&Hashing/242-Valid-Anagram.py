class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = dict(), dict()
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for key in countS.keys():
            if countS[key] != countT.get(key, 0):
                return False
        return True

def runTest ():
    s = "nagaram"
    t = "anagram"
    solu = Solution()
    print(solu.isAnagram(s, t))
    
if __name__ == '__main__':
    runTest()
      