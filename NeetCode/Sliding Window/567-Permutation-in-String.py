# class Solution:
#     def checkInclusion(self, s1:str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
#         s1Hash = [0] * 26
#         for c in s1:
#             s1Hash[ord(c) - ord("a")] += 1
        
#         for l in range(len(s2)):
#             if s1Hash[ord(s2[l]) - ord("a")] > 0:
#                 if isPermutation(l, l+len(s1), s2, s1Hash):
#                     return True
#         return False


# def isPermutation(l, r, s, s1Hash):
#     perHash = [0] * 26
#     for c in s[l:r]:
#         perHash[ord(c) - ord("a")] += 1
#     return perHash == s1Hash
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1:str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1CharCount = defaultdict(int)
        s2CharCount = defaultdict(int)
        for i in range(len(s1)):
            s1CharCount[s1[i]] += 1
            s2CharCount[s2[i]] += 1

        matches = 0
        for i in range(26):
            if s1CharCount[chr(ord("a")+i)] == s2CharCount[chr(ord("a")+i)]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            s2CharCount[s2[r]] += 1
            if s2CharCount[s2[r]] == s1CharCount[s2[r]]:
                matches += 1
            elif s2CharCount[s2[r]] - 1 == s1CharCount[s2[r]]:
                matches -= 1

            s2CharCount[s2[l]] -= 1
            if s2CharCount[s2[l]] == s1CharCount[s2[l]]:
                matches += 1
            elif s2CharCount[s2[l]] + 1 == s1CharCount[s2[l]]:
                matches -= 1
            l += 1
        return matches == 26


def runTest():
    s1 = "adc"
    s2 = "dcda"
    result = Solution().checkInclusion(s1, s2)
    print("expected: True", "got:", result)
    
if __name__ == '__main__':
    runTest()