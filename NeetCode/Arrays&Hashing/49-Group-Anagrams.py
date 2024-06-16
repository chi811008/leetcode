from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
            


def runTest():
    strs = ["tin","ram","zip","cry","pus","jon","zip","pyx"]
    s = Solution()
    print(s.groupAnagrams(strs))
    
if __name__ == "__main__":
    runTest()

