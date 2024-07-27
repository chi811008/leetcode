from collections import defaultdict, deque

class DisjointSet:
    def __init__(self, n):
        self.stringRoot = [i for i in range(n)]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.stringRoot[rootX] = rootY

    def find(self, x):
        if x != self.stringRoot[x]:
            self.stringRoot[x] = self.find(self.stringRoot[x])
        return self.stringRoot[x]
    
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        djs = DisjointSet(len(s))
        for x, y in pairs:
            djs.union(x, y)
        groupString = defaultdict(list)
        for i in range(len(djs.stringRoot)):
            groupString[djs.find(djs.stringRoot[i])].append(s[i])

        res = ""
        for k, v in groupString.items():
            v.sort()
            groupString[k] = deque(v)
        
        for i in range(len(s)):
            res += groupString[djs.find(djs.stringRoot[i])].popleft()
        return res
        
            
def runTests():
    test_cases = [
		("dcab", [[0,3],[1,2]], "bacd"),
		("dcab", [[0,3],[1,2],[0,2]], "abcd"),
		# ("cba", [[0,1],[1,2]], "abc")
	]
    
    for i, (s, pairs, expected) in enumerate(test_cases):
        result = Solution().smallestStringWithSwaps(s, pairs)
        print(f"Test case {i+1}: {result == expected}")

if __name__ == "__main__":
    runTests()