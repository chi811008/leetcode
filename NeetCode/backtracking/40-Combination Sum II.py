class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, curr, total):
            if total == 0:
                res.append(curr[:])
                return 
            
            if (i > len(candidates) - 1) or (total < 0):
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total-candidates[i])
            curr.pop()

            while i+1<len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            
            dfs(i+1, curr, total)
        dfs(0, [], target)
        return res

def runTest():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))
    
if __name__ == '__main__':
    runTest()