class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        partition = []
        
        def dfs(i):
            if i == len(s):
                res.append(partition[:])
            
            for j in range(i, len(s)):
                if self.is_palindrome(i, j, s):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res
    
    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

def runTest():
    s = "aab"
    sol = Solution()
    print(sol.partition(s))
    
if __name__ == "__main__":
    runTest()