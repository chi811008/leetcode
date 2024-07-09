class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, curr, total):
            if total == 0:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total < 0:
                return 
            
            curr.append(candidates[i])
            dfs(i, curr, total - candidates[i])
            curr.pop()

            dfs(i + 1, curr, total)
            
        dfs(0, [], target)
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        subSum = []
        def dfs(i):
            if sum(subSum) == target:
                res.append(subSum.copy())
                return
            elif i == len(candidates) or sum(subSum) > target:
                return
            
            subSum.append(candidates[i])
            dfs(i+1)

            subSum.pop()
            dfs(i+1)
        dfs(0)
        return res
        
        
def runTest():
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    r = s.combinationSum(candidates, target)
    print(r)

if __name__ == '__main__':
    runTest()
